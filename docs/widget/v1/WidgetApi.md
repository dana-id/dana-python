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

## Additional Documentation
* [Enum Types](#enum-types) - List of available enum constants 
* [WebhookParser](#webhookparser) - Webhook handling and notification parsing
* [OAuth URL Generation](#oauth-url-generation) - Generate OAuth URLs for authorization
* [Complete Payment URL Generation](#complete-payment-url-generation) - Generate URL to complete the payment by combining webRedirectUrl with OTT token

# **account_unbinding**
> account_unbinding(account_unbinding_request) -> AccountUnbindingResponse 

Account unbinding - Binding

This API is used to reverses the account binding process by revoking the accessToken and refreshToken

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.AccountUnbindingRequest import AccountUnbindingRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.ApplyOTTRequest import ApplyOTTRequest
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

```python
from dana.widget.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.ApplyTokenRequest import ApplyTokenRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.BalanceInquiryRequest import BalanceInquiryRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.CancelOrderRequest import CancelOrderRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.QueryPaymentRequest import QueryPaymentRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.QueryUserProfileRequest import QueryUserProfileRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.RefundOrderRequest import RefundOrderRequest
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

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import WidgetApi
from dana.widget.v1.models.WidgetPaymentRequest import WidgetPaymentRequest
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

# Enum Types

```python
from dana.widget.v1.enum import *

# Example of using enum
enum_value = ServiceType.PARKING
```

## ServiceType
| Value | Description |
|-------|-------------|
| `PARKING` |  |
| `INVESTMENT` |  |

## ServiceScenario
| Value | Description |
|-------|-------------|
| `SCAN_AND_PAY` |  |
| `EXIT_AND_PAY` |  |
| `EMAS_PURCHASE` |  |

## PromoType
| Value | Description |
|-------|-------------|
| `CASH_BACK` |  |
| `DISCOUNT` |  |
| `VOUCHER` |  |
| `POINT` |  |

## AcquirementStatus
| Value | Description |
|-------|-------------|
| `INIT` |  |
| `SUCCESS` |  |
| `CLOSED` |  |
| `PAYING` |  |
| `MERCHANT_ACCEPT` |  |
| `CANCELLED` |  |

## Mode
| Value | Description |
|-------|-------------|
| `API` |  |
| `DEEPLINK` |  |

## ResourceType
| Value | Description |
|-------|-------------|
| `BALANCE` |  |
| `TRANSACTION_URL` |  |
| `MASK_DANA_ID` |  |
| `TOPUP_URL` |  |
| `OTT` |  |
| `USER_KYC` |  |

## ResultStatus
| Value | Description |
|-------|-------------|
| `S` |  |
| `F` |  |
| `U` |  |

## SourcePlatform
| Value | Description |
|-------|-------------|
| `IPG` |  |

## TerminalType
| Value | Description |
|-------|-------------|
| `APP` |  |
| `WEB` |  |
| `WAP` |  |
| `SYSTEM` |  |

## OrderTerminalType
| Value | Description |
|-------|-------------|
| `APP` |  |
| `WEB` |  |
| `WAP` |  |
| `SYSTEM` |  |

## PayMethod
| Value | Description |
|-------|-------------|
| `BALANCE` |  |
| `COUPON` |  |
| `NET_BANKING` |  |
| `CREDIT_CARD` |  |
| `DEBIT_CARD` |  |
| `VIRTUAL_ACCOUNT` |  |
| `OTC` |  |
| `DIRECT_DEBIT_CREDIT_CARD` |  |
| `DIRECT_DEBIT_DEBIT_CARD` |  |
| `ONLINE_CREDIT` |  |
| `LOAN_CREDIT` |  |
| `NETWORK_PAY` |  |
| `CARD` |  |

## PayOption
| Value | Description |
|-------|-------------|
| `NETWORK_PAY_PG_SPAY` |  |
| `NETWORK_PAY_PG_OVO` |  |
| `NETWORK_PAY_PG_GOPAY` |  |
| `NETWORK_PAY_PG_LINKAJA` |  |
| `NETWORK_PAY_PG_CARD` |  |
| `NETWORK_PAY_PC_INDOMARET` |  |
| `NETWORK_PAY_PG_QRIS` |  |
| `VIRTUAL_ACCOUNT_BCA` |  |
| `VIRTUAL_ACCOUNT_BNI` |  |
| `VIRTUAL_ACCOUNT_MANDIRI` |  |
| `VIRTUAL_ACCOUNT_BRI` |  |
| `VIRTUAL_ACCOUNT_BTPN` |  |
| `VIRTUAL_ACCOUNT_CIMB` |  |
| `VIRTUAL_ACCOUNT_PERMATA` |  |
| `VIRTUAL_ACCOUNT_PANIN` |  |

## Type
| Value | Description |
|-------|-------------|
| `PAY_RETURN` |  |
| `NOTIFICATION` |  |

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


## OAuth URL Generation

Use the `Oauth2UrlData` class and `Util.generate_oauth_url()` to generate OAuth authorization URLs:

```python
from dana.widget.v1.models.oauth2_url_data import Oauth2UrlData
from dana.widget.v1.util import Util
from dana.widget.v1.enum import Mode

private_key = os.environ.get(PRIVATE_KEY)

# Set up OAuth2 URL data
oauth2_url_data = Oauth2UrlData(
    external_id=external_id,
    merchant_id=os.environ.get(MERCHANT_ID),  # from env variable
    redirect_url=https://google.com,
    mode=Mode.DEEPLINK # the default mode is API if not set
)

# You can set additional fields as needed
oauth2_url_data.seamless_data = {
    mobileNumber: 08787584xxxx  # Optional data for seamless login
}

# Generate the OAuth URL
oauth_url = Util.generate_oauth_url(oauth2_url_data, private_key)

# You can redirect the user to this URL to start the OAuth flow
print(f"Generated OAuth URL: {oauth_url}")
```

## Complete Payment URL Generation

```python
from dana.widget.v1.util import Util
from dana.widget.v1.models.widget_payment_response import WidgetPaymentResponse
from dana.widget.v1.models.apply_ott_response import ApplyOTTResponse

# Build the complete payment URL
widget_payment_response = WidgetPaymentResponse()
apply_ott_response = ApplyOTTResponse()
payment_url = Util.generate_complete_payment_url(widget_payment_response, apply_ott_response)

# Redirect the user to this URL to complete the payment
print(f"Redirect user to: {payment_url}")
```
