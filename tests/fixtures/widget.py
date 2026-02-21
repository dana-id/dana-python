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
import uuid
import pytest
from datetime import datetime, timezone, timedelta
from dana.widget.v1.api import WidgetApi
from dana.widget.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest
from dana.widget.v1.models.apply_ott_request import ApplyOTTRequest
from dana.widget.v1.models.apply_ott_request_additional_info import ApplyOTTRequestAdditionalInfo
from dana.widget.v1.models.widget_payment_request import WidgetPaymentRequest, WidgetPaymentRequestAdditionalInfo
from dana.widget.v1.models.account_unbinding_request import AccountUnbindingRequest, AccountUnbindingRequestAdditionalInfo
from dana.widget.v1.models.balance_inquiry_request import BalanceInquiryRequest
from dana.widget.v1.models.balance_inquiry_request_additional_info import BalanceInquiryRequestAdditionalInfo
from dana.widget.v1.models.query_payment_request import QueryPaymentRequest
from dana.widget.v1.models.cancel_order_request import CancelOrderRequest
from dana.widget.v1.models.refund_order_request import RefundOrderRequest
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
def apply_token_request(authorization_code: str) -> ApplyTokenAuthorizationCodeRequest:
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

    # Calculate valid date 10 minutes in the future in Jakarta timezone (GMT+7)
    valid_up_to = (datetime.now(timezone(timedelta(hours=7))) + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S+07:00")

    return WidgetPaymentRequest(
        partner_reference_no=partner_reference_no,
        merchant_id=merchant_id,
        amount=amount,
        valid_up_to=valid_up_to,
        additional_info=additional_info,
    )


@pytest.fixture(scope="function")
def widget_payment_request_with_valid_up_to_beyond_30_minutes() -> WidgetPaymentRequest:
    """
    Fixture to provide a WidgetPaymentRequest with valid_up_to set to 31 minutes
    in the future (Jakarta time, GMT+7).
    
    Uses model_construct() to bypass Pydantic field validators so we can test
    API-level validation (custom_validation) instead of field-level validation.
    """
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

    utc_now = datetime.now(timezone.utc)
    jakarta_now = utc_now + timedelta(hours=7) + timedelta(minutes=31)
    beyond_30_minutes = jakarta_now.strftime("%Y-%m-%dT%H:%M:%S+07:00")

    # Use model_construct() to bypass Pydantic field validators
    # This allows us to test API-level validation (custom_validation) instead of field-level validation
    return WidgetPaymentRequest.model_construct(
        partner_reference_no=partner_reference_no,
        merchant_id=merchant_id,
        amount=amount,
        valid_up_to=beyond_30_minutes,
        additional_info=additional_info,
    )


def account_unbinding_request(access_token: str) -> AccountUnbindingRequest:
    """Fixture to provide AccountUnbindingRequest built from an access token."""

    merchant_id = os.getenv("MERCHANT_ID")
    if not merchant_id:
        pytest.skip("MERCHANT_ID environment variable not set")

    device_id = "Mozilla / 5.0(Windows NT 10.0; Win64; x64)"

    additional_info = AccountUnbindingRequestAdditionalInfo(
        access_token=access_token,
        device_id=device_id,
        latitude="-6.108",
        longitude="10.845",
        end_user_ip_address="127.0.0.1",
    )


    return AccountUnbindingRequest(
        merchant_id=merchant_id,
        additional_info=additional_info,
    )


def balance_inquiry_request(access_token: str) -> BalanceInquiryRequest:
    """Fixture to provide BalanceInquiryRequest built from an access token."""

    partner_reference_no = str(uuid.uuid4())

    additional_info_dict = {
        "access_token": access_token,
        "device_id": "Dummy Device ID"
    }
    
    additional_info = BalanceInquiryRequestAdditionalInfo(**additional_info_dict)

    return BalanceInquiryRequest(
        partner_reference_no=partner_reference_no,
        balance_types=["BALANCE"],
        additional_info=additional_info,
    )


@pytest.fixture(scope="function")
def widget_query_payment_request(widget_payment_request):
    
    # Handle nullable parameters safely
    original_partner_reference_no = None
    if widget_payment_request is not None:
        original_partner_reference_no = widget_payment_request.partner_reference_no
    
    # Use the same merchant ID as other fixtures
    merchant_id = os.environ.get('DANA_MERCHANT_ID', '216620010016033632482')
    
    return QueryPaymentRequest(
        service_code="54",
        merchant_id=merchant_id,
        original_partner_reference_no=original_partner_reference_no,
    )


@pytest.fixture(scope="function")
def widget_cancel_order_request(widget_payment_request):
    """Fixture to provide a CancelOrderRequest using an original payment request."""
    
    # Get the widget payment request from pytest's fixture injection
    original_partner_reference_no = None
    merchant_id = os.environ.get('DANA_MERCHANT_ID', '216620010016033632482')
    
    if widget_payment_request is not None:
        original_partner_reference_no = widget_payment_request.partner_reference_no

    return CancelOrderRequest(
        original_partner_reference_no=original_partner_reference_no,
        merchant_id=merchant_id,
        reason="User cancelled order"
    )


@pytest.fixture(scope="function")
def widget_refund_order_request(widget_payment_request):
    """Fixture to provide a RefundOrderRequest using an original payment request."""
    
    # Handle nullable parameter safely
    original_partner_reference_no = None
    merchant_id = os.environ.get('MERCHANT_ID', '216620010016033632482')
    
    if widget_payment_request is not None:
        original_partner_reference_no = widget_payment_request.partner_reference_no
    
    # Generate a UUID for refund reference number, similar to PHP's implementation
    partner_refund_no = str(uuid.uuid4())
    
    refund_amount = Money(
        value="10000.00",
        currency="IDR"
    )
    
    return RefundOrderRequest(
        merchant_id=merchant_id,
        original_partner_reference_no=original_partner_reference_no,
        partner_refund_no=partner_refund_no,
        refund_amount=refund_amount
    )
