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
from dana.api_client import ApiClient
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models import PaymentInfo, ConsultPayRequest, CreateOrderByApiRequest, CreateOrderByRedirectRequest
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.rest import ApiException
from tests.fixtures.payment_gateway import consult_pay_request

class TestPaymentGatewayApi:
    
    @classmethod
    def setup_class(cls):
        cls.config = SnapConfiguration(api_key=AuthSettings(
             PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
             ORIGIN=os.environ.get("ORIGIN"),
             X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
             CHANNEL_ID=os.environ.get("CHANNEL_ID"),
             ENV=Env.SANDBOX
            ),
        )

    def test_consult_pay_with_str_private_key_success(self, consult_pay_request: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        with ApiClient(self.config) as api_client:
            api_instance = PaymentGatewayApi(api_client)
            api_response = api_instance.consult_pay(consult_pay_request)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'

        assert all(isinstance(i, PaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)
