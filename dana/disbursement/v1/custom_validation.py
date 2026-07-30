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

This module provides custom validation functions for Disbursement API requests.
Validations are registered in the validation_registry and executed via custom_validation().
"""

import json
import os
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Optional

from dana.exceptions import ApiException


SANDBOX_BENEFICIARY_ACCOUNT_NUMBER = '2460888509'
SANDBOX_BENEFICIARY_BANK_CODE = '014'
# Sandbox maximum amount (major units) for Disbursement.
SANDBOX_MAX_AMOUNT = 20000000
ALLOWED_ACCOUNT_TYPES = frozenset({
    'MERCHANT_DEPOSIT_ACCOUNT',
    'SETTLEMENT_ACCOUNT',
    'DIVISION_DEPOSIT_ACCOUNT',
})

SANDBOX_DANA_BALANCE_LIMIT_HINT = (
    'Make sure DANA balance not exceeding limit of 21000000 after topup'
)


def _is_sandbox() -> bool:
    env = os.getenv('DANA_ENV', os.getenv('ENV', 'sandbox')).lower()
    return env == 'sandbox'


def _ctx(field: str, message: str) -> Dict[str, str]:
    return {'field': field, 'message': message}


def _trim_str(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()


def _append_sandbox_hint(
    response_message: Optional[str],
    hint: str,
    *already_present_markers: str,
) -> str:
    """Always append (Go-compatible). Uses markers to avoid duplicates. No 150-char truncate."""
    msg = (response_message or '').strip()
    lower_msg = msg.lower()
    for marker in already_present_markers:
        if marker and marker.lower() in lower_msg:
            return msg
    if not msg:
        return hint
    if msg.endswith('.'):
        return f'{msg} {hint}'
    return f'{msg}. {hint}'


def _is_business_error_response(response_code: Any) -> bool:
    code = str(response_code or '').strip()
    return code == '' or not code.startswith('200')


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


def _require_non_empty(value: Any, field_path: str) -> None:
    if not _trim_str(value):
        raise ApiException(status=0, contexts=[
            _ctx(field_path, f'{field_path} is required and cannot be empty')
        ])


def _validate_account_type_value(value: str, field_path: str) -> None:
    if value not in ALLOWED_ACCOUNT_TYPES:
        raise ApiException(status=0, contexts=[_ctx(
            field_path,
            (
                f'{field_path} must be one of '
                f'[MERCHANT_DEPOSIT_ACCOUNT, SETTLEMENT_ACCOUNT, DIVISION_DEPOSIT_ACCOUNT]; got {value!r}'
            ),
        )])


def strip_sandbox_ignored_fields_bank_account_inquiry(request: Any) -> None:
    """In sandbox, accountType, beneficiaryAccountName, externalDivisionId, and chargeTarget are ignored."""
    if request is None or not _is_sandbox():
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    if hasattr(additional_info, 'account_type'):
        additional_info.account_type = None
    if hasattr(additional_info, 'beneficiary_account_name'):
        additional_info.beneficiary_account_name = None
    if hasattr(additional_info, 'external_division_id'):
        additional_info.external_division_id = None
    if hasattr(additional_info, 'charge_target'):
        additional_info.charge_target = None


def strip_sandbox_ignored_fields_transfer_to_bank(request: Any) -> None:
    """In sandbox, clear top-level accountType plus additionalInfo beneficiary/division charge fields."""
    if request is None or not _is_sandbox():
        return
    if hasattr(request, 'account_type'):
        request.account_type = None
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is not None and hasattr(additional_info, 'beneficiary_account_name'):
        additional_info.beneficiary_account_name = None
    if additional_info is not None and hasattr(additional_info, 'external_division_id'):
        additional_info.external_division_id = None
    if additional_info is not None and hasattr(additional_info, 'charge_target'):
        additional_info.charge_target = None


def strip_sandbox_ignored_fields_transfer_to_dana(request: Any) -> None:
    """In sandbox, clear additionalInfo.accountType, externalDivisionId, and chargeTarget."""
    if request is None or not _is_sandbox():
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    if hasattr(additional_info, 'account_type'):
        additional_info.account_type = None
    if hasattr(additional_info, 'external_division_id'):
        additional_info.external_division_id = None
    if hasattr(additional_info, 'charge_target'):
        additional_info.charge_target = None


def strip_sandbox_ignored_fields_dana_account_inquiry(request: Any) -> None:
    """In sandbox, clear additionalInfo.externalDivisionId and chargeTarget."""
    if request is None or not _is_sandbox():
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    if hasattr(additional_info, 'external_division_id'):
        additional_info.external_division_id = None
    if hasattr(additional_info, 'charge_target'):
        additional_info.charge_target = None


def validate_account_type_bank_account_inquiry(request: Any) -> None:
    """Non-sandbox: if accountType is set, it must be a valid enum value. Empty is allowed (no default)."""
    if request is None or _is_sandbox():
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    current = _trim_str(getattr(additional_info, 'account_type', None))
    if not current:
        return
    _validate_account_type_value(current, 'additionalInfo.accountType')


def validate_account_type_transfer_to_bank(request: Any) -> None:
    if request is None or _is_sandbox():
        return
    current = _trim_str(getattr(request, 'account_type', None))
    if not current:
        return
    _validate_account_type_value(current, 'accountType')


def validate_account_type_transfer_to_dana(request: Any) -> None:
    if request is None or _is_sandbox():
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    current = _trim_str(getattr(additional_info, 'account_type', None))
    if not current:
        return
    _validate_account_type_value(current, 'additionalInfo.accountType')


def validate_sandbox_beneficiary_bank_account_inquiry(request: Any) -> None:
    """In sandbox, beneficiaryAccountNumber must be 2460888509 and beneficiaryBankCode must be 014."""
    if request is None or not _is_sandbox():
        return
    contexts: List[Dict[str, str]] = []
    account_number = _trim_str(getattr(request, 'beneficiary_account_number', None))
    if account_number != SANDBOX_BENEFICIARY_ACCOUNT_NUMBER:
        contexts.append(_ctx(
            'beneficiaryAccountNumber',
            (
                f'in sandbox, beneficiaryAccountNumber must be {SANDBOX_BENEFICIARY_ACCOUNT_NUMBER}; '
                f'got {getattr(request, "beneficiary_account_number", None)!r}'
            ),
        ))
    additional_info = getattr(request, 'additional_info', None)
    bank_code = _trim_str(
        getattr(additional_info, 'beneficiary_bank_code', None) if additional_info is not None else None
    )
    if bank_code != SANDBOX_BENEFICIARY_BANK_CODE:
        contexts.append(_ctx(
            'additionalInfo.beneficiaryBankCode',
            (
                f'in sandbox, additionalInfo.beneficiaryBankCode must be {SANDBOX_BENEFICIARY_BANK_CODE}; '
                f'got {bank_code!r}'
            ),
        ))
    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_sandbox_beneficiary_transfer_to_bank(request: Any) -> None:
    """In sandbox, beneficiaryAccountNumber must be 2460888509 and beneficiaryBankCode must be 014."""
    if request is None or not _is_sandbox():
        return
    contexts: List[Dict[str, str]] = []
    account_number = _trim_str(getattr(request, 'beneficiary_account_number', None))
    if account_number != SANDBOX_BENEFICIARY_ACCOUNT_NUMBER:
        contexts.append(_ctx(
            'beneficiaryAccountNumber',
            (
                f'in sandbox, beneficiaryAccountNumber must be {SANDBOX_BENEFICIARY_ACCOUNT_NUMBER}; '
                f'got {getattr(request, "beneficiary_account_number", None)!r}'
            ),
        ))
    bank_code = _trim_str(getattr(request, 'beneficiary_bank_code', None))
    if bank_code != SANDBOX_BENEFICIARY_BANK_CODE:
        contexts.append(_ctx(
            'beneficiaryBankCode',
            (
                f'in sandbox, beneficiaryBankCode must be {SANDBOX_BENEFICIARY_BANK_CODE}; '
                f'got {getattr(request, "beneficiary_bank_code", None)!r}'
            ),
        ))
    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_required_additional_info_not_empty_bank_account_inquiry(request: Any) -> None:
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    contexts: List[Dict[str, str]] = []
    try:
        _require_non_empty(getattr(additional_info, 'fund_type', None), 'additionalInfo.fundType')
    except ApiException as e:
        contexts.extend(e.contexts or [])
    try:
        _require_non_empty(
            getattr(additional_info, 'beneficiary_bank_code', None),
            'additionalInfo.beneficiaryBankCode',
        )
    except ApiException as e:
        contexts.extend(e.contexts or [])
    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_required_additional_info_not_empty_transfer_to_bank(request: Any) -> None:
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    _require_non_empty(getattr(additional_info, 'fund_type', None), 'additionalInfo.fundType')


def validate_required_additional_info_not_empty_transfer_to_dana(request: Any) -> None:
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    _require_non_empty(getattr(additional_info, 'fund_type', None), 'additionalInfo.fundType')


def validate_required_additional_info_not_empty_dana_account_inquiry(request: Any) -> None:
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    _require_non_empty(getattr(additional_info, 'fund_type', None), 'additionalInfo.fundType')


validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'BankAccountInquiryRequest': [
        strip_sandbox_ignored_fields_bank_account_inquiry,
        validate_account_type_bank_account_inquiry,
        validate_sandbox_beneficiary_bank_account_inquiry,
        validate_sandbox_amount,
        validate_required_additional_info_not_empty_bank_account_inquiry,
    ],
    'TransferToBankRequest': [
        strip_sandbox_ignored_fields_transfer_to_bank,
        validate_account_type_transfer_to_bank,
        validate_sandbox_beneficiary_transfer_to_bank,
        validate_sandbox_amount,
        validate_required_additional_info_not_empty_transfer_to_bank,
    ],
    'TransferToDanaRequest': [
        strip_sandbox_ignored_fields_transfer_to_dana,
        validate_account_type_transfer_to_dana,
        validate_sandbox_amount,
        validate_required_additional_info_not_empty_transfer_to_dana,
    ],
    'DanaAccountInquiryRequest': [
        strip_sandbox_ignored_fields_dana_account_inquiry,
        validate_sandbox_amount,
        validate_required_additional_info_not_empty_dana_account_inquiry,
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


def custom_validation_response(request: Any, response: Any) -> None:
    """Augment TransferToDana responses in sandbox on business errors."""
    if not _is_sandbox() or request is None or response is None:
        return
    if request.__class__.__name__ != 'TransferToDanaRequest':
        return
    if not hasattr(response, 'response_message'):
        return
    response_code = getattr(response, 'response_code', None)
    if not _is_business_error_response(response_code):
        return
    response.response_message = _append_sandbox_hint(
        response.response_message,
        SANDBOX_DANA_BALANCE_LIMIT_HINT,
        '21000000',
        'after topup',
    )


def enrich_transfer_to_dana_error(request: Any, exc: ApiException) -> ApiException:
    """Enrich TransferToDana HTTP errors in sandbox (keeps exception; updates data)."""
    if not _is_sandbox() or request is None or exc is None:
        return exc
    if request.__class__.__name__ != 'TransferToDanaRequest':
        return exc

    body = exc.body
    if body is None or body == '':
        return exc

    try:
        if isinstance(body, (bytes, bytearray)):
            body_str = body.decode('utf-8')
        else:
            body_str = str(body)
        payload = json.loads(body_str)
    except (TypeError, ValueError, UnicodeDecodeError):
        return exc
    if not isinstance(payload, dict):
        return exc

    response = SimpleNamespace(
        response_code=str(payload.get('responseCode') or ''),
        response_message=str(payload.get('responseMessage') or ''),
        partner_reference_no=str(payload.get('partnerReferenceNo') or ''),
    )
    custom_validation_response(request, response)

    enriched_data = {
        'responseCode': response.response_code,
        'responseMessage': response.response_message,
        'partnerReferenceNo': response.partner_reference_no,
    }
    if isinstance(exc.data, dict):
        enriched_data = {**exc.data, **enriched_data}

    # Preserve subclass (e.g. NotFoundException for HTTP 404) so callers can catch by type
    enriched = type(exc)(
        status=exc.status,
        reason=exc.reason,
        body=exc.body,
        data=enriched_data,
    )
    enriched.headers = getattr(exc, 'headers', None)
    return enriched
