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

from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.api_client import ApiClient
from dana.payment_gateway.v1 import PaymentGatewayApi

@pytest.fixture(scope="class")
def api_instance():
    """Fixture to provide an API instance for the tests."""
    auth_settings = AuthSettings(
        PRIVATE_KEY=os.getenv("PRIVATE_KEY"),
        ORIGIN=os.getenv("ORIGIN"),
        X_PARTNER_ID=os.getenv("X_PARTNER_ID"),
        CHANNEL_ID=os.getenv("CHANNEL_ID"),
        ENV=Env.SANDBOX
    )
    config = SnapConfiguration(api_key=auth_settings)
    client = ApiClient(config)
    api_instance = PaymentGatewayApi(client)
    
    yield api_instance
    
