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

from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models import ConsultPayPaymentInfo, ConsultPayRequest, CreateOrderByApiRequest, QueryPaymentRequest
from dana.rest import ApiException
# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance
from tests.fixtures.payment_gateway import consult_pay_request, create_order_by_api_request, query_payment_request


class TestPaymentGatewayApi:
    
    def test_consult_pay_with_str_private_key_success(self, api_instance: PaymentGatewayApi, consult_pay_request: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response = api_instance.consult_pay(consult_pay_request)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'

        assert all(isinstance(i, ConsultPayPaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)

    def test_create_order_by_api_and_query_payment_success(self, api_instance: PaymentGatewayApi, create_order_by_api_request: CreateOrderByApiRequest, query_payment_request: QueryPaymentRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        api_response_create_order = api_instance.create_order(create_order_by_api_request)

        assert api_response_create_order.response_code == '2000000'
        assert api_response_create_order.response_message == 'Success'

        api_response_query_payment = api_instance.query_payment(query_payment_request)

        assert hasattr(api_response_query_payment, 'response_code')
        assert hasattr(api_response_query_payment, 'response_message')
