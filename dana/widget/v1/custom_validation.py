# Copyright 2026 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
CustomValidation

This module provides custom validation functions for Widget API requests.
Validations are registered in the validation_registry and executed via custom_validation().
"""

from typing import Any, Callable, Dict, List
import os

from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException

# Sandbox maximum amount (major units) for Widget payment.
SANDBOX_MAX_AMOUNT = 10000000


def _is_sandbox() -> bool:
    env = os.getenv('DANA_ENV', os.getenv('ENV', 'sandbox')).lower()
    return env == 'sandbox'


def _ctx(field: str, message: str) -> Dict[str, str]:
    return {'field': field, 'message': message}


def _trim_str(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()


def default_source_platform(request: Any) -> None:
    """Set envInfo.sourcePlatform to IPG when missing/empty."""
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    env_info = getattr(additional_info, 'env_info', None)
    if env_info is None:
        return
    source_platform = getattr(env_info, 'source_platform', None)
    if source_platform is None or str(source_platform).strip() == '':
        env_info.source_platform = 'IPG'


def validate_required_additional_info_fields_not_empty(request: Any) -> None:
    """Reject empty strings for required additionalInfo fields.

    Note: mcc may be an empty string for Widget.
    """
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return

    contexts: List[Dict[str, str]] = []
    if hasattr(additional_info, 'product_code') and not _trim_str(getattr(additional_info, 'product_code', None)):
        contexts.append(
            _ctx(
                'additionalInfo.productCode',
                'additionalInfo.productCode is required and cannot be empty',
            )
        )

    env_info = getattr(additional_info, 'env_info', None)
    if env_info is not None and hasattr(env_info, 'terminal_type'):
        terminal_type = getattr(env_info, 'terminal_type', None)
        if not _trim_str(terminal_type):
            contexts.append(
                _ctx(
                    'additionalInfo.envInfo.terminalType',
                    'additionalInfo.envInfo.terminalType is required and cannot be empty',
                )
            )

    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_sandbox_amount(request: Any) -> None:
    """In sandbox, amount.value must not exceed SANDBOX_MAX_AMOUNT."""
    if request is None or not _is_sandbox():
        return
    amount = getattr(request, 'amount', None)
    if amount is None:
        return
    value = getattr(amount, 'value', None)
    if value is None or str(value).strip() == '':
        return
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return
    if parsed > SANDBOX_MAX_AMOUNT:
        raise ApiException(status=0, contexts=[_ctx(
            'amount.value',
            f'in sandbox, amount.value must not exceed {SANDBOX_MAX_AMOUNT}; got {value!r}',
        )])


def validate_valid_up_to_widget_payment_request(request: Any) -> None:
    """Validate validUpTo field in WidgetPaymentRequest."""
    if request is None:
        return
    if hasattr(request, 'valid_up_to') and request.valid_up_to is not None:
        try:
            validate_valid_up_to_date(request.valid_up_to)
        except ValueError as e:
            raise ApiException(status=0, contexts=[
                _ctx('validUpTo', f'validUpTo validation failed: {str(e)}')
            ]) from e


def _contains_forbidden_auth_code_delimiters(auth_code: str) -> bool:
    return '&' in auth_code or '=' in auth_code


def validate_apply_token_auth_code_authorization_code(request: Any) -> None:
    """authCode must not contain URL query delimiter characters (pasted query string)."""
    if request is None:
        return
    auth_code = getattr(request, 'auth_code', None)
    if auth_code is None:
        return
    s = str(auth_code)
    if s and _contains_forbidden_auth_code_delimiters(s):
        raise ApiException(status=0, contexts=[
            _ctx('authCode', "authCode must not contain URL query delimiter characters ('&' or '=')")
        ])


def validate_apply_token_auth_code_refresh_token(request: Any) -> None:
    """If authCode is present on refresh-token request, apply the same rule."""
    if request is None:
        return
    auth_code = getattr(request, 'auth_code', None)
    if auth_code is None:
        return
    trimmed = str(auth_code).strip()
    if not trimmed:
        return
    if _contains_forbidden_auth_code_delimiters(trimmed):
        raise ApiException(status=0, contexts=[
            _ctx('authCode', "authCode must not contain URL query delimiter characters ('&' or '=')")
        ])


validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'WidgetPaymentRequest': [
        default_source_platform,
        validate_required_additional_info_fields_not_empty,
        validate_sandbox_amount,
        validate_valid_up_to_widget_payment_request,
    ],
    'ApplyTokenAuthorizationCodeRequest': [
        validate_apply_token_auth_code_authorization_code,
    ],
    'ApplyTokenRefreshTokenRequest': [
        validate_apply_token_auth_code_refresh_token,
    ],
}


def custom_validation(request: Any) -> None:
    """Run all validators for the request type and aggregate as validation failed: ..."""
    if request is None:
        return

    class_name = request.__class__.__name__
    if class_name not in validation_registry:
        return

    aggregated: List[Dict[str, str]] = []
    messages: List[str] = []
    for validator in validation_registry[class_name]:
        try:
            validator(request)
        except ApiException as e:
            if e.contexts:
                aggregated.extend(e.contexts)
                messages.extend(c.get('message', '') for c in e.contexts if c.get('message'))
            elif e.reason:
                messages.append(str(e.reason))
            else:
                raise

    if messages:
        raise ApiException(
            status=0,
            reason=f"validation failed: {'; '.join(messages)}",
            contexts=aggregated or None,
        )
