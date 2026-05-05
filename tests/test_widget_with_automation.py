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

import uuid
import pytest
import os
import tempfile
import time

from dana.widget.v1.api import WidgetApi
from dana.widget.v1.models import (
    ApplyTokenAuthorizationCodeRequest,
    ApplyTokenResponse,
    ApplyOTTRequest,
    ApplyOTTResponse,
    BalanceInquiryRequest,
    QueryPaymentRequest,
    RefundOrderRequest,
    AccountUnbindingRequest,
    ApplyOTTRequestAdditionalInfo,
    Oauth2UrlData,
    WidgetPaymentRequest,
)
from dana.widget.v1.util import Util

from tests.fixtures.api_client import api_instance_widget
from tests.fixtures.widget import (
    widget_payment_request, 
    widget_query_payment_request, 
    balance_inquiry_request,
    query_user_profile_request,
    widget_refund_order_request, 
    account_unbinding_request
)
from tests.automate_oauth import get_auth_code


class TestWidgetWithAutomation:
    """Test class for Widget API endpoints with browser automation"""

    binding_access_token = None
    ott = None
    
    def test_complete_process(self, api_instance_widget: WidgetApi, widget_payment_request: WidgetPaymentRequest, widget_query_payment_request: QueryPaymentRequest, widget_refund_order_request: RefundOrderRequest):
        """Test Binding Flow - OAuth, ApplyToken, ApplyOTT, Payment, Query, Refund, Unbind
        
        This test runs the complete binding flow from OAuth to ApplyToken to ApplyOTT
        """
        merchant_id = os.getenv('MERCHANT_ID')
        private_key = os.getenv('PRIVATE_KEY')
        
        # Step 1: Generate OAuth URL
        oauth2_url_data = Oauth2UrlData(
            redirect_url='https://google.com',
            merchant_id=merchant_id,
            seamless_data={
                'mobileNumber': '083811223355'
            },
            external_id=str(uuid.uuid4())
        )
        
        oauth_url = Util.generate_oauth_url(
            data=oauth2_url_data,
            private_key=private_key
        )
        
        print(f'Generated OAuth URL for binding flow: {oauth_url}')
        assert oauth_url is not None and len(oauth_url) > 0, 'OAuth URL should not be empty'
        
        # Required parameters validation
        from urllib.parse import urlparse, parse_qs
        url_parts = urlparse(oauth_url)
        url_params = parse_qs(url_parts.query)
        
        assert url_params.get('partnerId', [''])[0] == os.getenv('X_PARTNER_ID'), 'Partner ID should match'
        assert url_params.get('merchantId', [''])[0] == merchant_id, 'Merchant ID should match'
        assert 'channelId' in url_params, 'Should have channelId'
        assert 'timestamp' in url_params, 'Should have timestamp'
        assert 'state' in url_params, 'Should have state'
        assert url_params.get('isSnapBI', [''])[0] == 'true', 'isSnapBI should be true'
        
        # Step 2: Execute automate_oauth script to get auth code
        print('Executing automation script to get auth code...')
        
        temp_output_file = os.path.join(tempfile.gettempdir(), 'auth_code_output.txt')
        generated_auth_code = None
        
        try:
            # Use get_auth_code to automate the OAuth process
            print('Starting OAuth automation process...')
            generated_auth_code = get_auth_code(
                oauth_url=oauth_url,
                phone_number='083811223355',  # Optional: override phone number if needed
                pin='181818'
            )
            
            if generated_auth_code:
                print('OAuth automation completed successfully!')
            else:
                print('OAuth automation did not return an auth code')
                
                # Try to read from output file if it exists
                if os.path.exists(temp_output_file):
                    with open(temp_output_file, 'r') as f:
                        generated_auth_code = f.read().strip()
                    os.unlink(temp_output_file)  # Clean up temporary file
                    
                    if generated_auth_code:
                        print('Auth code retrieved from output file')
        except Exception as e:
            pytest.fail(f'Error running automated OAuth process: {e}')
        
        # Verify we got an auth code
        assert generated_auth_code is not None, 'Auth code should not be null'
        assert len(generated_auth_code) > 0, 'Auth code should not be empty'
        print(f'Auth code obtained: {generated_auth_code}')
        
        # Step 3: Apply Token using auth code
        apply_token_request = ApplyTokenAuthorizationCodeRequest(
            grant_type="AUTHORIZATION_CODE",
            auth_code=generated_auth_code
        )
        
        print('Applying token with auth code...')
        try:
            token_response = api_instance_widget.apply_token(apply_token_request)
            
            # Extract access token and store it for later tests
            self.__class__.binding_access_token = token_response.access_token
            print(f'Successfully applied token, got access token: {self.__class__.binding_access_token}')
            
            # Token validation
            assert token_response is not None, 'Token response should not be null'
            assert token_response.response_code is not None, 'Response code should not be null'
            assert token_response.response_code == '2007400', 'Response code should be 2007400'
            assert token_response.response_message is not None, 'Response message should not be null'
            assert token_response.response_message == 'Successful', 'Response message should be Successful'
            assert token_response.token_type is not None, 'Token type should not be null'
            assert token_response.access_token is not None, 'Access token should not be null'
            assert token_response.access_token_expiry_time is not None, 'Access token expiry time should not be null'
            assert token_response.refresh_token is not None, 'Refresh token should not be null'
            assert token_response.refresh_token_expiry_time is not None, 'Refresh token expiry time should not be null'
            
            # Step 4: Apply OTT using access token
            additional_info = ApplyOTTRequestAdditionalInfo(
                access_token=self.__class__.binding_access_token,
                device_id="BINDING_DEVICE_ID"
            )
            
            apply_ott_request = ApplyOTTRequest(
                additional_info=additional_info,
                user_resources=["OTT"]
            )
            
            print('Applying for OTT using access token...')
            ott_response = api_instance_widget.apply_ott(apply_ott_request)
            
            print(f'OTT response: {ott_response}')
            
            # OTT validation
            assert ott_response is not None, 'OTT response should not be null'
            assert ott_response.response_code is not None, 'Response code should not be null'
            assert ott_response.response_code == '2004900', 'Response code should be 2004900'
            assert ott_response.response_message is not None, 'Response message should not be null'
            assert ott_response.response_message == 'Successful', 'Response message should be Successful'
            assert ott_response.user_resources is not None, 'User resources should not be null'
            assert len(ott_response.user_resources) > 0, 'User resources should have at least one item'
            assert ott_response.user_resources[0].value is not None, 'OTT value should not be null'
            
            self.__class__.ott = ott_response.user_resources[0].value
            
            print('Binding flow completed successfully!')
        except Exception as e:
            pytest.fail(f'API call for apply OTT failed: {e}')

        # Doing balance inquiry
        try:
            # Use the fixture as a function with the required parameters
            balance_inquiry_req = balance_inquiry_request(token_response.access_token)
            
            balance_inquiry_resp = api_instance_widget.balance_inquiry(balance_inquiry_req)
            assert balance_inquiry_resp is not None
            assert balance_inquiry_resp.response_code == '2001100'
        except Exception as e:
            pytest.fail(f'API call for balance inquiry failed: {e}')

        # Widget Payment with automation
        try:
            payment_response = api_instance_widget.widget_payment(widget_payment_request)
            assert payment_response is not None
            
            assert payment_response.response_code == '2005400'
            assert payment_response.response_message == 'Successful'
            assert payment_response.partner_reference_no == widget_payment_request.partner_reference_no
            assert payment_response.web_redirect_url is not None
            assert len(payment_response.web_redirect_url) > 0
        except Exception as e:
            pytest.fail(f'Error during WidgetPayment execution: {e}')

        # Construct full payment URL with OTT and automate payment.
        # OTTs are short-lived, so we re-apply OTT on each attempt to avoid
        # "OTT not valid" errors caused by the time taken by prior test steps.
        from tests.web_automation import automate_payment_widget
        max_payment_retries = 3
        payment_success = False
        for payment_attempt in range(1, max_payment_retries + 1):
            try:
                print(f'Applying fresh OTT for payment attempt {payment_attempt}...')
                fresh_ott_response = api_instance_widget.apply_ott(apply_ott_request)
                assert fresh_ott_response.response_code == '2004900', \
                    f'OTT failed: {fresh_ott_response.response_code}'
                self.__class__.ott = fresh_ott_response.user_resources[0].value

                payment_url = Util.generate_complete_payment_url(
                    widget_payment_response=payment_response,
                    apply_ott_response=fresh_ott_response
                )
                print(f"Payment URL (attempt {payment_attempt}): {payment_url}")

                print("Running payment automation script...")
                success = automate_payment_widget(payment_url)
                if success:
                    payment_success = True
                    break
                print(f"Payment automation returned False on attempt {payment_attempt}")
            except Exception as e:
                print(f"Payment attempt {payment_attempt} error: {e}")
            if payment_attempt < max_payment_retries:
                print(f"Retrying payment in 3 seconds...")
                time.sleep(3)
        assert payment_success, f"Payment automation failed after {max_payment_retries} attempts"

        time.sleep(5)

        try:
            # Query Payment Status
            print("Querying payment status...")
            query_response = api_instance_widget.query_payment(widget_query_payment_request)
            
            assert query_response is not None
            assert query_response.response_code == '2005500'
            assert query_response.response_message == 'Successful'
            assert query_response.original_partner_reference_no == widget_payment_request.partner_reference_no
            assert query_response.transaction_status_desc == 'SUCCESS'
        except Exception as e:
            pytest.fail(f'Error during QueryPayment execution: {e}')

        # try:
        #     # Refund Order
        #     print("Refunding the order...")
        #     refund_response = api_instance_widget.refund_order(widget_refund_order_request)
            
        #     assert refund_response is not None
        #     assert refund_response.response_code == '2005800'
        #     assert refund_response.response_message == 'Successful'
        #     assert refund_response.original_partner_reference_no == widget_payment_request.partner_reference_no
        # except Exception as e:
        #     pytest.fail(f'Error during RefundOrder execution: {e}')

        try:
            # Query User Profile
            print("Querying user profile...")
            query_user_profile_req = query_user_profile_request(self.__class__.binding_access_token)
            query_user_profile_response = api_instance_widget.query_user_profile(query_user_profile_req)
            
            assert query_user_profile_response is not None
            assert query_user_profile_response.response is not None
            assert query_user_profile_response.response.head is not None
            assert query_user_profile_response.response.body is not None
            
            # Verify result status is success
            result_info = query_user_profile_response.response.body.result_info
            assert result_info is not None
            assert result_info.result_status == 'S', 'Result status should be Success (S)'
            
            # Verify that we requested BALANCE resource
            assert 'BALANCE' in query_user_profile_req.user_resources
            assert query_user_profile_req.access_token == self.__class__.binding_access_token
            
            print("Successfully retrieved user profile with BALANCE resource")
            print(f"Result Status: {result_info.result_status}")
            print(f"Result Code: {result_info.result_code}")
            print(f"Access Token used: {self.__class__.binding_access_token}")
            
            # Check if user resources were returned
            user_resource_infos = query_user_profile_response.response.body.user_resource_infos
            if user_resource_infos and len(user_resource_infos) > 0:
                print(f"Returned {len(user_resource_infos)} user resource(s)")
        except Exception as e:
            pytest.fail(f'Error during QueryUserProfile execution: {e}')

        try:
            # Account Unbinding
            print("Unbinding the account...")
            unbinding_request = account_unbinding_request(self.__class__.binding_access_token)
            unbinding_response = api_instance_widget.account_unbinding(unbinding_request)
            
            assert unbinding_response is not None
            assert unbinding_response.response_code == '2000900'
            assert unbinding_response.response_message == 'Successful'
            
            print("Complete widget payment flow executed successfully!")
        except Exception as e:
            pytest.fail(f'Error during AccountUnbinding execution: {e}')