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

This module provides custom validation functions for Payment Gateway API requests.
Validations are registered in the validation_registry and executed via custom_validation().
"""

import json
import os
import re
from types import SimpleNamespace
from typing import Any, Callable, Dict, FrozenSet, List, Optional, Set

from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException

# Money value pattern: digits (1-16) + "." + exactly 2 digits (e.g. 10000.00)
MONEY_VALUE_PATTERN = re.compile(r'^\d{1,16}\.\d{2}$')

SANDBOX_ALLOWED_PAY_METHODS: FrozenSet[str] = frozenset({
    'BALANCE', 'CREDIT_CARD', 'DEBIT_CARD', 'VIRTUAL_ACCOUNT', 'NETWORK_PAY',
})

SANDBOX_ALLOWED_PAY_OPTIONS: FrozenSet[str] = frozenset({
    'CARD', 'QRIS', 'BRI', 'PANI', 'CIMB', 'BTPN', 'BSI_PAYMENT',
})

# Sandbox maximum amount (major units) for Payment Gateway create order.
SANDBOX_MAX_AMOUNT = 10000000

CARD_PAY_METHODS: Set[str] = {'CARD', 'CREDIT_CARD', 'DEBIT_CARD'}
NETWORK_PAY_PG_CARD = 'NETWORK_PAY_PG_CARD'
EWALLET_PAY_OPTIONS: Set[str] = {
    'NETWORK_PAY_PG_SPAY',
    'NETWORK_PAY_PG_OVO',
    'NETWORK_PAY_PG_GOPAY',
    'NETWORK_PAY_PG_LINKAJA',
}

SANDBOX_QRIS_GUIDANCE_HINT_SUCCESS = (
    'If you want to use QRIS and it is not showing in payment methods, make sure you already fill '
    'externalStoreId. See https://dashboard.dana.id/sandbox/submerchants in the external shop id section.'
)
SANDBOX_QRIS_GUIDANCE_HINT_ERROR = (
    'If you want to use QRIS, make sure you fill externalStoreId. See '
    'https://dashboard.dana.id/sandbox/submerchants in the external shop id section. '
    'For QRIS, partnerReferenceNo max is 25 chars.'
)
SANDBOX_SUB_MERCHANT_ID_GUIDANCE_HINT = (
    'Make sure your subMerchantId exists. You can see it at '
    'https://dashboard.dana.id/sandbox/submerchants in the External Division ID section.'
)


def _is_sandbox() -> bool:
    env = os.getenv('DANA_ENV', os.getenv('ENV', 'sandbox')).lower()
    return env == 'sandbox'


def _pay_option_allowed_in_sandbox(value: str) -> bool:
    if not value or not str(value).strip():
        return False
    s = str(value).strip()
    if s in SANDBOX_ALLOWED_PAY_OPTIONS:
        return True
    for opt in SANDBOX_ALLOWED_PAY_OPTIONS:
        if s.endswith('_' + opt):
            return True
    return False


def _normalize_value(value: Any) -> str:
    if value is None:
        return ''
    if hasattr(value, 'value'):
        return str(getattr(value, 'value')).strip()
    return str(value).strip()


def _trim_str(value: Any) -> str:
    if value is None:
        return ''
    return str(value).strip()


def _rune_len(s: str) -> int:
    return len(s)


def _ctx(field: str, message: str) -> Dict[str, str]:
    return {'field': field, 'message': message}


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


def validate_additional_info_required(request: Any) -> None:
    if request is None:
        return
    if hasattr(request, 'additional_info') and request.additional_info is None:
        raise ApiException(status=0, contexts=[_ctx('additionalInfo', 'additionalInfo is required')])


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
    """Reject empty strings for required additionalInfo fields (mcc, envInfo.terminalType)."""
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return

    contexts: List[Dict[str, str]] = []
    if not _trim_str(getattr(additional_info, 'mcc', None)):
        contexts.append(
            _ctx('additionalInfo.mcc', 'additionalInfo.mcc is required and cannot be empty')
        )

    env_info = getattr(additional_info, 'env_info', None)
    terminal_type = getattr(env_info, 'terminal_type', None) if env_info is not None else None
    if not _trim_str(terminal_type):
        contexts.append(
            _ctx(
                'additionalInfo.envInfo.terminalType',
                'additionalInfo.envInfo.terminalType is required and cannot be empty',
            )
        )

    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_money_value_pattern(request: Any) -> None:
    if request is None:
        return
    if not hasattr(request, 'amount') or request.amount is None:
        return
    value = getattr(request.amount, 'value', None)
    if value is None or value == '':
        raise ApiException(status=0, contexts=[_ctx('amount.value', 'amount.value is required')])
    if not MONEY_VALUE_PATTERN.match(str(value)):
        raise ApiException(status=0, contexts=[
            _ctx('amount.value', f'amount.value must match pattern (e.g. 10000.00): got {value!r}')
        ])


def validate_sandbox_amount(request: Any) -> None:
    """In sandbox, amount.value must not exceed SANDBOX_MAX_AMOUNT."""
    if request is None or not _is_sandbox():
        return
    if not hasattr(request, 'amount') or request.amount is None:
        return
    value = getattr(request.amount, 'value', None)
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


def validate_valid_up_to_create_order_request(request: Any) -> None:
    if request is None:
        return
    if hasattr(request, 'valid_up_to') and request.valid_up_to is not None:
        try:
            validate_valid_up_to_date(request.valid_up_to)
        except ValueError as e:
            raise ApiException(status=0, contexts=[
                _ctx('validUpTo', f'validUpTo validation failed: {str(e)}')
            ]) from e


def validate_external_store_id_for_qris(request: Any) -> None:
    """API-only: externalStoreId required when payOption is NETWORK_PAY_PG_QRIS."""
    if request is None:
        return
    if request.__class__.__name__ == 'CreateOrderByRedirectRequest':
        return
    if not hasattr(request, 'pay_option_details') or request.pay_option_details is None:
        return
    has_qris = False
    if isinstance(request.pay_option_details, list):
        for pay_option_detail in request.pay_option_details:
            if hasattr(pay_option_detail, 'pay_option') and pay_option_detail.pay_option == 'NETWORK_PAY_PG_QRIS':
                has_qris = True
                break
    if has_qris:
        external_store_id = None
        if hasattr(request, 'external_store_id'):
            external_store_id = request.external_store_id
        if not external_store_id or (isinstance(external_store_id, str) and external_store_id.strip() == ''):
            raise ApiException(status=0, contexts=[
                _ctx('externalStoreId', 'externalStoreId is required when payOption is NETWORK_PAY_PG_QRIS')
            ])


def validate_partner_reference_no_for_qris(request: Any) -> None:
    """API-only: partnerReferenceNo max 25 when payOption is NETWORK_PAY_PG_QRIS."""
    if request is None:
        return
    if request.__class__.__name__ == 'CreateOrderByRedirectRequest':
        return
    if not hasattr(request, 'pay_option_details') or request.pay_option_details is None:
        return
    has_qris = False
    if isinstance(request.pay_option_details, list):
        for pay_option_detail in request.pay_option_details:
            if hasattr(pay_option_detail, 'pay_option') and pay_option_detail.pay_option == 'NETWORK_PAY_PG_QRIS':
                has_qris = True
                break
    if not has_qris:
        return
    partner_reference_no = _trim_str(getattr(request, 'partner_reference_no', None))
    if _rune_len(partner_reference_no) > 25:
        raise ApiException(status=0, contexts=[
            _ctx(
                'partnerReferenceNo',
                'partnerReferenceNo must be at most 25 characters when payOption is NETWORK_PAY_PG_QRIS',
            )
        ])


def validate_sandbox_pay_method_and_pay_option(request: Any) -> None:
    if request is None or not _is_sandbox():
        return
    pay_option_details = getattr(request, 'pay_option_details', None)
    if not pay_option_details or not isinstance(pay_option_details, list):
        return
    allowed_methods = 'BALANCE, CREDIT_CARD, DEBIT_CARD, VIRTUAL_ACCOUNT, NETWORK_PAY'
    allowed_options = 'CARD, QRIS, BRI, PANI, CIMB, BTPN, BSI_PAYMENT'
    for i, detail in enumerate(pay_option_details):
        if not detail:
            continue
        if hasattr(detail, 'pay_method') and detail.pay_method is not None:
            pm_str = _normalize_value(detail.pay_method)
            if pm_str and pm_str not in SANDBOX_ALLOWED_PAY_METHODS:
                raise ApiException(status=0, contexts=[
                    _ctx(
                        f'payOptionDetails[{i}].payMethod',
                        (
                            f'in sandbox, payMethod must be one of [{allowed_methods}]; '
                            f'got {pm_str!r} in payOptionDetails[{i}]'
                        ),
                    )
                ])
        if hasattr(detail, 'pay_option') and detail.pay_option is not None:
            po_str = _normalize_value(detail.pay_option)
            if po_str and not _pay_option_allowed_in_sandbox(po_str):
                raise ApiException(status=0, contexts=[
                    _ctx(
                        f'payOptionDetails[{i}].payOption',
                        (
                            f'in sandbox, payOption must be one of [{allowed_options}] '
                            f'(or suffix like VIRTUAL_ACCOUNT_BRI); got {po_str!r} in payOptionDetails[{i}]'
                        ),
                    )
                ])


def validate_conditional_pay_option_additional_info_create_order_request(request: Any) -> None:
    if request is None:
        return
    if request.__class__.__name__ == 'CreateOrderByRedirectRequest':
        return
    pay_option_details = getattr(request, 'pay_option_details', None)
    if not pay_option_details or not isinstance(pay_option_details, list):
        return

    contexts: List[Dict[str, str]] = []

    for i, detail in enumerate(pay_option_details):
        if not detail:
            continue
        pay_method = _trim_str(getattr(detail, 'pay_method', None))
        pay_option = _trim_str(getattr(detail, 'pay_option', None))
        additional_info = getattr(detail, 'additional_info', None)
        phone_raw = None
        if additional_info is not None:
            phone_raw = getattr(additional_info, 'phone_number', None)
        phone_number = _trim_str(phone_raw)

        is_card = pay_method in CARD_PAY_METHODS or pay_option == NETWORK_PAY_PG_CARD
        is_ewallet = pay_option in EWALLET_PAY_OPTIONS

        if is_card or is_ewallet:
            field = f'payOptionDetails[{i}].additionalInfo.phoneNumber'
            if not phone_number:
                contexts.append(
                    _ctx(field, f'phoneNumber is required for card/e-wallet payment (payOptionDetails[{i}])')
                )
            else:
                ln = _rune_len(phone_number)
                if ln < 1 or ln > 15:
                    contexts.append(
                        _ctx(field, f'phoneNumber must be between 1 and 15 characters (payOptionDetails[{i}])')
                    )

    if contexts:
        raise ApiException(status=0, contexts=contexts)


def validate_optional_fields_with_required_nested_create_order_request(request: Any) -> None:
    if request is None:
        return
    additional_info = getattr(request, 'additional_info', None)
    if additional_info is None:
        return
    order = getattr(additional_info, 'order', None)
    if not order:
        return

    contexts: List[Dict[str, str]] = []

    buyer = getattr(order, 'buyer', None)
    if buyer:
        ext_type = _trim_str(getattr(buyer, 'external_user_type', None))
        ext_id = _trim_str(getattr(buyer, 'external_user_id', None))
        has_type = bool(ext_type)
        has_id = bool(ext_id)
        if has_id and not has_type:
            contexts.append(
                _ctx(
                    'additionalInfo.order.buyer.externalUserType',
                    'additionalInfo.order.buyer.externalUserType is required when externalUserId is filled',
                )
            )
        if has_type and not has_id:
            contexts.append(
                _ctx(
                    'additionalInfo.order.buyer.externalUserId',
                    'additionalInfo.order.buyer.externalUserId is required when externalUserType is filled',
                )
            )

    goods = getattr(order, 'goods', None)
    if isinstance(goods, list) and len(goods) > 0:
        for i, g in enumerate(goods):
            if not g:
                continue
            prefix = f'additionalInfo.order.goods[{i}]'
            if not _trim_str(getattr(g, 'name', None)):
                contexts.append(_ctx(f'{prefix}.name', f'{prefix}.name is required when goods is filled'))
            if not _trim_str(getattr(g, 'merchant_goods_id', None)):
                contexts.append(
                    _ctx(f'{prefix}.merchantGoodsId', f'{prefix}.merchantGoodsId is required when goods is filled')
                )
            if not _trim_str(getattr(g, 'description', None)):
                contexts.append(
                    _ctx(f'{prefix}.description', f'{prefix}.description is required when goods is filled')
                )
            if not _trim_str(getattr(g, 'category', None)):
                contexts.append(
                    _ctx(f'{prefix}.category', f'{prefix}.category is required when goods is filled')
                )
            if not _trim_str(getattr(g, 'quantity', None)):
                contexts.append(
                    _ctx(f'{prefix}.quantity', f'{prefix}.quantity is required when goods is filled')
                )
            price = getattr(g, 'price', None)
            price_value = _trim_str(getattr(price, 'value', None)) if price is not None else ''
            price_currency = _trim_str(getattr(price, 'currency', None)) if price is not None else ''
            if not price_value:
                contexts.append(
                    _ctx(f'{prefix}.price.value', f'{prefix}.price.value is required when goods is filled')
                )
            if not price_currency:
                contexts.append(
                    _ctx(f'{prefix}.price.currency', f'{prefix}.price.currency is required when goods is filled')
                )

    shipping_info = getattr(order, 'shipping_info', None)
    if isinstance(shipping_info, list) and len(shipping_info) > 0:
        for i, s in enumerate(shipping_info):
            if not s:
                continue
            prefix = f'additionalInfo.order.shippingInfo[{i}]'
            required_fields = [
                ('merchant_shipping_id', 'merchantShippingId'),
                ('country_name', 'countryName'),
                ('state_name', 'stateName'),
                ('city_name', 'cityName'),
                ('address1', 'address1'),
                ('first_name', 'firstName'),
                ('last_name', 'lastName'),
                ('zip_code', 'zipCode'),
            ]
            for attr, camel in required_fields:
                if not _trim_str(getattr(s, attr, None)):
                    contexts.append(
                        _ctx(
                            f'{prefix}.{camel}',
                            f'{prefix}.{camel} is required when shippingInfo is filled',
                        )
                    )

    if contexts:
        raise ApiException(status=0, contexts=contexts)


validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'CreateOrderByApiRequest': [
        default_source_platform,
        validate_additional_info_required,
        validate_required_additional_info_fields_not_empty,
        validate_money_value_pattern,
        validate_sandbox_amount,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
        validate_partner_reference_no_for_qris,
        validate_conditional_pay_option_additional_info_create_order_request,
        validate_sandbox_pay_method_and_pay_option,
        validate_optional_fields_with_required_nested_create_order_request,
    ],
    'CreateOrderByRedirectRequest': [
        default_source_platform,
        validate_additional_info_required,
        validate_required_additional_info_fields_not_empty,
        validate_money_value_pattern,
        validate_sandbox_amount,
        validate_valid_up_to_create_order_request,
        validate_sandbox_pay_method_and_pay_option,
        validate_optional_fields_with_required_nested_create_order_request,
    ],
    'CreateOrderRequest': [
        default_source_platform,
        validate_additional_info_required,
        validate_required_additional_info_fields_not_empty,
        validate_money_value_pattern,
        validate_sandbox_amount,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
        validate_partner_reference_no_for_qris,
        validate_conditional_pay_option_additional_info_create_order_request,
        validate_sandbox_pay_method_and_pay_option,
        validate_optional_fields_with_required_nested_create_order_request,
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
    """Augment CreateOrder responses in sandbox (QRIS / subMerchantId guidance)."""
    if not _is_sandbox() or request is None or response is None:
        return
    if not hasattr(response, 'response_message'):
        return

    # SUCCESS QRIS hint ONLY for CreateOrderByRedirectRequest without externalStoreId
    if request.__class__.__name__ == 'CreateOrderByRedirectRequest':
        external_store_id = getattr(request, 'external_store_id', None)
        if not (external_store_id and str(external_store_id).strip()):
            object.__setattr__(
                response,
                'response_message',
                _append_sandbox_hint(
                    response.response_message,
                    SANDBOX_QRIS_GUIDANCE_HINT_SUCCESS,
                    'externalstoreid',
                ),
            )

    sub_merchant_id = getattr(request, 'sub_merchant_id', None)
    if sub_merchant_id and str(sub_merchant_id).strip():
        response_code = getattr(response, 'response_code', None)
        if _is_business_error_response(response_code):
            object.__setattr__(
                response,
                'response_message',
                _append_sandbox_hint(
                    response.response_message,
                    SANDBOX_SUB_MERCHANT_ID_GUIDANCE_HINT,
                    'submerchantid',
                    'externaldivisionid',
                ),
            )


def enrich_create_order_error(request: Any, exc: ApiException) -> ApiException:
    """Enrich CreateOrder HTTP errors in sandbox (keeps exception; updates reason / data)."""
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

    response = SimpleNamespace(
        response_code=str(payload.get('responseCode') or ''),
        response_message=str(payload.get('responseMessage') or ''),
        partner_reference_no=str(payload.get('partnerReferenceNo') or ''),
    )
    custom_validation_response(request, response)

    reason = exc.reason
    # ERROR QRIS hint on exception reason for Redirect without externalStoreId (Go puts on err string)
    if request.__class__.__name__ == 'CreateOrderByRedirectRequest':
        external_store_id = getattr(request, 'external_store_id', None)
        if not (external_store_id and str(external_store_id).strip()):
            hinted = _append_sandbox_hint(
                '',
                SANDBOX_QRIS_GUIDANCE_HINT_ERROR,
                'externalstoreid',
                'partnerreferenceno',
            )
            status = exc.status if exc.status is not None else ''
            reason = f'{status}: {hinted}'

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
        reason=reason,
        body=exc.body,
        data=enriched_data,
    )
    enriched.headers = getattr(exc, 'headers', None)
    return enriched
