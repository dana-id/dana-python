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

import os
import re
from typing import Any, Callable, Dict, FrozenSet, List, Set

from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException

# Money value pattern: digits (1-16) + "." + exactly 2 digits (e.g. 10000.00)
MONEY_VALUE_PATTERN = re.compile(r'^\d{1,16}\.\d{2}$')

SANDBOX_ALLOWED_PAY_METHODS: FrozenSet[str] = frozenset({
    'BALANCE', 'CREDIT_CARD', 'DEBIT_CARD', 'VIRTUAL_ACCOUNT', 'NETWORK_PAY',
})

SANDBOX_ALLOWED_PAY_OPTIONS: FrozenSet[str] = frozenset({
    'CARD', 'QRIS', 'BRI', 'PANIN', 'CIMB', 'MANDIRI', 'BTPN',
})

CREDIT_DEBIT_CARD_PAY_METHODS: Set[str] = {'CREDIT_CARD', 'DEBIT_CARD'}
NETWORK_PAY_PG_CARD = 'NETWORK_PAY_PG_CARD'
EWALLET_PAY_OPTIONS: Set[str] = {
    'NETWORK_PAY_PG_SPAY',
    'NETWORK_PAY_PG_OVO',
    'NETWORK_PAY_PG_GOPAY',
    'NETWORK_PAY_PG_LINKAJA',
}


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
    return len(list(s))


def _ctx(field: str, message: str) -> Dict[str, str]:
    return {'field': field, 'message': message}


def validate_additional_info_required(request: Any) -> None:
    if request is None:
        return
    if hasattr(request, 'additional_info') and request.additional_info is None:
        raise ApiException(status=0, contexts=[_ctx('additionalInfo', 'additionalInfo is required')])


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
    if request is None:
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


def validate_sandbox_pay_method_and_pay_option(request: Any) -> None:
    if request is None or not _is_sandbox():
        return
    pay_option_details = getattr(request, 'pay_option_details', None)
    if not pay_option_details or not isinstance(pay_option_details, list):
        return
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
                            f'In sandbox, payMethod must be one of [{", ".join(sorted(SANDBOX_ALLOWED_PAY_METHODS))}]; '
                            f'got {pm_str}'
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
                            f'In sandbox, payOption must be one of [{", ".join(sorted(SANDBOX_ALLOWED_PAY_OPTIONS))}] '
                            f'(or suffix like VIRTUAL_ACCOUNT_BRI); got {po_str}'
                        ),
                    )
                ])


def validate_conditional_pay_option_additional_info_create_order_request(request: Any) -> None:
    if request is None:
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

        is_card = pay_method in CREDIT_DEBIT_CARD_PAY_METHODS or pay_option == NETWORK_PAY_PG_CARD
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
                    'externalUserType is required when externalUserId is filled',
                )
            )
        if has_type and not has_id:
            contexts.append(
                _ctx(
                    'additionalInfo.order.buyer.externalUserId',
                    'externalUserId is required when externalUserType is filled',
                )
            )

    goods = getattr(order, 'goods', None)
    if isinstance(goods, list) and len(goods) > 0:
        for i, g in enumerate(goods):
            if not g:
                continue
            name = _trim_str(getattr(g, 'name', None))
            if not name:
                contexts.append(
                    _ctx(
                        f'additionalInfo.order.goods[{i}].name',
                        'name is required when goods is filled',
                    )
                )

    shipping_info = getattr(order, 'shipping_info', None)
    if isinstance(shipping_info, list) and len(shipping_info) > 0:
        for i, s in enumerate(shipping_info):
            if not s:
                continue
            first_name = _trim_str(getattr(s, 'first_name', None))
            if not first_name:
                contexts.append(
                    _ctx(
                        f'additionalInfo.order.shippingInfo[{i}].firstName',
                        'firstName is required when shippingInfo is filled',
                    )
                )

    if contexts:
        raise ApiException(status=0, contexts=contexts)


validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'CreateOrderByApiRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
        validate_sandbox_pay_method_and_pay_option,
        validate_conditional_pay_option_additional_info_create_order_request,
        validate_optional_fields_with_required_nested_create_order_request,
    ],
    'CreateOrderByRedirectRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
        validate_sandbox_pay_method_and_pay_option,
        validate_conditional_pay_option_additional_info_create_order_request,
        validate_optional_fields_with_required_nested_create_order_request,
    ],
    'CreateOrderRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
        validate_sandbox_pay_method_and_pay_option,
        validate_conditional_pay_option_additional_info_create_order_request,
        validate_optional_fields_with_required_nested_create_order_request,
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
