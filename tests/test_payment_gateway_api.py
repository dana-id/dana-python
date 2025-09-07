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
from dana.payment_gateway.v1.models import ConsultPayPaymentInfo, ConsultPayRequest, CreateOrderByApiRequest, QueryPaymentRequest, CancelOrderRequest, RefundOrderRequest
from dana.webhook.finish_notify_request import FinishNotifyRequest
from dana.rest import ApiException
from dana.webhook import WebhookParser
from dana.utils.snap_header import SnapHeader
# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance_payment_gateway, api_instance_payment_gateway_with_key_path
from tests.fixtures.payment_gateway import consult_pay_request, create_order_by_api_request, query_payment_request, cancel_order_request, refund_order_request, webhook_key_pair



class TestPaymentGatewayApi:
    
    def test_consult_pay_with_str_private_key_success(self, api_instance_payment_gateway: PaymentGatewayApi, consult_pay_request: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response = api_instance_payment_gateway.consult_pay(consult_pay_request)

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
    
    def test_create_order_with_valid_up_to_outside_range(self, api_instance_payment_gateway: PaymentGatewayApi):
        """Should reject an order with valid_up_to more than one week in the future"""
        
        # Import required modules
        from datetime import datetime, timedelta, timezone
        import pytest
        import json
        from tests.fixtures.payment_gateway import PaymentGatewayFixtures
        
        # Get a base request from the fixtures
        base_request = PaymentGatewayFixtures.get_create_order_by_api_request()
        
        # Set valid_up_to to 8 days in the future (outside of allowed range)
        jakarta_tz = timezone(timedelta(hours=7))
        beyond_one_week = (datetime.now(jakarta_tz) + timedelta(days=8)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
        
        # Try to create an order with this invalid date
        # The API should reject it with a specific error code
        with pytest.raises(ValueError) as excinfo:
            # Create a modified request with the invalid valid_up_to date
            base_request.valid_up_to = beyond_one_week
            
        # Check the error message contains expected text about the date range
        error_msg = str(excinfo.value)
        assert "week" in error_msg.lower() or "future" in error_msg.lower()

