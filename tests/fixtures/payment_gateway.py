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
import random
import pytest
from datetime import datetime, timedelta, timezone

from dana.payment_gateway.v1.models import *
from dana.payment_gateway.v1.enum import *


class PaymentGatewayFixtures:
    """Payment Gateway fixtures for testing
    
    Provides test fixtures for payment gateway API requests
    """
    
    @staticmethod
    def get_merchant_id() -> str:
        """Get test merchant ID
        
        Returns:
            str: The merchant ID from environment variables
        """
        return os.getenv("MERCHANT_ID") or ""
    
    @staticmethod
    def generate_partner_reference_no(prefix="PY-TEST-") -> str:
        """Generate a unique partner reference number
        
        Args:
            prefix: Optional prefix for the reference number
        
        Returns:
            str: A unique reference number with timestamp and random digits
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_suffix = random.randint(1000, 9999)
        return f"{prefix}{timestamp}{random_suffix}"
    
    @staticmethod
    def get_consult_pay_request() -> ConsultPayRequest:
        """Get a ConsultPayRequest fixture
        
        Returns:
            ConsultPayRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        
        return ConsultPayRequest(
            merchant_id=merchant_id,
            amount=Money(
                value="12345678.00",
                currency="IDR"
            ),
            additional_info=ConsultPayRequestAdditionalInfo(
                buyer=Buyer(
                    external_user_id="8392183912832913821",
                    external_user_type="",
                    nickname="",
                    user_id=""
                ),
                env_info=EnvInfo(
                    session_id="8EU6mLl5mUpUBgyRFT4v7DjfQ3fcauthcenter",
                    token_id="a8d359d6-ca3d-4048-9295-bbea5f6715a6",
                    website_language="en_US",
                    client_ip="10.15.8.189",
                    os_type="Windows.PC",
                    app_version="1.0",
                    sdk_version="1.0",
                    source_platform=SourcePlatform.IPG,
                    order_os_type="IOS",
                    merchant_app_version="1.0",
                    terminal_type=TerminalType.SYSTEM,
                    order_terminal_type=OrderTerminalType.WEB,
                    extend_info="{\"deviceId\":\"CV19A56370e8a00d54293aab8001e4794\"}"
                ),
                merchant_trans_type="SPECIAL_MOVIE"
            ),
        )

    @staticmethod
    def get_consult_pay_request_without_buyer() -> ConsultPayRequest:
        """Get a ConsultPayRequest fixture without buyer
        
        Returns:
            ConsultPayRequest: A configured request object for testing without buyer
        """
        request = PaymentGatewayFixtures.get_consult_pay_request()
        request.additional_info.buyer = None
        return request

    @staticmethod
    def get_consult_pay_request_with_external_store_id() -> ConsultPayRequest:
        """Get a ConsultPayRequest fixture with external store id
        
        Returns:
            ConsultPayRequest: A configured request object for testing with external store id
        """
        request = PaymentGatewayFixtures.get_consult_pay_request()
        request.external_store_id = "test_shop"
        return request

    @staticmethod
    def get_create_order_by_api_request() -> CreateOrderByApiRequest:
        """Get a CreateOrderByApiRequest fixture
        
        Returns:
            CreateOrderByApiRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        partner_reference_no = PaymentGatewayFixtures.generate_partner_reference_no()
        
        # Calculate valid date with Jakarta timezone (GMT+7)
        valid_up_to = (datetime.now(timezone(timedelta(hours=7))) + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
        
        return CreateOrderByApiRequest(
            partner_reference_no=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            merchant_id=merchant_id,
            amount=Money(
                value="222000.00",
                currency="IDR"
            ),
            url_params=[
                UrlParam(
                    url="https://tinknet.my.id/v1/test",
                    type=Type.PAY_RETURN,
                    is_deeplink="Y"
                ),
                UrlParam(
                    url="https://tinknet.my.id/v1/test",
                    type=Type.NOTIFICATION,
                    is_deeplink="Y"
                )
            ],
            valid_up_to=valid_up_to,
            pay_option_details=[
                PayOptionDetail(
                    pay_method=PayMethod.BALANCE,
                    pay_option="",
                    trans_amount=Money(
                        value="222000.00",
                        currency="IDR"
                    )
                )
            ],
            additional_info=CreateOrderByApiAdditionalInfo(
                order=OrderApiObject(
                    order_title="Paket Tinknet 10Mb",
                    scenario="API",
                    merchant_trans_type="SPECIAL_MOVIE"
                ),
                mcc="5732",
                env_info=EnvInfo(
                    source_platform=SourcePlatform.IPG,
                    terminal_type=TerminalType.SYSTEM
                )
            )
        )
    
    @staticmethod
    def get_create_order_by_redirect_request() -> CreateOrderByRedirectRequest:
        """Get a CreateOrderByRedirectRequest fixture with configuration
        Matches the PHP implementation of getCreateOrderByApiRequest but for redirect flow
        
        Returns:
            CreateOrderByRedirectRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        partner_reference_no = PaymentGatewayFixtures.generate_partner_reference_no()
        valid_up_to = (datetime.now(timezone(timedelta(hours=7))) + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
 
        return CreateOrderByRedirectRequest(
            partner_reference_no=partner_reference_no,
            merchant_id=merchant_id,
            amount=Money(
                value="50001.00",
                currency="IDR"
            ),
            valid_up_to=valid_up_to,
            url_params=[
                UrlParam(
                    url="https://example.com/return",
                    type=Type.PAY_RETURN,
                    is_deeplink="N"
                ),
                UrlParam(
                    url="https://example.com/notify",
                    type=Type.NOTIFICATION,
                    is_deeplink="N"
                )
            ],
            additional_info=CreateOrderByRedirectAdditionalInfo(
                order=OrderRedirectObject(
                    order_title="Test Product",
                    scenario="REDIRECT",
                    merchant_trans_type="SPECIAL_MOVIE"
                ),
                mcc="5732",
                env_info=EnvInfo(
                    source_platform=SourcePlatform.IPG,
                    terminal_type=TerminalType.SYSTEM,
                    session_id="8EU6mLl5mUpUBgyRFT4v7DjfQ3fcauthcenter",
                    token_id="a8d359d6-ca3d-4048-9295-bbea5f6715a6",
                    website_language="en_US",
                    client_ip="10.15.8.189",
                    os_type="Windows.PC",
                    app_version="1.0",
                    sdk_version="1.0",
                    client_key="e5806b64-598d-414f-b7f7-83f9576eb6fb",
                    order_terminal_type="WEB",
                    order_os_type="IOS",
                    merchant_app_version="1.0"
                )
            )
        )
        
    @staticmethod
    def get_create_order_by_api_paid_request() -> CreateOrderByApiRequest:
        """Get a CreateOrderByApiRequest fixture with paid configuration
        Matches the PHP implementation of getCreateOrderByApiPaidRequest
        
        Returns:
            CreateOrderByApiRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        partner_reference_no = PaymentGatewayFixtures.generate_partner_reference_no()
        
        return CreateOrderByApiRequest(
            partner_reference_no=partner_reference_no,
            merchant_id=merchant_id,
            amount=Money(
                value="50001.00",
                currency="IDR"
            ),
            valid_up_to="2030-05-01T00:46:43+07:00",
            url_params=[
                UrlParam(
                    url="https://example.com/return",
                    type=Type.PAY_RETURN,
                    is_deeplink="N"
                ),
                UrlParam(
                    url="https://example.com/notify",
                    type=Type.NOTIFICATION,
                    is_deeplink="N"
                )
            ],
            additional_info=CreateOrderByApiAdditionalInfo(
                order=OrderApiObject(
                    order_title="Test Product",
                    scenario="REDIRECT",
                    merchant_trans_type="SPECIAL_MOVIE"
                ),
                mcc="5732",
                env_info=EnvInfo(
                    source_platform=SourcePlatform.IPG,
                    terminal_type=TerminalType.SYSTEM,
                    session_id="8EU6mLl5mUpUBgyRFT4v7DjfQ3fcauthcenter",
                    token_id="a8d359d6-ca3d-4048-9295-bbea5f6715a6",
                    website_language="en_US",
                    client_ip="10.15.8.189",
                    os_type="Windows.PC",
                    app_version="1.0",
                    sdk_version="1.0",
                    client_key="e5806b64-598d-414f-b7f7-83f9576eb6fb",
                    order_terminal_type="WEB",
                    order_os_type="IOS",
                    merchant_app_version="1.0"
                )
            )
        )

    @staticmethod
    def get_query_payment_request(partner_reference_no=None) -> QueryPaymentRequest:
        """Get a QueryPaymentRequest fixture
        
        Args:
            partner_reference_no: Optional specific partner reference number
        
        Returns:
            QueryPaymentRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        
        return QueryPaymentRequest(
            original_partner_reference_no=partner_reference_no or PaymentGatewayFixtures.generate_partner_reference_no(),
            merchant_id=merchant_id,
            service_code="54"
        )

    @staticmethod
    def get_cancel_order_request(partner_reference_no=None) -> CancelOrderRequest:
        """Get a CancelOrderRequest fixture
        
        Args:
            partner_reference_no: Optional specific partner reference number
            
        Returns:
            CancelOrderRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        
        return CancelOrderRequest(
            original_partner_reference_no=partner_reference_no or PaymentGatewayFixtures.generate_partner_reference_no(),
            merchant_id=merchant_id,
            reason="Test cancellation"
        )

    @staticmethod
    def get_create_order_by_api_with_beyond_30_minutes() -> CreateOrderByApiRequest:
        """Get a CreateOrderByApiRequest fixture with ValidUpTo set to 31 minutes in the future.
        
        This fixture directly sets ValidUpTo to bypass setter validation, used to test
        custom validation in Execute() functions.
        
        Returns:
            CreateOrderByApiRequest: A configured request object with invalid valid_up_to
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        partner_reference_no = PaymentGatewayFixtures.generate_partner_reference_no()
        
        # Set valid_up_to to 31 minutes in the future (outside of allowed 30-minute range)
        jakarta_tz = timezone(timedelta(hours=7))
        beyond_30_minutes = (datetime.now(jakarta_tz) + timedelta(minutes=31)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
        
        # Create a valid request first
        request = PaymentGatewayFixtures.get_create_order_by_api_request()
        
        # Use model_construct to bypass field validators and set the invalid date directly
        # This allows us to test custom_validation() in Execute() even when field validator is bypassed
        request = CreateOrderByApiRequest.model_construct(
            partner_reference_no=request.partner_reference_no,
            merchant_id=request.merchant_id,
            amount=request.amount,
            url_params=request.url_params,
            valid_up_to=beyond_30_minutes,  # Directly set invalid date, bypassing field validator
            pay_option_details=request.pay_option_details,
            additional_info=request.additional_info
        )
        
        return request

    @staticmethod
    def get_refund_order_request(
        create_order_request=None, 
        original_reference_no=None,
        original_partner_reference_no=None
    ) -> RefundOrderRequest:
        """Get a RefundOrderRequest fixture
        
        Args:
            create_order_request: Original create order request
            original_reference_no: Original reference number from the successful payment
            original_partner_reference_no: Original partner reference number
            
        Returns:
            RefundOrderRequest: A configured request object for testing
        """
        merchant_id = PaymentGatewayFixtures.get_merchant_id()
        partner_refund_no = PaymentGatewayFixtures.generate_partner_reference_no('PY-REFUND-')
        
        # Get the amount from the original request or use a default value
        refund_amount = None
        if create_order_request and hasattr(create_order_request, 'amount'):
            refund_amount = create_order_request.amount
        else:
            refund_amount = Money(
                value="10000.00",
                currency="IDR"
            )
            
        return RefundOrderRequest(
            merchant_id=merchant_id,
            original_reference_no=original_reference_no,
            original_partner_reference_no=original_partner_reference_no,
            partner_refund_no=partner_refund_no,
            refund_amount=refund_amount,
            reason="Test refund"
        )


# Define fixtures that use the PaymentGatewayFixtures class
@pytest.fixture
def consult_pay_request() -> ConsultPayRequest:
    return PaymentGatewayFixtures.get_consult_pay_request()

@pytest.fixture
def consult_pay_request_without_buyer() -> ConsultPayRequest:
    return PaymentGatewayFixtures.get_consult_pay_request_without_buyer()

@pytest.fixture
def consult_pay_request_with_external_store_id() -> ConsultPayRequest:
    return PaymentGatewayFixtures.get_consult_pay_request_with_external_store_id()

@pytest.fixture
def create_order_by_api_request() -> CreateOrderByApiRequest:
    return PaymentGatewayFixtures.get_create_order_by_api_request()

@pytest.fixture
def create_order_by_redirect_request() -> CreateOrderByRedirectRequest:
    return PaymentGatewayFixtures.get_create_order_by_redirect_request()

@pytest.fixture
def create_order_by_api_paid_request() -> CreateOrderByApiRequest:
    return PaymentGatewayFixtures.get_create_order_by_api_paid_request()

@pytest.fixture
def query_payment_request() -> QueryPaymentRequest:
    # We create a new order request first to get the partner reference number
    order_request = PaymentGatewayFixtures.get_create_order_by_api_request()
    return PaymentGatewayFixtures.get_query_payment_request(order_request.partner_reference_no)

@pytest.fixture
def cancel_order_request() -> CancelOrderRequest:
    # We create a new order request first to get the partner reference number
    order_request = PaymentGatewayFixtures.get_create_order_by_api_request()
    return PaymentGatewayFixtures.get_cancel_order_request(order_request.partner_reference_no)

@pytest.fixture
def refund_order_request() -> RefundOrderRequest:
    order_request = PaymentGatewayFixtures.get_create_order_by_api_request()
    return PaymentGatewayFixtures.get_refund_order_request(
        create_order_request=order_request,
        original_partner_reference_no=order_request.partner_reference_no
    )

@pytest.fixture
def webhook_key_pair():
    return os.getenv("WEBHOOK_PUBLIC_KEY"), os.getenv("WEBHOOK_PRIVATE_KEY")