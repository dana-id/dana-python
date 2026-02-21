# Copyright 2025 PT Espay Debit Indonesia Koe
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
import json
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models import ConsultPayPaymentInfo, ConsultPayRequest, CreateOrderByApiRequest, CreateOrderByRedirectRequest, QueryPaymentRequest, CancelOrderRequest, RefundOrderRequest, Money, PayOptionDetail
from dana.webhook.finish_notify_request import FinishNotifyRequest
from dana.rest import ApiException
from dana.webhook import WebhookParser
from dana.utils.snap_header import SnapHeader
# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance_payment_gateway, api_instance_payment_gateway_with_key_path
from tests.fixtures.payment_gateway import consult_pay_request, consult_pay_request_without_buyer, consult_pay_request_with_external_store_id, create_order_by_api_request, query_payment_request, cancel_order_request, refund_order_request, webhook_key_pair



class TestPaymentGatewayApi:
    
    def test_consult_pay_with_str_private_key_success(self, api_instance_payment_gateway: PaymentGatewayApi, consult_pay_request: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response = api_instance_payment_gateway.consult_pay(consult_pay_request)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'

        assert all(isinstance(i, ConsultPayPaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)

    def test_consult_pay_without_buyer(self, api_instance_payment_gateway: PaymentGatewayApi, consult_pay_request_without_buyer: ConsultPayRequest):
        """Should give error response code and message and correct mandatory fields"""
        
        api_response = api_instance_payment_gateway.consult_pay(consult_pay_request_without_buyer)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'

        assert all(isinstance(i, ConsultPayPaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)

    def test_consult_pay_with_external_store_id(self, api_instance_payment_gateway: PaymentGatewayApi, consult_pay_request_with_external_store_id: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response = api_instance_payment_gateway.consult_pay(consult_pay_request_with_external_store_id)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'
        
        assert all(isinstance(i, ConsultPayPaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)

    def test_create_order_by_api_and_query_payment_success(self, api_instance_payment_gateway: PaymentGatewayApi, create_order_by_api_request: CreateOrderByApiRequest, query_payment_request: QueryPaymentRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response_create_order = api_instance_payment_gateway.create_order(create_order_by_api_request)

        assert api_response_create_order.response_code == '2005400'
        assert api_response_create_order.response_message == 'Successful'

        api_response_query_payment = api_instance_payment_gateway.query_payment(query_payment_request)

        assert hasattr(api_response_query_payment, 'response_code')
        assert hasattr(api_response_query_payment, 'response_message')
        
    def test_create_order_with_private_key_path(self, api_instance_payment_gateway_with_key_path: PaymentGatewayApi, create_order_by_api_request: CreateOrderByApiRequest):
        """Should successfully create an order using private key file path instead of key string"""
        api_response = api_instance_payment_gateway_with_key_path.create_order(create_order_by_api_request)
        
        assert api_response.response_code == '2005400'
        assert api_response.response_message == 'Successful'

    def test_cancel_order_success(self, api_instance_payment_gateway: PaymentGatewayApi, create_order_by_api_request: CreateOrderByApiRequest, cancel_order_request: CancelOrderRequest):
        """Should successfully cancel an order and return success response code"""
        
        # First create an order
        api_response_create_order = api_instance_payment_gateway.create_order(create_order_by_api_request)
        assert api_response_create_order.response_code == '2005400'
        
        # Then cancel the order
        api_response_cancel = api_instance_payment_gateway.cancel_order(cancel_order_request)
        
        # Assert successful cancellation
        assert api_response_cancel.response_code == '2005700'
        assert api_response_cancel.response_message == 'Success'
        assert api_response_cancel.original_partner_reference_no == cancel_order_request.original_partner_reference_no
    
    def test_create_order_with_valid_up_to_outside_range_setter(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should reject an order with valid_up_to more than 30 minutes in the future (setter validation)"""
        
        # Import required modules
        from datetime import datetime, timedelta, timezone
        import pytest
        import os
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        
        # Only run this test in sandbox environment
        env = os.getenv("DANA_ENV", os.getenv("ENV", "sandbox")).lower()
        if env != "sandbox":
            pytest.skip("Skipping test: validUpTo validation only runs in sandbox environment")
        
        # Get a base request from the fixtures
        base_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        
        # Set valid_up_to to 31 minutes in the future (outside of allowed 30-minute range)
        jakarta_tz = timezone(timedelta(hours=7))
        beyond_30_minutes = (datetime.now(jakarta_tz) + timedelta(minutes=31)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
        
        # Try to set the invalid date - should trigger field validator
        with pytest.raises(ValueError) as excinfo:
            # Setting the value should trigger the @field_validator
            base_request.valid_up_to = beyond_30_minutes
            
        # Check the error message contains expected text about the date range
        error_msg = str(excinfo.value)
        assert "minutes" in error_msg.lower(), \
            f"Error message should mention 'minutes'. Got: {error_msg}"
        print(f"Setter validation error as expected: {error_msg}")

    def test_create_order_with_valid_up_to_outside_range_custom(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should reject an order with valid_up_to more than 30 minutes in the future (custom validation)"""
        
        # Import required modules
        from datetime import datetime, timedelta, timezone
        import pytest
        import os
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        from dana.rest import ApiException
        
        # Only run this test in sandbox environment
        env = os.getenv("DANA_ENV", os.getenv("ENV", "sandbox")).lower()
        if env != "sandbox":
            pytest.skip("Skipping test: validUpTo validation only runs in sandbox environment")
        
        # Get a fixture that directly sets ValidUpTo to 31 minutes (bypassing setter)
        # This tests that custom_validation() in Execute() catches invalid dates
        create_order_by_api_request = PaymentGatewayFixtures.get_create_order_by_api_with_beyond_30_minutes()
        
        # Attempt to execute the request - should fail validation in custom_validation()
        with pytest.raises(ApiException) as excinfo:
            api_instance_payment_gateway.create_order(create_order_by_api_request)
        
        # Assert that there was an error from custom_validation()
        error_msg = str(excinfo.value)
        assert "validUpTo" in error_msg.lower() or "minutes" in error_msg.lower(), \
            f"Error message must mention 'validUpTo' or 'minutes', got: {error_msg}"
        print(f"CustomValidation() error as expected: {error_msg}")

    def test_create_order_by_api_missing_additional_info_client_validation(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should reject CreateOrderByApiRequest without additional_info (client-side)"""
        import pytest
        from dana.exceptions import ApiException
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures

        request = PaymentGatewayFixtures.get_create_order_by_api_request()
        request.additional_info = None

        with pytest.raises(ApiException) as excinfo:
            api_instance_payment_gateway.create_order(request)

        assert "additionalinfo" in str(excinfo.value).lower()

    def test_create_order_by_redirect_missing_additional_info_client_validation(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should reject CreateOrderByRedirectRequest without additional_info (client-side)"""
        import pytest
        from dana.exceptions import ApiException
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures

        request = PaymentGatewayFixtures.get_create_order_by_redirect_request()
        request.additional_info = None

        with pytest.raises(ApiException) as excinfo:
            api_instance_payment_gateway.create_order(request)

        assert "additionalinfo" in str(excinfo.value).lower()

    def test_create_order_with_debug_mode(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should test debug mode functionality"""
        from dana.exceptions import ApiException
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        import pytest
        
        # Get base request from fixtures
        base_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        base_request.external_store_id = 'test_debug_mode'
        
        # This should fail and return debug information
        with pytest.raises(ApiException) as excinfo:
            api_instance_payment_gateway.create_order(base_request)
        
        # Check if debug message is present in the error
        error_msg = str(excinfo.value)
        assert 'debugMessage' in error_msg

    def test_qris_external_store_id_required(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Test that externalStoreId is required when payOption is NETWORK_PAY_PG_QRIS"""
        from dana.exceptions import ApiException
        from dana.payment_gateway.v1.models import CreateOrderByApiRequest, PayOptionDetail, Money
        from dana.payment_gateway.v1.enum import PayMethod, PayOption
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        import pytest
        
        # Create a request with QRIS payOption but without externalStoreId
        create_order_by_api_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        
        # Set payOption to QRIS
        pay_option_detail = PayOptionDetail(
            pay_method=PayMethod.NETWORK_PAY,
            pay_option=PayOption.NETWORK_PAY_PG_QRIS,
            trans_amount=Money(value="222000.00", currency="IDR")
        )
        create_order_by_api_request.pay_option_details = [pay_option_detail]
        
        # Do NOT set external_store_id - should fail validation
        
        # Attempt to execute the request - should fail validation in custom_validation()
        with pytest.raises(ApiException) as excinfo:
            api_instance_payment_gateway.create_order(create_order_by_api_request)
        
        # Assert that there was an error from custom_validation()
        error_msg = str(excinfo.value).lower()
        assert "externalstoreid" in error_msg or "external_store_id" in error_msg or "qris" in error_msg, \
            f"Error message must mention 'externalStoreId' or 'QRIS', got: {error_msg}"

    def test_qris_external_store_id_provided(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Test that when externalStoreId is provided with QRIS, validation passes"""
        from dana.exceptions import ApiException
        from dana.payment_gateway.v1.models import CreateOrderByApiRequest, PayOptionDetail, Money
        from dana.payment_gateway.v1.enum import PayMethod, PayOption
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        import pytest
        
        # Create a request with QRIS payOption and with externalStoreId
        create_order_by_api_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        
        # Set payOption to QRIS
        pay_option_detail = PayOptionDetail(
            pay_method=PayMethod.NETWORK_PAY,
            pay_option=PayOption.NETWORK_PAY_PG_QRIS,
            trans_amount=Money(value="222000.00", currency="IDR")
        )
        create_order_by_api_request.pay_option_details = [pay_option_detail]
        
        # Set external_store_id - should pass validation
        create_order_by_api_request.external_store_id = "test_shop"
        
        # Attempt to execute the request - should pass custom validation
        # (may still fail at API level, but not due to externalStoreId validation)
        try:
            api_instance_payment_gateway.create_order(create_order_by_api_request)
            # If we get here, validation passed (though API call may have failed for other reasons)
        except ApiException as e:
            # Check that the error is NOT about externalStoreId
            error_msg = str(e).lower()
            assert not ("externalstoreid" in error_msg and "required" in error_msg), \
                f"Error should not be about missing externalStoreId, got: {error_msg}"

    def test_money_amount_value_pattern_negative_cases(self):
        """Money amount value pattern - negative cases: e.g. .15, no decimals, wrong decimals."""
        import re
        pattern = re.compile(r"^\d{1,16}\.\d{2}$")
        invalid_values = [".15", "10000", "10000.0", "10000.123", ""]
        for value in invalid_values:
            assert not pattern.match(value), f"Value should not match amount pattern: {value}"

    def test_create_order_with_invalid_amount_value_dot15(self, api_instance_payment_gateway: PaymentGatewayApi):
        """CreateOrder with invalid amount value .15 should fail (pattern or API validation)."""
        import pytest
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures

        create_order_by_api_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        create_order_by_api_request.amount = Money(value=".15", currency="IDR")
        pay_option_detail = PayOptionDetail(
            pay_method="BALANCE",
            pay_option="",
            trans_amount=Money(value=".15", currency="IDR")
        )
        create_order_by_api_request.pay_option_details = [pay_option_detail]

        with pytest.raises((ApiException, ValueError, Exception)):
            api_instance_payment_gateway.create_order(create_order_by_api_request)
