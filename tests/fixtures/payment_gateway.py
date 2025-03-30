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
