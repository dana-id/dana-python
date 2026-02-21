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

from typing import Any, Dict, List, Callable
from dana.utils.date_validation import validate_valid_up_to_date
from dana.exceptions import ApiException


def validate_valid_up_to_widget_payment_request(request: Any) -> None:
    """
    Validate validUpTo field in WidgetPaymentRequest.
    
    Args:
        request: The request object to validate
    
    Raises:
        ApiException: If validation fails
    """
    if request is None:
        return
    
    if hasattr(request, 'valid_up_to') and request.valid_up_to is not None:
        try:
            validate_valid_up_to_date(request.valid_up_to)
        except ValueError as e:
            raise ApiException(
                status=0,
                reason=f'validUpTo validation failed: {str(e)}'
            ) from e


# Validation registry maps request class names to their validation functions
validation_registry: Dict[str, List[Callable[[Any], None]]] = {
    'WidgetPaymentRequest': [
        validate_valid_up_to_widget_payment_request,
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
