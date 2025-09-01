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

import pytest
import os

from dana.widget.v1.api import WidgetApi
from dana.widget.v1.models import (
    ApplyOTTRequest,
    QueryPaymentRequest,
    CancelOrderRequest,
    BalanceInquiryRequest,
)

from tests.fixtures.api_client import api_instance_widget
from tests.fixtures.widget import widget_payment_request, apply_token_request, widget_cancel_order_request

class TestWidgetApi:
    """Test class for Widget API endpoints without automation"""
    
    def test_create_payment_and_query(self, api_instance_widget: WidgetApi, widget_payment_request):
        """Test Payment and Query flow
        
        This test creates a widget payment and then queries its status
        """
        # Step 1: Create Widget Payment
        print("Step 1: Creating widget payment...")
        try:
            widget_payment_response = api_instance_widget.widget_payment(widget_payment_request)
            assert widget_payment_response is not None
            assert widget_payment_response.web_redirect_url is not None
            assert len(widget_payment_response.web_redirect_url) > 0
            
            # Step 2: Query Payment - create query request directly to avoid fixture issues
            print("Step 2: Querying payment status...")
            query_payment_request = QueryPaymentRequest(
                service_code="54",
                merchant_id=os.environ.get('MERCHANT_ID', '216620010016033632482'),
                original_partner_reference_no=widget_payment_request.partner_reference_no,
                original_reference_no=widget_payment_response.reference_no if hasattr(widget_payment_response, 'reference_no') else None
            )
            query_payment_response = api_instance_widget.query_payment(query_payment_request)
            
            assert query_payment_response is not None
            assert query_payment_response.response_code == "2005500"
            assert query_payment_response.response_message == "Successful"
            assert query_payment_response.original_partner_reference_no == widget_payment_request.partner_reference_no
        
        except Exception as e:
            pytest.fail(f"Error during Widget Payment or Query execution: {e}")
    
    def test_widget_cancel_order(self, api_instance_widget: WidgetApi, widget_payment_request):
        """Test Widget Cancel Order flow
        
        This test creates a widget payment and then cancels it
        """
        print("Testing widget cancel order...")
        
        try:
            # Create a payment first
            widget_payment_response = api_instance_widget.widget_payment(widget_payment_request)
            assert widget_payment_response is not None
            
            # Create cancel request directly
            merchant_id = os.environ.get('DANA_MERCHANT_ID', '216620000000147517713')
            if hasattr(widget_payment_request, 'merchant_id') and widget_payment_request.merchant_id is not None:
                merchant_id = widget_payment_request.merchant_id
                
            cancel_order_request = CancelOrderRequest(
                original_partner_reference_no=widget_payment_request.partner_reference_no,
                merchant_id=merchant_id,
                reason="User cancelled order"
            )
            
            # Test CancelOrder
            cancel_order_response = api_instance_widget.cancel_order(cancel_order_request)
            
            assert cancel_order_response is not None
            assert cancel_order_response.original_partner_reference_no == widget_payment_request.partner_reference_no
        
        except Exception as e:
            pytest.fail(f"Error during CancelOrder execution: {e}")
