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
from datetime import datetime, timedelta

from dana.payment_gateway.v1.models import *
from dana.payment_gateway.v1.enum import *

@pytest.fixture
def consult_pay_request() -> ConsultPayRequest:

    return ConsultPayRequest(
        merchant_id=os.getenv("MERCHANT_ID"),
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
                source_platform="IPG",
                order_os_type="IOS",
                merchant_app_version="1.0",
                terminal_type="SYSTEM",
                order_terminal_type="WEB",
                extend_info="{\"deviceId\":\"CV19A56370e8a00d54293aab8001e4794\"}"
            ),
            merchant_trans_type="SPECIAL_MOVIE"
        ),
    )

@pytest.fixture
def create_order_by_api_request() -> CreateOrderByApiRequest:
    # Calculate valid date 1 day from now
    valid_up_to = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S+07:00")
    
    return CreateOrderByApiRequest(
        partner_reference_no=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        merchant_id=os.getenv("MERCHANT_ID"),
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
                pay_method=PayMethod.VIRTUAL_ACCOUNT,
                pay_option=PayOption.VIRTUAL_ACCOUNT_BNI,
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

@pytest.fixture
def query_payment_request(create_order_by_api_request: CreateOrderByApiRequest) -> QueryPaymentRequest:
    
    return QueryPaymentRequest(
        service_code="54",  # Payment Gateway service code
        merchant_id=os.getenv("MERCHANT_ID"),
        original_partner_reference_no=create_order_by_api_request.partner_reference_no,
        amount=create_order_by_api_request.amount,
    )

@pytest.fixture
def cancel_order_request(create_order_by_api_request: CreateOrderByApiRequest) -> CancelOrderRequest:
    
    return CancelOrderRequest(
        original_partner_reference_no=create_order_by_api_request.partner_reference_no,
        merchant_id=os.getenv("MERCHANT_ID"),
        reason="Customer requested cancellation",
        amount=create_order_by_api_request.amount,
    )

@pytest.fixture
def refund_order_request(create_order_by_api_request):
    """Fixture to provide a RefundOrderRequest for the tests."""
    
    return RefundOrderRequest(
        original_partner_reference_no="20250303145313698344",
        original_reference_no="20250303111212800110166621502002622",  # Using the reference_no from query payment
        merchant_id="216620020005034264607",
        partner_refund_no=f"REFUND-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",  # Generate a new unique ID
        refund_amount=Money(
            value="10000.00",  # Match the amount from query payment
            currency="IDR"
        ),
        reason="Test refund",
        additional_info=RefundOrderRequestAdditionalInfo(
            payout_account_no="20050000000001503276",
            actor_type="BACK_OFFICE",
            device_id="TEST-DEVICE-ID",
            terminal_type="WEB"
        )
    )
