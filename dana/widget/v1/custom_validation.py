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

from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException


def _ctx(field: str, message: str) -> Dict[str, str]:
    return {'field': field, 'message': message}


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
    """Run all validators for the request type and aggregate client validation contexts."""
    if request is None:
        return

    class_name = request.__class__.__name__
    if class_name not in validation_registry:
        return

    aggregated: List[Dict[str, str]] = []
    for validator in validation_registry[class_name]:
        try:
            validator(request)
        except ApiException as e:
            if e.contexts:
                aggregated.extend(e.contexts)
            else:
                raise

    if aggregated:
        raise ApiException(status=0, contexts=aggregated)
