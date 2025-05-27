# IPGApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_unbinding**](IPGApi.md#account_unbinding) | **POST** /v1.0/registration-account-unbinding.htm | Account unbinding - Binding
[**apply_ott**](IPGApi.md#apply_ott) | **POST** /rest/v1.1/qr/apply-ott | Apply OTT - IPG
[**apply_token**](IPGApi.md#apply_token) | **POST** /v1.0/access-token/b2b2c.htm | Apply Token, required by Apply OTT - Binding
[**cancel_order**](IPGApi.md#cancel_order) | **POST** /v1.0/debit/cancel.htm | Cancel Order - IPG
[**ipg_payment**](IPGApi.md#ipg_payment) | **POST** /rest/redirection/v1.0/debit/payment-host-to-host | IPG payment - IPG
[**query_payment**](IPGApi.md#query_payment) | **POST** /rest/v1.1/debit/status | Query Payment - IPG
[**refund_order**](IPGApi.md#refund_order) | **POST** /v1.0/debit/refund.htm | Refund Order - IPG

# **account_unbinding**
> account_unbinding(account_unbinding_request) -> AccountUnbindingResponse 

Account unbinding - Binding

This API is used to reverses the account binding process by revoking the accessToken and refreshToken

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.AccountUnbindingRequest import AccountUnbindingRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    account_unbinding_request = AccountUnbindingRequest()

    try:
        api_response = api_instance.account_unbinding(account_unbinding_request)
        print("The response of IPGApi->account_unbinding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->account_unbinding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_unbinding_request** | [**AccountUnbindingRequest**](IPG/AccountUnbindingRequest.md)|  | 

### Return type

[**AccountUnbindingResponse**](IPG/AccountUnbindingResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account unbinding response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_ott**
> apply_ott(apply_ott_request) -> ApplyOTTResponse 

Apply OTT - IPG

This API is used to get one time token that will be used as authorization parameter upon redirecting to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.ApplyOTTRequest import ApplyOTTRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    apply_ott_request = ApplyOTTRequest()

    try:
        api_response = api_instance.apply_ott(apply_ott_request)
        print("The response of IPGApi->apply_ott:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->apply_ott: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_ott_request** | [**ApplyOTTRequest**](IPG/ApplyOTTRequest.md)|  | 

### Return type

[**ApplyOTTResponse**](IPG/ApplyOTTResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apply OTT response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_token**
> apply_token(apply_token_request) -> ApplyTokenResponse 

Apply Token, required by Apply OTT - Binding

This API is used to finalized account binding process by exchanging the authCode into accessToken that can be used as user authorization

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
from dana.ipg.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.ApplyTokenRequest import ApplyTokenRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    apply_token_request = ApplyTokenAuthorizationCodeRequest()

    try:
        api_response = api_instance.apply_token(apply_token_request)
        print("The response of IPGApi->apply_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->apply_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_token_request** | [**ApplyTokenAuthorizationCodeRequest**](IPG/ApplyTokenAuthorizationCodeRequest.md) or [**ApplyTokenRefreshTokenRequest**](IPG/ApplyTokenRefreshTokenRequest.md)|  | 

### Return type

[**ApplyTokenResponse**](IPG/ApplyTokenResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apply token response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> cancel_order(cancel_order_request) -> CancelOrderResponse 

Cancel Order - IPG

This API is used to cancel the order from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.CancelOrderRequest import CancelOrderRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    cancel_order_request = CancelOrderRequest()

    try:
        api_response = api_instance.cancel_order(cancel_order_request)
        print("The response of IPGApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_order_request** | [**CancelOrderRequest**](IPG/CancelOrderRequest.md)|  | 

### Return type

[**CancelOrderResponse**](IPG/CancelOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancel order response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipg_payment**
> ipg_payment(ipg_payment_request) -> IPGPaymentResponse 

IPG payment - IPG

This API is used to initiate payment from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.IPGPaymentRequest import IPGPaymentRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    ipg_payment_request = IPGPaymentRequest()

    try:
        api_response = api_instance.ipg_payment(ipg_payment_request)
        print("The response of IPGApi->ipg_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->ipg_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipg_payment_request** | [**IPGPaymentRequest**](IPG/IPGPaymentRequest.md)|  | 

### Return type

[**IPGPaymentResponse**](IPG/IPGPaymentResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IPG payment response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_payment**
> query_payment(query_payment_request) -> QueryPaymentResponse 

Query Payment - IPG

This API is used to inquiry payment status and information from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.QueryPaymentRequest import QueryPaymentRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    query_payment_request = QueryPaymentRequest()

    try:
        api_response = api_instance.query_payment(query_payment_request)
        print("The response of IPGApi->query_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->query_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_payment_request** | [**QueryPaymentRequest**](IPG/QueryPaymentRequest.md)|  | 

### Return type

[**QueryPaymentResponse**](IPG/QueryPaymentResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query payment response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_order**
> refund_order(refund_order_request) -> RefundOrderResponse 

Refund Order - IPG

This API is used to refund the order from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import IPGApi
from dana.payment_gateway.v1.models.RefundOrderRequest import RefundOrderRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = IPGApi(api_client)
    refund_order_request = RefundOrderRequest()

    try:
        api_response = api_instance.refund_order(refund_order_request)
        print("The response of IPGApi->refund_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->refund_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_order_request** | [**RefundOrderRequest**](IPG/RefundOrderRequest.md)|  | 

### Return type

[**RefundOrderResponse**](IPG/RefundOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund order response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

