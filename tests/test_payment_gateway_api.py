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
from dana.payment_gateway.v1.models import ConsultPayPaymentInfo, ConsultPayRequest, CreateOrderByApiRequest, QueryPaymentRequest, CancelOrderRequest, RefundOrderRequest
from dana.rest import ApiException
# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance_payment_gateway
from tests.fixtures.payment_gateway import consult_pay_request, create_order_by_api_request, query_payment_request, cancel_order_request, refund_order_request


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

    # def test_refund_order_success(self, api_instance: PaymentGatewayApi, create_order_by_api_request: CreateOrderByApiRequest, query_payment_request: QueryPaymentRequest):
    #     """Should successfully refund an order"""
        
    #     # First create an order
    #     create_response = api_instance.create_order(create_order_by_api_request)
    #     assert create_response.response_code == '2000000'
    #     print(f"Order created successfully with response code: {create_response.response_code}")

    #     # Query the payment status first with special parameters
    #     from dana.payment_gateway.v1.models.query_payment_request import QueryPaymentRequest
    #     from dana.payment_gateway.v1.models.refund_order_request import RefundOrderRequest
    #     from dana.payment_gateway.v1.models.refund_order_request_additional_info import RefundOrderRequestAdditionalInfo
    #     from dana.payment_gateway.v1.models.money import Money
    #     import datetime

    #     special_query_request = QueryPaymentRequest(
    #         original_partner_reference_no="20250303145313698344",
    #         original_reference_no=None,
    #         service_code="00",  # Special service code for refund preparation
    #         merchant_id="216620020005034264607"
    #     )
        
    #     try:
    #         # Query the payment to prepare for refund
    #         query_response = api_instance.query_payment(special_query_request)
    #         print(f"Query payment response: {query_response}")
            
    #         # Check if query was successful
    #         assert query_response.response_code in ['2005500', '2005700'], f"Query payment failed with code: {query_response.response_code}"
    #         print("Special query payment preparation successful")
    #     except Exception as e:
    #         print(f"Query payment error: {e}")
    #         # If query fails, we can't proceed with the test
    #         raise
        
    #     # Construct RefundOrderRequest using data from query_response
    #     partner_refund_no = f"REFUND-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    #     live_refund_order_request = RefundOrderRequest(
    #         original_partner_reference_no=query_response.original_partner_reference_no,
    #         original_reference_no=query_response.original_reference_no,
    #         merchant_id=special_query_request.merchant_id,  # or query_response.merchant_id if available and preferred
    #         partner_refund_no=partner_refund_no,
    #         refund_amount=Money(
    #             value="0.00",
    #             currency=query_response.trans_amount.currency
    #         ),
    #         reason="Test refund from live query data",
    #     )

    #     # Attempt to refund the order and expect a successful response
    #     refund_response = api_instance.refund_order(live_refund_order_request)
    #     print(f"Refund API call executed. Response code: {refund_response.response_code}, Message: {refund_response.response_message}")

    #     # Assert that the refund was truly successful
    #     # According to the MEMORY, service code 58 (Refund) should result in responseCode 2005800 for success.
    #     # Let's use that or allow 2005700 if that was a previously observed success code for similar operations.
    #     assert refund_response.response_code in ['2005800', '2005700'], \
    #         f"Refund failed. Expected response code 2005800 or 2005700, but got {refund_response.response_code}. Message: {refund_response.response_message}"
        
    #     assert refund_response.response_message == 'Successful', \
    #         f"Refund failed. Expected response message 'Successful', but got '{refund_response.response_message}'"

    #     # Add more specific assertions if the 'result' object is populated on success
    #     if hasattr(refund_response, 'result') and refund_response.result is not None:
    #         assert refund_response.result.merchant_id == live_refund_order_request.merchant_id, "Merchant ID mismatch in refund result"
    #         assert refund_response.result.partner_refund_no == live_refund_order_request.partner_refund_no, "Partner refund number mismatch in refund result"
        
    #     print("Refund test passed with a successful API response.")
