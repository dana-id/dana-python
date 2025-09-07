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
from dana.utils.open_api_configuration import OpenApiConfiguration, OpenApiAuthSettings
from dana.api_client import ApiClient
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.widget.v1 import WidgetApi
from dana.disbursement.v1 import DisbursementApi
from dana.merchant_management.v1 import MerchantManagementApi

@pytest.fixture(scope="class")
def api_instance_payment_gateway():
    """Fixture to provide an API instance for the tests using PRIVATE_KEY."""
    auth_settings = AuthSettings(
        PRIVATE_KEY=os.getenv("PRIVATE_KEY"),
        ORIGIN=os.getenv("ORIGIN"),
        X_PARTNER_ID=os.getenv("X_PARTNER_ID"),
        CHANNEL_ID=os.getenv("CHANNEL_ID"),
        DANA_ENV=Env.SANDBOX,
        ENV=Env.SANDBOX
    )
    config = SnapConfiguration(api_key=auth_settings)
    client = ApiClient(config)

    api_instance = PaymentGatewayApi(client)
    
    yield api_instance

@pytest.fixture(scope="class")
def api_instance_payment_gateway_with_key_path():
    """Fixture to provide an API instance for the tests using PRIVATE_KEY_PATH."""
    # For CI/CD, we assume the private key is saved to a temporary file
    # Create a temporary file with the private key content
    import tempfile
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        pytest.skip("PRIVATE_KEY environment variable not set")
        
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".pem")
    try:
        temp_file.write(private_key)
        temp_file.close()
        
        auth_settings = AuthSettings(
            PRIVATE_KEY_PATH=temp_file.name,  # Use the path instead of the key content
            ORIGIN=os.getenv("ORIGIN"),
            X_PARTNER_ID=os.getenv("X_PARTNER_ID"),
            CHANNEL_ID=os.getenv("CHANNEL_ID"),
            DANA_ENV=Env.SANDBOX,
        )
        config = SnapConfiguration(api_key=auth_settings)
        client = ApiClient(config)

        api_instance = PaymentGatewayApi(client)
        
        yield api_instance
    finally:
        # Clean up the temporary file
        os.unlink(temp_file.name)

@pytest.fixture(scope="class")
def api_instance_widget():
    """Fixture to provide an API instance for the tests."""
    auth_settings = AuthSettings(
        PRIVATE_KEY=os.getenv("PRIVATE_KEY"),
        ORIGIN=os.getenv("ORIGIN"),
        X_PARTNER_ID=os.getenv("X_PARTNER_ID"),
        DANA_ENV=Env.SANDBOX,
        ENV=Env.SANDBOX
    )
    config = SnapConfiguration(api_key=auth_settings)
    client = ApiClient(config)

    api_instance = WidgetApi(client)
    
    yield api_instance

    
@pytest.fixture(scope="class")
def api_instance_disbursement():
    """Fixture to provide a Disbursement API instance for the tests."""
    auth_settings = AuthSettings(
        PRIVATE_KEY=os.getenv("PRIVATE_KEY"),
        ORIGIN=os.getenv("ORIGIN"),
        X_PARTNER_ID=os.getenv("X_PARTNER_ID"),
        CHANNEL_ID=os.getenv("CHANNEL_ID"),
        DANA_ENV=Env.SANDBOX,
        ENV=Env.SANDBOX
    )
    config = SnapConfiguration(api_key=auth_settings)
    client = ApiClient(config)

    api_instance = DisbursementApi(client)
    
    yield api_instance

@pytest.fixture(scope="class")
def api_instance_merchant_management():
    """Fixture to provide a Merchant Management API instance for the tests."""
    auth_settings = OpenApiAuthSettings(
        CLIENT_SECRET=os.getenv("CLIENT_SECRET"),
        CLIENT_ID=os.getenv("CLIENT_ID"),
        DANA_ENV=Env.SANDBOX,
        ENV=Env.SANDBOX,
        PRIVATE_KEY=os.getenv("PRIVATE_KEY"),
        X_PARTNER_ID=os.getenv("X_PARTNER_ID")
    )
    config = OpenApiConfiguration(api_key=auth_settings)
    client = ApiClient(config)

    api_instance = MerchantManagementApi(client)
    
    yield api_instance
