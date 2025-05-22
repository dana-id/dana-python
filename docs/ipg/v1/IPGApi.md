# IPGApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_unbinding**](IPGApi.md#account_unbinding) | **POST** /v1.0/registration-account-unbinding.htm | Account unbinding process
[**apply_ott**](IPGApi.md#apply_ott) | **POST** /rest/v1.1/qr/apply-ott | Apply One Time Token
[**apply_token**](IPGApi.md#apply_token) | **POST** /v1.0/access-token/b2b2c.htm | Account binding process to get user token
[**cancel_order**](IPGApi.md#cancel_order) | **POST** /v1.0/debit/cancel.htm | Cancel Order API
[**get_o_auth_url**](IPGApi.md#get_o_auth_url) | **GET** /v1.0/get-auth-code | Get OAuth 2.0 URL for end user authentication
[**ipg_payment**](IPGApi.md#ipg_payment) | **POST** /rest/redirection/v1.0/debit/payment-host-to-host | Process IPG payment
[**query_payment**](IPGApi.md#query_payment) | **POST** /rest/v1.1/debit/status | Query Payment API
[**refund_order**](IPGApi.md#refund_order) | **POST** /v1.0/debit/refund.htm | Refund Order API

# **account_unbinding**
> account_unbinding(account_unbinding_request) -> AccountUnbindingResponse 

Account unbinding process

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
 **account_unbinding_request** | [**AccountUnbindingRequest**](IPG/AccountUnbindingRequest.md)| Account unbinding request body | 

### Return type

[**AccountUnbindingResponse**](IPG/AccountUnbindingResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_ott**
> apply_ott(apply_ott_request) -> ApplyOTTResponse 

Apply One Time Token

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
 **apply_ott_request** | [**ApplyOTTRequest**](IPG/ApplyOTTRequest.md)| Apply OTT request body | 

### Return type

[**ApplyOTTResponse**](IPG/ApplyOTTResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_token**
> apply_token(apply_token_request) -> ApplyTokenResponse 

Account binding process to get user token

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
 **apply_token_request** | [**ApplyTokenAuthorizationCodeRequest**](IPG/ApplyTokenAuthorizationCodeRequest.md) or [**ApplyTokenRefreshTokenRequest**](IPG/ApplyTokenRefreshTokenRequest.md)| Apply token request body | 

### Return type

[**ApplyTokenResponse**](IPG/ApplyTokenResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> cancel_order(cancel_order_request) -> CancelOrderResponse 

Cancel Order API

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

# **get_o_auth_url**
> get_o_auth_url(partner_id, timestamp, external_id, channel_id, scopes, redirect_url, state, merchant_id=merchant_id, sub_merchant_id=sub_merchant_id, seamless_data=seamless_data, lang=lang, allow_registration=allow_registration) -> GetOAuthUrlResponse 

Get OAuth 2.0 URL for end user authentication

TThis API is used to generate OAuth 2.0 redirect URL to DANA to initiate account binding process where the user will be able to register/login from DANA page

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

    try:
        api_response = api_instance.get_o_auth_url(partner_id, timestamp, external_id, channel_id, scopes, redirect_url, state, merchant_id=merchant_id, sub_merchant_id=sub_merchant_id, seamless_data=seamless_data, lang=lang, allow_registration=allow_registration)
        print("The response of IPGApi->get_o_auth_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPGApi->get_o_auth_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_id** | **str**| Information of partner identifier | 
 **timestamp** | **str**| Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
 **external_id** | **str**| Information of partner identifier | 
 **channel_id** | **str**| Information of channel identifier | 
 **scopes** | [**List[str]**](str.md)| The scopes of the authorization | 
 **redirect_url** | **str**| When user authorization is success, the user will be redirected to this URL | 
 **state** | **str**| Random string for CSRF protection purposes | 
 **merchant_id** | **str**| Merchant identifier that is unique per each merchant | [optional] 
 **sub_merchant_id** | **str**| Information of sub merchant identifier | [optional] 
 **seamless_data** | [**SeamlessData**](.md)| Option for binding process. This is a JSON object that will be automatically URL-encoded.  | [optional] 
 **lang** | **str**| Service language code, ISO 639-1 | [optional] 
 **allow_registration** | **str**| If value equals true, provider may enable registration process during binding. Default true | [optional] 

### Return type

[**GetOAuthUrlResponse**](IPG/GetOAuthUrlResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipg_payment**
> ipg_payment(ipg_payment_request) -> IPGPaymentResponse 

Process IPG payment

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
**200** | Payment consultation request sent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_payment**
> query_payment(query_payment_request) -> QueryPaymentResponse 

Query Payment API

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

Refund Order API

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

