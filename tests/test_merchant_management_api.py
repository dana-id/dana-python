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

from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models import (
    CreateShopRequest, 
    CreateShopResponse,
    QueryMerchantResourceRequest,
    QueryMerchantResourceResponse,
    QueryShopRequest
)
from dana.rest import ApiException

# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance_merchant_management
from tests.fixtures.merchant_management import create_shop_request, query_merchant_resource_request, query_shop_request

import pytest

@pytest.mark.skip
class TestMerchantManagementApi:
    """Test class for Merchant Management API endpoints"""
    def test_create_shop_and_query_shop_success(self, api_instance_merchant_management: MerchantManagementApi, create_shop_request: CreateShopRequest, query_shop_request: QueryShopRequest):
        """Should successfully create a shop and return success response"""
        
        # Act
        api_response = api_instance_merchant_management.create_shop(create_shop_request)
        
        # Assert - Check response structure and required fields
        assert api_response is not None
        assert hasattr(api_response, 'response')
        assert hasattr(api_response.response, 'body')
        assert hasattr(api_response.response.body, 'result_info')
        
        # Assert - Check result info structure
        result_info = api_response.response.body.result_info
        assert hasattr(result_info, 'result_status')
        assert hasattr(result_info, 'result_code_id')
        assert hasattr(result_info, 'result_code')
        assert hasattr(result_info, 'result_msg')
        
        # Assert - Check expected success response fields
        assert result_info.result_status is not None, "Result status should not be empty"
        assert result_info.result_code_id is not None, "Result code ID should not be empty"
        assert result_info.result_code is not None, "Result code should not be empty"
        assert result_info.result_msg is not None, "Result message should not be empty"
        
        # Assert - Check for successful creation (shopId should be present on success)
        # When successful, response should contain shopId
        assert result_info.result_code in ["SUCCESS", "ROLE_HAS_EXISTS"], result_info.result_msg
        assert result_info.result_code_id == "00000000"
        assert result_info.result_status == "S"
        assert api_response.response.body.shop_id is not None, "Shop ID should not be empty"
        query_shop_request.shop_id = create_shop_request.external_shop_id
        query_shop_response = api_instance_merchant_management.query_shop(query_shop_request)
        
        # Assert - Check query shop response structure
        assert query_shop_response is not None
        assert hasattr(query_shop_response, 'response')
        assert hasattr(query_shop_response.response, 'body')
        assert hasattr(query_shop_response.response.body, 'result_info')
        
        # Assert - Check query shop result info
        query_result_info = query_shop_response.response.body.result_info
        assert query_result_info.result_status is not None
        assert query_result_info.result_code is not None
        
        # Assert - Check if shop information is returned
        if query_result_info.result_code == "SUCCESS":
            assert hasattr(query_shop_response.response.body, 'shop_resource_info')
            assert query_shop_response.response.body.shop_resource_info is not None

    def test_query_merchant_resource_success(self, api_instance_merchant_management: MerchantManagementApi, query_merchant_resource_request: QueryMerchantResourceRequest):
        """Should successfully query merchant resource and return balance information"""
        
        # Act
        api_response = api_instance_merchant_management.query_merchant_resource(query_merchant_resource_request)
        # Assert - Check response structure and required fields
        assert api_response is not None
        assert hasattr(api_response, 'response')
        assert hasattr(api_response.response, 'body')
        assert hasattr(api_response.response.body, 'result_info')
        
        # Assert - Check result info structure
        result_info = api_response.response.body.result_info
        assert hasattr(result_info, 'result_status')
        assert hasattr(result_info, 'result_code_id')
        assert hasattr(result_info, 'result_code')
        assert hasattr(result_info, 'result_msg')
        
        # Assert - Check expected success response fields
        assert result_info.result_status is not None, "Result status should not be empty"
        assert result_info.result_code_id is not None, "Result code ID should not be empty"
        assert result_info.result_code is not None, "Result code should not be empty"
        assert result_info.result_msg is not None, "Result message should not be empty"

        assert result_info.result_code == "SUCCESS"
        assert result_info.result_code_id == "00000000"
        assert result_info.result_status == "S"
 