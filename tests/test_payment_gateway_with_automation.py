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
import time
import uuid
from datetime import datetime

from dana.payment_gateway.v1.api import PaymentGatewayApi
from dana.payment_gateway.v1.models import (
    ConsultPayRequest,
    CreateOrderByApiRequest,
    CreateOrderByRedirectRequest,
    QueryPaymentRequest,
    CancelOrderRequest,
    RefundOrderRequest,
    Money
)

from tests.fixtures.api_client import api_instance_payment_gateway
from tests.fixtures.payment_gateway import (
    consult_pay_request,
    create_order_by_api_request,
    create_order_by_api_paid_request,
    create_order_by_redirect_request,
    query_payment_request,
    cancel_order_request,
    refund_order_request
)
from tests.web_automation import automate_payment_payment_gateway


class TestPaymentGatewayWithAutomation:
    """Test class for Payment Gateway API endpoints with browser automation"""

    def test_complete_scenario(self, api_instance_payment_gateway: PaymentGatewayApi, create_order_by_redirect_request: CreateOrderByRedirectRequest):
        """Test RefundOrder operation with web automation
        
        This test does the following:
        1. Creates an order
        2. Automates payment via web redirect URL
        3. Queries payment status until success (with retries)
        4. Performs refund operation on the successful payment
        """
        # Skip test if no API client credentials are available
        merchant_id = os.getenv('MERCHANT_ID')
        if not merchant_id:
            pytest.skip("Skipping test: No API client credentials")
        
        try:
            # Execute the create order API call
            resp_create_order = api_instance_payment_gateway.create_order(create_order_by_redirect_request)
            
            # Assertions for create order response
            assert resp_create_order is not None
            assert resp_create_order.web_redirect_url is not None
            assert resp_create_order.partner_reference_no == create_order_by_redirect_request.partner_reference_no
            assert resp_create_order.reference_no is not None
            
            # Store the reference number for refund
            ref_no = resp_create_order.reference_no
            
            # Flag to track if payment automation was successful
            payment_succeeded = False
            
            # Allow some time for the order to be processed
            time.sleep(5)
            
            # Extract webRedirectUrl from the response
            web_redirect_url = resp_create_order.web_redirect_url
            if web_redirect_url:
                print(f"Found webRedirectUrl, launching automated payment process: {web_redirect_url}")
                
                # Run the payment automation
                payment_succeeded = automate_payment_payment_gateway(web_redirect_url)
                
                if not payment_succeeded:
                    print("Payment automation failed")
                else:
                    print("Payment automation completed successfully!")
            
            # Only proceed with query payment and refund if payment was successful
            if payment_succeeded:
                print("Payment automation successful. Proceeding with query payment...")
                
                # Get query payment request from fixtures
                query_request = QueryPaymentRequest(
                    original_partner_reference_no=create_order_by_redirect_request.partner_reference_no,
                    service_code="54",
                    merchant_id=merchant_id
                )
                
                # Try query payment up to 3 times until we get 'SUCCESS' status
                max_retries = 3
                query_succeeded = False
                resp_query_payment = None
                
                for i in range(max_retries):
                    print(f"Query payment attempt {i+1} of {max_retries}...")
                    
                    try:
                        resp_query_payment = api_instance_payment_gateway.query_payment(query_request)
                        
                        print(f"Query payment attempt {i+1} response: "
                              f"status={resp_query_payment.transaction_status_desc or 'unknown'}, "
                              f"code={resp_query_payment.response_code}")
                        
                        if resp_query_payment.transaction_status_desc == 'SUCCESS':
                            print("Query payment returned SUCCESS status")
                            query_succeeded = True
                            break
                    except Exception as e:
                        print(f"Query payment attempt {i+1} failed: {e}")
                    
                    if i < max_retries - 1:
                        print("Waiting 5 seconds before retrying query...")
                        time.sleep(5)
                
                # Log the query results
                if query_succeeded:
                    print(f"Final query payment status: {resp_query_payment.transaction_status_desc}")
                    
                    # Check if Amount and its fields exist before accessing
                    if (hasattr(resp_query_payment, 'amount') and
                            resp_query_payment.amount and
                            hasattr(resp_query_payment.amount, 'value') and
                            hasattr(resp_query_payment.amount, 'currency')):
                        print(f"Payment details: Amount={resp_query_payment.amount.value} "
                              f"{resp_query_payment.amount.currency}")
                else:
                    pytest.fail("All query payment attempts failed or did not return SUCCESS status. Continuing with refund anyway.")
                
                print("Proceeding with refund order request...")
                
                # Create refund order request
                refund_request = RefundOrderRequest(
                    original_partner_reference_no=create_order_by_redirect_request.partner_reference_no,
                    merchant_id=merchant_id,
                    partner_refund_no=str(uuid.uuid4()),
                    refund_amount=Money(
                        value=create_order_by_redirect_request.amount.value,
                        currency=create_order_by_redirect_request.amount.currency
                    ),
                    reason="Python SDK Automation Test Refund"
                )
                
                # Execute the refund order API call
                try:
                    resp_refund_order = api_instance_payment_gateway.refund_order(refund_request)
                    
                    # Add assertions for successful refund response
                    assert resp_refund_order is not None
                    
                    assert resp_refund_order.response_code is not None
                    
                    if resp_refund_order.response_code:
                        assert resp_refund_order.response_code in ['2005800', '2001400'], "Unexpected response code"
                    
                    print(f"Refund response: {resp_refund_order}")
                except Exception as e:
                    error_str = str(e)
                    print(f"Refund order request error: {error_str}")
                    
                    # If we get a 404 with "Invalid Transaction Status", that's expected in test environment
                    if "Invalid Transaction Status" in error_str:
                        print("Received expected 'Invalid Transaction Status' error")
                    else:
                        pytest.fail(f"Refund request failed with unexpected error: {e}")
            else:
                pytest.fail("Payment automation was not successful")
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
