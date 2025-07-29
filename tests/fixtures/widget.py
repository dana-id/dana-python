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

import os
import pytest
from datetime import datetime, timezone, timedelta
from dana.widget.v1.api import WidgetApi
from dana.widget.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest
from dana.widget.v1.models.apply_ott_request import ApplyOTTRequest
from dana.widget.v1.models.apply_ott_request_additional_info import ApplyOTTRequestAdditionalInfo
from dana.widget.v1.models.widget_payment_request import WidgetPaymentRequest, WidgetPaymentRequestAdditionalInfo
from dana.widget.v1.models.account_unbinding_request import AccountUnbindingRequest, AccountUnbindingRequestAdditionalInfo
from dana.widget.v1.models import Money, Order, EnvInfo
from dana.widget.v1.enum import SourcePlatform, TerminalType
from dana.widget.v1.models.apply_token_response import ApplyTokenResponse
# Import OAuth automation 
from tests.automate_oauth import get_auth_code


@pytest.fixture(scope="function")
def authorization_code():
    """Fixture to provide an OAuth authorization code."""
    auth_code = get_auth_code()
    return auth_code


@pytest.fixture(scope="function")
def apply_token_request(authorization_code: str):
    """Fixture to provide an ApplyToken request with authorization code."""
    if not authorization_code:
        pytest.skip("Authorization code not available")
    
    return ApplyTokenAuthorizationCodeRequest(
        grant_type="AUTHORIZATION_CODE", 
        auth_code=authorization_code,
        refresh_token=""
    )


@pytest.fixture(scope="function")
def apply_ott_request(api_instance_widget: WidgetApi, apply_token_request: ApplyTokenAuthorizationCodeRequest):
    """Fixture to provide an ApplyOTT request with access token."""
    # First get an access token
    token_response = None
    try:
        token_response: ApplyTokenResponse = api_instance_widget.apply_token(apply_token_request)
    except Exception as e:
        pytest.skip(f"Could not obtain access token: {e}")
    
    if not token_response or not hasattr(token_response, 'access_token'):
        pytest.skip("Access token not available in response")
    
    # Get merchant_id from environment
    merchant_id = os.getenv("MERCHANT_ID")
    if not merchant_id:
        pytest.skip("MERCHANT_ID environment variable not set")
    
    # Create additional info
    additional_info = ApplyOTTRequestAdditionalInfo(
        access_token=token_response.access_token,
        device_id="Mozilla / 5.0(Windows NT 10.0; Win64; x64)", 
        latitude="-6.108", 
        longitude="10.845", 
        end_user_ip_address="127.0.0.1"
    )
    
    # Create OTT request
    return ApplyOTTRequest(
        userResources=["OTT"],
        additional_info=additional_info
    )


@pytest.fixture(scope="function")
def widget_payment_request() -> WidgetPaymentRequest:
    """Fixture to provide an WidgetPaymentRequest."""

    merchant_id = os.getenv("MERCHANT_ID")
    if not merchant_id:
        pytest.skip("MERCHANT_ID environment variable not set")

    partner_reference_no = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    amount = Money(value="10000.00", currency="IDR")

    created_time = (datetime.now(timezone.utc) + timedelta(hours=7)).strftime("%Y-%m-%dT%H:%M:%S+07:00")

    order = Order(
        order_title="DANA Widget Test Order",
        created_time=created_time,
    )

    env_info = EnvInfo(
        source_platform=SourcePlatform.IPG,
        terminal_type=TerminalType.SYSTEM,
    )

    additional_info = WidgetPaymentRequestAdditionalInfo(
        product_code="51051000100000000001",
        order=order,
        mcc="5732",
        env_info=env_info,
    )

    return WidgetPaymentRequest(
        partner_reference_no=partner_reference_no,
        merchant_id=merchant_id,
        amount=amount,
        additional_info=additional_info,
    )


@pytest.fixture(scope="function")
def account_unbinding_request(api_instance_widget: WidgetApi, apply_token_request: ApplyTokenAuthorizationCodeRequest):
    """Fixture to provide AccountUnbindingRequest built from an access token."""
    # Obtain access token first
    token_response: ApplyTokenResponse = None
    try:
        token_response = api_instance_widget.apply_token(apply_token_request)
    except Exception as e:
        pytest.skip(f"Could not obtain access token: {e}")

    if not token_response or not hasattr(token_response, "access_token"):
        pytest.skip("Access token not available in response")

    merchant_id = os.getenv("MERCHANT_ID")
    if not merchant_id:
        pytest.skip("MERCHANT_ID environment variable not set")

    device_id = "Mozilla / 5.0(Windows NT 10.0; Win64; x64)"

    additional_info = AccountUnbindingRequestAdditionalInfo(
        access_token=token_response.access_token,
        device_id=device_id,
        latitude="-6.108",
        longitude="10.845",
        end_user_ip_address="127.0.0.1",
    )


    return AccountUnbindingRequest(
        merchant_id=merchant_id,
        additional_info=additional_info,
    )
