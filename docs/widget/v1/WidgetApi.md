# WidgetApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_unbinding**](WidgetApi.md#account_unbinding) | **POST** /v1.0/registration-account-unbinding.htm | Account unbinding - Binding
[**apply_ott**](WidgetApi.md#apply_ott) | **POST** /rest/v1.1/qr/apply-ott | Apply OTT - Widget
[**apply_token**](WidgetApi.md#apply_token) | **POST** /v1.0/access-token/b2b2c.htm | Apply Token, required by Apply OTT - Binding
[**balance_inquiry**](WidgetApi.md#balance_inquiry) | **POST** /v1.0/balance-inquiry.htm | Balance Inquiry
[**cancel_order**](WidgetApi.md#cancel_order) | **POST** /v1.0/debit/cancel.htm | Cancel Order - Widget
[**query_payment**](WidgetApi.md#query_payment) | **POST** /rest/v1.1/debit/status | Query Payment - Widget
[**query_user_profile**](WidgetApi.md#query_user_profile) | **POST** /dana/member/query/queryUserProfile.htm | Query User Profile
[**refund_order**](WidgetApi.md#refund_order) | **POST** /v1.0/debit/refund.htm | Refund Order - Widget
[**widget_payment**](WidgetApi.md#widget_payment) | **POST** /rest/redirection/v1.0/debit/payment-host-to-host | Widget Payment - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.AccountUnbindingRequest import AccountUnbindingRequest
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
    api_instance = WidgetApi(api_client)
    account_unbinding_request = AccountUnbindingRequest()

    try:
        api_response = api_instance.account_unbinding(account_unbinding_request)
        print("The response of WidgetApi->account_unbinding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->account_unbinding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_unbinding_request** | [**AccountUnbindingRequest**](Widget/AccountUnbindingRequest.md)|  | 

### Return type

[**AccountUnbindingResponse**](Widget/AccountUnbindingResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account unbinding response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_ott**
> apply_ott(apply_ott_request) -> ApplyOTTResponse 

Apply OTT - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.ApplyOTTRequest import ApplyOTTRequest
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
    api_instance = WidgetApi(api_client)
    apply_ott_request = ApplyOTTRequest()

    try:
        api_response = api_instance.apply_ott(apply_ott_request)
        print("The response of WidgetApi->apply_ott:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->apply_ott: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_ott_request** | [**ApplyOTTRequest**](Widget/ApplyOTTRequest.md)|  | 

### Return type

[**ApplyOTTResponse**](Widget/ApplyOTTResponse.md)

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
from dana.widget.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.ApplyTokenRequest import ApplyTokenRequest
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
    api_instance = WidgetApi(api_client)
    apply_token_request = ApplyTokenAuthorizationCodeRequest()

    try:
        api_response = api_instance.apply_token(apply_token_request)
        print("The response of WidgetApi->apply_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->apply_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_token_request** | [**ApplyTokenAuthorizationCodeRequest**](Widget/ApplyTokenAuthorizationCodeRequest.md) or [**ApplyTokenRefreshTokenRequest**](Widget/ApplyTokenRefreshTokenRequest.md)|  | 

### Return type

[**ApplyTokenResponse**](Widget/ApplyTokenResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apply token response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_inquiry**
> balance_inquiry(balance_inquiry_request) -> BalanceInquiryResponse 

Balance Inquiry

This API is used to query user's DANA account balance via merchant

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.BalanceInquiryRequest import BalanceInquiryRequest
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
    api_instance = WidgetApi(api_client)
    balance_inquiry_request = BalanceInquiryRequest()

    try:
        api_response = api_instance.balance_inquiry(balance_inquiry_request)
        print("The response of WidgetApi->balance_inquiry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->balance_inquiry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_inquiry_request** | [**BalanceInquiryRequest**](Widget/BalanceInquiryRequest.md)|  | 

### Return type

[**BalanceInquiryResponse**](Widget/BalanceInquiryResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance inquiry response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> cancel_order(cancel_order_request) -> CancelOrderResponse 

Cancel Order - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.CancelOrderRequest import CancelOrderRequest
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
    api_instance = WidgetApi(api_client)
    cancel_order_request = CancelOrderRequest()

    try:
        api_response = api_instance.cancel_order(cancel_order_request)
        print("The response of WidgetApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_order_request** | [**CancelOrderRequest**](Widget/CancelOrderRequest.md)|  | 

### Return type

[**CancelOrderResponse**](Widget/CancelOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancel order response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_payment**
> query_payment(query_payment_request) -> QueryPaymentResponse 

Query Payment - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.QueryPaymentRequest import QueryPaymentRequest
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
    api_instance = WidgetApi(api_client)
    query_payment_request = QueryPaymentRequest()

    try:
        api_response = api_instance.query_payment(query_payment_request)
        print("The response of WidgetApi->query_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->query_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_payment_request** | [**QueryPaymentRequest**](Widget/QueryPaymentRequest.md)|  | 

### Return type

[**QueryPaymentResponse**](Widget/QueryPaymentResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query payment response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_user_profile**
> query_user_profile(query_user_profile_request) -> QueryUserProfileResponse 

Query User Profile

The API is used to query user profile such as DANA balance (unit in IDR), masked DANA phone number, KYC or OTT (one time token) between merchant server and DANA's server

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.QueryUserProfileRequest import QueryUserProfileRequest
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
    api_instance = WidgetApi(api_client)
    query_user_profile_request = QueryUserProfileRequest()

    try:
        api_response = api_instance.query_user_profile(query_user_profile_request)
        print("The response of WidgetApi->query_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->query_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_user_profile_request** | [**QueryUserProfileRequest**](Widget/QueryUserProfileRequest.md)|  | 

### Return type

[**QueryUserProfileResponse**](Widget/QueryUserProfileResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query user profile response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_order**
> refund_order(refund_order_request) -> RefundOrderResponse 

Refund Order - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.RefundOrderRequest import RefundOrderRequest
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
    api_instance = WidgetApi(api_client)
    refund_order_request = RefundOrderRequest()

    try:
        api_response = api_instance.refund_order(refund_order_request)
        print("The response of WidgetApi->refund_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->refund_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_order_request** | [**RefundOrderRequest**](Widget/RefundOrderRequest.md)|  | 

### Return type

[**RefundOrderResponse**](Widget/RefundOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund order response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **widget_payment**
> widget_payment(widget_payment_request) -> WidgetPaymentResponse 

Widget Payment - Widget

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
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.WidgetPaymentRequest import WidgetPaymentRequest
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
    api_instance = WidgetApi(api_client)
    widget_payment_request = WidgetPaymentRequest()

    try:
        api_response = api_instance.widget_payment(widget_payment_request)
        print("The response of WidgetApi->widget_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->widget_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_payment_request** | [**WidgetPaymentRequest**](Widget/WidgetPaymentRequest.md)|  | 

### Return type

[**WidgetPaymentResponse**](Widget/WidgetPaymentResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Widget payment response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

