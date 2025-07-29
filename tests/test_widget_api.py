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

from dana.widget.v1.api import WidgetApi
from dana.widget.v1.models import (
    ApplyOTTRequest,
    QueryPaymentRequest,
    CancelOrderRequest,
)

from tests.fixtures.api_client import api_instance_widget
from tests.fixtures.widget import authorization_code, apply_token_request, apply_ott_request, widget_payment_request, account_unbinding_request

class TestWidgetApi:
    """Test class for Widget API endpoints"""
    
    def test_apply_token_and_apply_ott_success(self, api_instance_widget: WidgetApi, apply_ott_request: ApplyOTTRequest):
        """Should successfully apply for a one-time token (OTT) and return it in the response"""
        
        # Call apply OTT API
        api_response = api_instance_widget.apply_ott(
            apply_ott_request=apply_ott_request,
        )
        assert api_response is not None
        assert api_response.response_code == "2004900"
        assert api_response.response_message == "Successful"
        
        # Find OTT in user resources
        ott_token = None
        if api_response.user_resources:
            for resource in api_response.user_resources:
                if hasattr(resource, 'resource_type') and resource.resource_type == "OTT":
                    ott_token = resource.value
                    break
        
        assert ott_token is not None, "OTT token not found in response"

    def test_widget_create_query_cancel_success(self, api_instance_widget: WidgetApi, widget_payment_request):
        """End-to-end test: create order (WidgetPayment), query it, and then cancel it"""
        
        # Fixture already provides fully-formed request
        merchant_id = widget_payment_request.merchant_id
        partner_reference_no = widget_payment_request.partner_reference_no
        amount = widget_payment_request.amount

        # --- Call WidgetPayment -------------------------------------
        payment_response = api_instance_widget.widget_payment(widget_payment_request=widget_payment_request)
        assert payment_response is not None
        assert payment_response.response_code == "2005400"
        assert payment_response.partner_reference_no == partner_reference_no
        assert payment_response.web_redirect_url is not None

        # --- Call QueryPayment -----------------------------------
        query_request = QueryPaymentRequest(
            service_code="54",
            merchant_id=merchant_id,
            original_partner_reference_no=partner_reference_no,
            original_reference_no=payment_response.reference_no,
            amount=amount,
        )
        query_response = api_instance_widget.query_payment(query_payment_request=query_request)
        assert query_response is not None
        assert query_response.response_code == "2005500"
        
        # --- Call CancelOrder ------------------------------------
        cancel_request = CancelOrderRequest(
            original_partner_reference_no=partner_reference_no,
            merchant_id=merchant_id,
            reason="User cancelled order",
            amount=amount,
        )
        cancel_response = api_instance_widget.cancel_order(cancel_order_request=cancel_request)
        assert cancel_response is not None
        assert cancel_response.response_code == "2005700"
        assert cancel_response.original_partner_reference_no == partner_reference_no

    def test_account_unbinding_success(self, api_instance_widget: WidgetApi, account_unbinding_request):
        """Should unbind an account successfully after obtaining access token."""

        response = api_instance_widget.account_unbinding(
            account_unbinding_request=account_unbinding_request,
        )

        assert response is not None
        assert response.response_code == "2000900"
        assert response.response_message == "Successful"



