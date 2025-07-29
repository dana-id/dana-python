# MerchantManagementApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_division**](MerchantManagementApi.md#create_division) | **POST** /dana/merchant/division/createDivision.htm | Create Division
[**create_shop**](MerchantManagementApi.md#create_shop) | **POST** /dana/merchant/shop/createShop.htm | Member – Create Shop
[**query_division**](MerchantManagementApi.md#query_division) | **POST** /dana/merchant/division/queryDivision.htm | Query Division
[**query_merchant_resource**](MerchantManagementApi.md#query_merchant_resource) | **POST** /dana/merchant/queryMerchantResource.htm | Member – Merchant Open API Check Disbursement Account
[**query_shop**](MerchantManagementApi.md#query_shop) | **POST** /dana/merchant/shop/queryShop.htm | Member – Query Shop
[**update_division**](MerchantManagementApi.md#update_division) | **POST** /dana/merchant/division/updateDivision.htm | Update Division
[**update_shop**](MerchantManagementApi.md#update_shop) | **POST** /dana/merchant/shop/updateShop.htm | Update Shop


# **create_division**
> create_division(create_division_request) -> CreateDivisionResponse 

Create Division

This API is used to create a new division

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.CreateDivisionRequest import CreateDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    create_division_request = CreateDivisionRequest()

    try:
        api_response = api_instance.create_division(create_division_request)
        print("The response of MerchantManagementApi->create_division:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->create_division: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_division_request** | [**CreateDivisionRequest**](MerchantManagement/CreateDivisionRequest.md)|  | 

### Return type

[**CreateDivisionResponse**](MerchantManagement/CreateDivisionResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create division response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shop**
> create_shop(create_shop_request) -> CreateShopResponse 

Member – Create Shop

Create shop under merchant or division

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.CreateShopRequest import CreateShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    create_shop_request = CreateShopRequest()

    try:
        api_response = api_instance.create_shop(create_shop_request)
        print("The response of MerchantManagementApi->create_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->create_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shop_request** | [**CreateShopRequest**](MerchantManagement/CreateShopRequest.md)|  | 

### Return type

[**CreateShopResponse**](MerchantManagement/CreateShopResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create shop response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_division**
> query_division(query_division_request) -> QueryDivisionResponse 

Query Division

This API is used to obtain information of division

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.QueryDivisionRequest import QueryDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    query_division_request = QueryDivisionRequest()

    try:
        api_response = api_instance.query_division(query_division_request)
        print("The response of MerchantManagementApi->query_division:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->query_division: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_division_request** | [**QueryDivisionRequest**](MerchantManagement/QueryDivisionRequest.md)|  | 

### Return type

[**QueryDivisionResponse**](MerchantManagement/QueryDivisionResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query division response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_merchant_resource**
> query_merchant_resource(query_merchant_resource_request) -> QueryMerchantResourceResponse 

Member – Merchant Open API Check Disbursement Account

The interface is check merchant resource info (account balance merchant)

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.QueryMerchantResourceRequest import QueryMerchantResourceRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    query_merchant_resource_request = QueryMerchantResourceRequest()

    try:
        api_response = api_instance.query_merchant_resource(query_merchant_resource_request)
        print("The response of MerchantManagementApi->query_merchant_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->query_merchant_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_merchant_resource_request** | [**QueryMerchantResourceRequest**](MerchantManagement/QueryMerchantResourceRequest.md)|  | 

### Return type

[**QueryMerchantResourceResponse**](MerchantManagement/QueryMerchantResourceResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query merchant resource response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_shop**
> query_shop(query_shop_request) -> QueryShopResponse 

Member – Query Shop

This API is used to obtain information of shop information

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.QueryShopRequest import QueryShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    query_shop_request = QueryShopRequest()

    try:
        api_response = api_instance.query_shop(query_shop_request)
        print("The response of MerchantManagementApi->query_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->query_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_shop_request** | [**QueryShopRequest**](MerchantManagement/QueryShopRequest.md)|  | 

### Return type

[**QueryShopResponse**](MerchantManagement/QueryShopResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query shop response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_division**
> update_division(update_division_request) -> UpdateDivisionResponse 

Update Division

This API is used to update the division information

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.UpdateDivisionRequest import UpdateDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    update_division_request = UpdateDivisionRequest()

    try:
        api_response = api_instance.update_division(update_division_request)
        print("The response of MerchantManagementApi->update_division:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->update_division: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_division_request** | [**UpdateDivisionRequest**](MerchantManagement/UpdateDivisionRequest.md)|  | 

### Return type

[**UpdateDivisionResponse**](MerchantManagement/UpdateDivisionResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update division response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop**
> update_shop(update_shop_request) -> UpdateShopResponse 

Update Shop

This API is used to update the shop information

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import MerchantManagementApi
from dana.widget.v1.models.UpdateShopRequest import UpdateShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = MerchantManagementApi(api_client)
    update_shop_request = UpdateShopRequest()

    try:
        api_response = api_instance.update_shop(update_shop_request)
        print("The response of MerchantManagementApi->update_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantManagementApi->update_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_shop_request** | [**UpdateShopRequest**](MerchantManagement/UpdateShopRequest.md)|  | 

### Return type

[**UpdateShopResponse**](MerchantManagement/UpdateShopResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update shop response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

