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

import re
from typing import Any, Dict, List, Callable
from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException

# Money value pattern: digits (1-16) + "." + exactly 2 digits (e.g. 10000.00)
MONEY_VALUE_PATTERN = re.compile(r'^\d{1,16}\.\d{2}$')


def validate_additional_info_required(request: Any) -> None:
    """
    Validate that additionalInfo must exist.

    Raises:
        ApiException: If additionalInfo is missing
    """
    if request is None:
        return
    if hasattr(request, 'additional_info') and request.additional_info is None:
        raise ApiException(
            status=0,
            reason='additionalInfo is required'
        )


def validate_money_value_pattern(request: Any) -> None:
    """
    Validate that Money value matches pattern (e.g. 10000.00): ^\\d{1,16}\\.\\d{2}$

    Raises:
        ApiException: If amount.value is missing or does not match pattern
    """
    if request is None:
        return
    if not hasattr(request, 'amount') or request.amount is None:
        return
    value = getattr(request.amount, 'value', None)
    if value is None or value == '':
        raise ApiException(
            status=0,
            reason='amount.value is required'
        )
    if not MONEY_VALUE_PATTERN.match(str(value)):
        raise ApiException(
            status=0,
            reason=f'amount.value must match pattern (e.g. 10000.00): got {value!r}'
        )


def validate_valid_up_to_create_order_request(request: Any) -> None:
    """
    Validate validUpTo field in CreateOrderByApiRequest or CreateOrderByRedirectRequest.
    
    This function handles both request types directly (not wrapped in CreateOrderRequest):
    - CreateOrderByApiRequest: validates valid_up_to directly
    - CreateOrderByRedirectRequest: validates valid_up_to directly
    
    Args:
        request: The request object to validate
    
    Raises:
        ApiException: If validation fails
    """
    if request is None:
        return
    
    # Handle CreateOrderByApiRequest or CreateOrderByRedirectRequest directly
    if hasattr(request, 'valid_up_to') and request.valid_up_to is not None:
        try:
            validate_valid_up_to_date(request.valid_up_to)
        except ValueError as e:
            raise ApiException(
                status=0,
                reason=f'validUpTo validation failed: {str(e)}'
            ) from e


def validate_external_store_id_for_qris(request: Any) -> None:
    """
    Validate that externalStoreId is required when payOption is NETWORK_PAY_PG_QRIS.
    
    This function checks if any payOption in payOptionDetails is NETWORK_PAY_PG_QRIS,
    and if so, ensures externalStoreId is provided.
    
    Args:
        request: The request object to validate
    
    Raises:
        ApiException: If validation fails
    """
    if request is None:
        return
    
    # Check if request has payOptionDetails
    if not hasattr(request, 'pay_option_details') or request.pay_option_details is None:
        return
    
    # Check if any payOption is NETWORK_PAY_PG_QRIS
    has_qris = False
    if isinstance(request.pay_option_details, list):
        for pay_option_detail in request.pay_option_details:
            if hasattr(pay_option_detail, 'pay_option') and pay_option_detail.pay_option == 'NETWORK_PAY_PG_QRIS':
                has_qris = True
                break
    
    # If QRIS is found, externalStoreId must be provided
    if has_qris:
        external_store_id = None
        if hasattr(request, 'external_store_id'):
            external_store_id = request.external_store_id
        
        if not external_store_id or (isinstance(external_store_id, str) and external_store_id.strip() == ''):
            raise ApiException(
                status=0,
                reason='externalStoreId is required when payOption is NETWORK_PAY_PG_QRIS'
            )


# Validation registry maps request class names to their validation functions
validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'CreateOrderByApiRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
    ],
    'CreateOrderByRedirectRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
    ],
    'CreateOrderRequest': [
        validate_additional_info_required,
        validate_money_value_pattern,
        validate_valid_up_to_create_order_request,
        validate_external_store_id_for_qris,
    ],
    # Add more request types and their validations here as needed
}


def custom_validation(request: Any) -> None:
    """
    Perform custom validations on the request based on its type.
    
    This function checks the request type and runs the appropriate validations from the registry.
    
    Args:
        request: The request object to validate (can be any type)
    
    Raises:
        ApiException: If validation fails
    """
    if request is None:
        return
    
    # Get the class name of the request
    class_name = request.__class__.__name__
    
    # Check if this request type has validations registered
    if class_name in validation_registry:
        for validator in validation_registry[class_name]:
            validator(request)
