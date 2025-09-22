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


## Additional Documentation
* [Enum Types](#enum-types) - List of available enum constants 
* [WebhookParser](#webhookparser) - Webhook handling and notification parsing

# **create_division**
> create_division(create_division_request) -> CreateDivisionResponse 

Create Division

This API is used to create a new division

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.CreateDivisionRequest import CreateDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.CreateShopRequest import CreateShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.QueryDivisionRequest import QueryDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.QueryMerchantResourceRequest import QueryMerchantResourceRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.QueryShopRequest import QueryShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.UpdateDivisionRequest import UpdateDivisionRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.merchant_management.v1 import MerchantManagementApi
from dana.merchant_management.v1.models.UpdateShopRequest import UpdateShopRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

# configuration and ApiClient object can be used for multiple operations
# They should be singleton through the application lifecycle
configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"), # or you can set PRIVATE_KEY_PATH 
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"), # or you can set ENV
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
    )
)


# Configure API key authorization: CLIENT_SECRET
# For OPEN_API type, we use CLIENT_SECRET authentication
configuration = OpenApiConfiguration(
    api_key=OpenApiAuthSettings(
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET"),
        CLIENT_ID=os.environ.get("CLIENT_ID"),
        DANA_ENV=os.environ.get("DANA_ENV"),
        ENV=os.environ.get("ENV")
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


# Enum Types

```python
from dana.merchant_management.v1.enum import *

# Example of using enum
enum_value = ShopParentType.MERCHANT
```


## ShopParentType
| Value | Description |
|-------|-------------|
| `MERCHANT` |  |
| `DIVISION` |  |
| `EXTERNAL_DIVISION` |  |



## SizeType
| Value | Description |
|-------|-------------|
| `UMI` |  |
| `UKE` |  |
| `UME` |  |
| `UBE` |  |



## Loyalty
| Value | Description |
|-------|-------------|
| `true` |  |
| `false` |  |



## BusinessEntity
| Value | Description |
|-------|-------------|
| `pt` |  |
| `cv` |  |
| `individu` |  |
| `usaha_dagang` |  |
| `yayasan` |  |
| `koperasi` |  |



## OwnerIdType
| Value | Description |
|-------|-------------|
| `KTP` |  |
| `SIM` |  |
| `PASSPORT` |  |
| `SIUP` |  |
| `NIB` |  |



## ShopOwning
| Value | Description |
|-------|-------------|
| `DIRECT_OWNED` |  |
| `FRANCHISED` |  |



## ShopIdType
| Value | Description |
|-------|-------------|
| `INNER_ID` |  |
| `EXTERNAL_ID` |  |



## ParentRoleType
| Value | Description |
|-------|-------------|
| `MERCHANT` |  |
| `DIVISION` |  |
| `EXTERNAL_DIVISION` |  |



## DivisionType
| Value | Description |
|-------|-------------|
| `REGION` |  |
| `AREA` |  |
| `BRANCH` |  |
| `OUTLET` |  |
| `STORE` |  |
| `KIOSK` |  |
| `STALL` |  |
| `COUNTER` |  |
| `BOOTH` |  |
| `POINT_OF_SALE` |  |
| `VENDING_MACHINE` |  |



## GOODSSOLDTYPE
| Value | Description |
|-------|-------------|
| `DIGITAL` |  |
| `PHYSICAL` |  |



## USERPROFILING
| Value | Description |
|-------|-------------|
| `B2B` |  |
| `B2C` |  |



## PgDivisionFlag
| Value | Description |
|-------|-------------|
| `true` |  |
| `false` |  |



## DivisionIdType
| Value | Description |
|-------|-------------|
| `INNER_ID` |  |
| `EXTERNAL_ID` |  |



## ResourceType
| Value | Description |
|-------|-------------|
| `MERCHANT_DEPOSIT_BALANCE` |  |
| `MERCHANT_AVAILABLE_BALANCE` |  |
| `MERCHANT_TOTAL_BALANCE` |  |



## Verified
| Value | Description |
|-------|-------------|
| `true` |  |
| `false` |  |



## DocType
| Value | Description |
|-------|-------------|
| `KTP` |  |
| `SIM` |  |
| `SIUP` |  |
| `NIB` |  |



## ResultStatus
| Value | Description |
|-------|-------------|
| `S` |  |
| `F` |  |
| `U` |  |



## ShopBizType
| Value | Description |
|-------|-------------|
| `ONLINE` |  |
| `OFFLINE` |  |




# WebhookParser

This section demonstrates how to securely verify and parse DANA webhook notifications using the `WebhookParser` utility from the Python SDK.

## Example
```python
import os
from dana.webhook import WebhookParser

# You can provide the DANA_PUBLIC_KEY or DANA_PUBLIC_KEY_PATH
# The parser will prioritize DANA_PUBLIC_KEY_PATH if both are provided.

http_method = "POST"
relative_path_url = "/v1.0/debit/notify"
headers = {
    "X-SIGNATURE": "<signature-from-header>",
    "X-TIMESTAMP": "<timestamp-from-header>"
}
body = '{"original_partner_reference_no": "123...", ...}'  # Raw JSON string from request body

parser = WebhookParser(public_key_path=os.getenv("DANA_PUBLIC_KEY_PATH"))

try:
    finish_notify = parser.parse_webhook(
        http_method=http_method,
        relative_path_url=relative_path_url,
        headers=headers,
        body=body
    )
    print(finish_notify.original_partner_reference_no)
except ValueError as e:
    print(f"Webhook verification failed: {e}")
```

## API Reference

### `WebhookParser`

**Constructor:**
```python
WebhookParser(public_key: str = None, public_key_path: str = None)
```
- `public_key` (str, optional): The DANA gateway's public key as a PEM formatted string. This is used if `public_key_path` is not provided or is empty. Defaults to `None`.
- `public_key_path` (str, optional): The file path to the DANA gateway's public key PEM file. If provided, this will be prioritized over the `public_key` string. Defaults to `None`.

One of `public_key` or `public_key_path` must be provided.

**Method:**
```python
parse_webhook(http_method: str, relative_path_url: str, headers: dict, body: str) -> FinishNotify
```
- `http_method`: HTTP method of the webhook request (e.g., `POST`).
- `relative_path_url`: The relative URL path (e.g., `/v1.0/debit/notify`).
- `headers`: Dictionary containing at least `X-SIGNATURE` and `X-TIMESTAMP`.
- `body`: Raw JSON string of the webhook payload.
- **Returns:** `FinishNotifyRequest` model with parsed data.
- **Raises:** `ValueError` if signature verification fails or the payload is invalid.

## Security Notes
- Always use the official public key provided by DANA for webhook verification.
- Reject any webhook requests that fail signature verification or have malformed payloads.
- Never trust webhook data unless it passes verification.

## Webhook Notification Models

The following webhook notification models may be received:

Model | Description
------------- | -------------
[**FinishNotifyRequest**](../../webhook/v1/FinishNotifyRequest.md) | Represents the standard notification payload for payment events.

