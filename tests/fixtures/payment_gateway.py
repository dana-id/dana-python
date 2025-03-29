import os
import pytest

from dana_python.v1.payment_gateway.models import *

@pytest.fixture
def consult_pay_request() -> ConsultPayRequest:

    return ConsultPayRequest(
        merchant_id=os.getenv("MERCHANT_ID"),
        amount=ConsultPayRequestAmount(
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
