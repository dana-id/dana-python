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


ALLOWED_ACCOUNT_TYPES = frozenset({
    'MERCHANT_DEPOSIT_ACCOUNT',
    'SETTLEMENT_ACCOUNT',
    'DIVISION_DEPOSIT_ACCOUNT',
})

SANDBOX_POSITIVE_BENEFICIARY_ACCOUNT_NUMBER = '2460888509'
SANDBOX_POSITIVE_BENEFICIARY_BANK_CODE = '014'
SANDBOX_MAX_AMOUNT = 20000000

SANDBOX_POSITIVE_BANK_HINT = (
    f'For testing positive case in sandbox use beneficiaryAccountNumber '
    f'{SANDBOX_POSITIVE_BENEFICIARY_ACCOUNT_NUMBER} and beneficiaryBankCode '
    f'{SANDBOX_POSITIVE_BENEFICIARY_BANK_CODE}'
)

SANDBOX_AMOUNT_MAX_HINT = f'In sandbox, amount.value must not exceed {SANDBOX_MAX_AMOUNT}'

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
    """Always append. Uses markers to avoid duplicates. No 150-char truncate."""
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


def _should_append_dana_balance_hint(response_code: Any, response_message: Any) -> bool:
    msg = str(response_message or '').lower()
    if 'exceed' in msg or 'melebihi' in msg:
        return True
    return str(response_code or '').strip() == '4033802'


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
        validate_required_additional_info_not_empty_bank_account_inquiry,
    ],
    'TransferToBankRequest': [
        strip_sandbox_ignored_fields_transfer_to_bank,
        validate_account_type_transfer_to_bank,
        validate_required_additional_info_not_empty_transfer_to_bank,
    ],
    'TransferToDanaRequest': [
        strip_sandbox_ignored_fields_transfer_to_dana,
        validate_account_type_transfer_to_dana,
        validate_required_additional_info_not_empty_transfer_to_dana,
    ],
    'DanaAccountInquiryRequest': [
        strip_sandbox_ignored_fields_dana_account_inquiry,
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


def _is_bank_transfer_request(request: Any) -> bool:
    return request.__class__.__name__ in ('BankAccountInquiryRequest', 'TransferToBankRequest')


def _should_append_positive_bank_hint(response_code: Any) -> bool:
    return str(response_code or '').strip().startswith('500')


def _should_append_amount_max_hint(response_message: Any) -> bool:
    msg = str(response_message or '').lower()
    return 'exceed' in msg or 'melebihi' in msg


def _apply_sandbox_disbursement_hints(request: Any, response: Any) -> None:
    if not hasattr(response, 'response_message'):
        return
    response_code = getattr(response, 'response_code', None)
    response_message = getattr(response, 'response_message', None)

    updated = str(response_message or '')

    if _is_bank_transfer_request(request) and _should_append_positive_bank_hint(response_code):
        updated = _append_sandbox_hint(
            updated,
            SANDBOX_POSITIVE_BANK_HINT,
            SANDBOX_POSITIVE_BENEFICIARY_ACCOUNT_NUMBER,
            f'beneficiarybankcode {SANDBOX_POSITIVE_BENEFICIARY_BANK_CODE}',
        )

    if request.__class__.__name__ == 'TransferToDanaRequest':
        if _should_append_dana_balance_hint(response_code, response_message):
            updated = _append_sandbox_hint(
                updated,
                SANDBOX_DANA_BALANCE_LIMIT_HINT,
                '21000000',
                'after topup',
            )
    elif _should_append_amount_max_hint(response_message):
        updated = _append_sandbox_hint(updated, SANDBOX_AMOUNT_MAX_HINT, str(SANDBOX_MAX_AMOUNT))

    if updated != str(response_message or ''):
        response.response_message = updated


def custom_validation_response(request: Any, response: Any) -> None:
    """Augment Disbursement responses in sandbox with account/amount guidance."""
    if not _is_sandbox() or request is None or response is None:
        return
    _apply_sandbox_disbursement_hints(request, response)


def enrich_disbursement_error(request: Any, exc: ApiException) -> ApiException:
    """Enrich Disbursement HTTP errors in sandbox (keeps exception; updates reason / data).
    """
    if not _is_sandbox() or request is None or exc is None:
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

    partner_reference_no = str(
        payload.get('partnerReferenceNo')
        or payload.get('originalPartnerReferenceNo')
        or ''
    )
    response = SimpleNamespace(
        response_code=str(payload.get('responseCode') or ''),
        response_message=str(payload.get('responseMessage') or ''),
        partner_reference_no=partner_reference_no,
    )
    original_msg = response.response_message
    custom_validation_response(request, response)

    reason = exc.reason
    if response.response_message and response.response_message != original_msg:
        status = exc.status if exc.status is not None else ''
        reason = f'{status}: {response.response_message}'

    enriched_data = {
        'responseCode': response.response_code,
        'responseMessage': response.response_message,
        'partnerReferenceNo': response.partner_reference_no,
    }
    if isinstance(exc.data, dict):
        enriched_data = {**exc.data, **enriched_data}

    enriched_body = body_str
    if response.response_message != original_msg:
        enriched_payload = dict(payload)
        enriched_payload['responseCode'] = enriched_data['responseCode']
        enriched_payload['responseMessage'] = enriched_data['responseMessage']
        if enriched_data.get('partnerReferenceNo'):
            enriched_payload['partnerReferenceNo'] = enriched_data['partnerReferenceNo']
        enriched_body = json.dumps(enriched_payload)

    # Preserve subclass (e.g. NotFoundException for HTTP 404) so callers can catch by type
    enriched = type(exc)(
        status=exc.status,
        reason=reason,
        body=enriched_body,
        data=enriched_data,
    )
    enriched.headers = getattr(exc, 'headers', None)
    return enriched


def enrich_transfer_to_dana_error(request: Any, exc: ApiException) -> ApiException:
    """Enrich TransferToDana HTTP errors in sandbox (alias for enrich_disbursement_error)."""
    return enrich_disbursement_error(request, exc)
