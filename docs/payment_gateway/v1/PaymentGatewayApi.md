# PaymentGatewayApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](PaymentGatewayApi.md#cancel_order) | **POST** /payment-gateway/v1.0/debit/cancel.htm | Cancel Order - Payment Gateway
[**consult_pay**](PaymentGatewayApi.md#consult_pay) | **POST** /v1.0/payment-gateway/consult-pay.htm | Consult Pay - Payment Gateway
[**create_order**](PaymentGatewayApi.md#create_order) | **POST** /payment-gateway/v1.0/debit/payment-host-to-host.htm | Create Order - Payment Gateway
[**query_payment**](PaymentGatewayApi.md#query_payment) | **POST** /payment-gateway/v1.0/debit/status.htm | Query Payment - Payment Gateway
[**refund_order**](PaymentGatewayApi.md#refund_order) | **POST** /payment-gateway/v1.0/debit/refund.htm | Refund Order - Payment Gateway

## Additional Documentation
* [Enum Types](#enum-types) - List of available enum constants 
* [WebhookParser](#webhookparser) - Webhook handling and notification parsing

# **cancel_order**
> cancel_order(cancel_order_request) -> CancelOrderResponse 

Cancel Order - Payment Gateway

This API is used to cancel the order from merchant's platform to DANA

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.CancelOrderRequest import CancelOrderRequest
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
    api_instance = PaymentGatewayApi(api_client)
    cancel_order_request = CancelOrderRequest()

    try:
        api_response = api_instance.cancel_order(cancel_order_request)
        print("The response of PaymentGatewayApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_order_request** | [**CancelOrderRequest**](PaymentGateway/CancelOrderRequest.md)|  | 

### Return type

[**CancelOrderResponse**](PaymentGateway/CancelOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancel order response |  -  |
**202** | Cancel order in progress response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consult_pay**
> consult_pay(consult_pay_request) -> ConsultPayResponse 

Consult Pay - Payment Gateway

This API is used to consult the list of payment methods or payment channels that user has and used in certain transactions or orders

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.ConsultPayRequest import ConsultPayRequest
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
    api_instance = PaymentGatewayApi(api_client)
    consult_pay_request = ConsultPayRequest()

    try:
        api_response = api_instance.consult_pay(consult_pay_request)
        print("The response of PaymentGatewayApi->consult_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->consult_pay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consult_pay_request** | [**ConsultPayRequest**](PaymentGateway/ConsultPayRequest.md)|  | 

### Return type

[**ConsultPayResponse**](PaymentGateway/ConsultPayResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consult pay response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> create_order(create_order_request) -> CreateOrderResponse 

Create Order - Payment Gateway

This API is used for merchant to create order in DANA side

### Example

```python
from dana.payment_gateway.v1.models.create_order_by_redirect_request import CreateOrderByRedirectRequest
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.CreateOrderRequest import CreateOrderRequest
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
    api_instance = PaymentGatewayApi(api_client)
    create_order_request = CreateOrderByRedirectRequest()

    try:
        api_response = api_instance.create_order(create_order_request)
        print("The response of PaymentGatewayApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request** | [**CreateOrderByRedirectRequest**](PaymentGateway/CreateOrderByRedirectRequest.md) or [**CreateOrderByApiRequest**](PaymentGateway/CreateOrderByApiRequest.md)|  | 

### Return type

[**CreateOrderResponse**](PaymentGateway/CreateOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create order response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_payment**
> query_payment(query_payment_request) -> QueryPaymentResponse 

Query Payment - Payment Gateway

This API is used to inquiry payment status and information from merchant's platform to DANA

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.QueryPaymentRequest import QueryPaymentRequest
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
    api_instance = PaymentGatewayApi(api_client)
    query_payment_request = QueryPaymentRequest()

    try:
        api_response = api_instance.query_payment(query_payment_request)
        print("The response of PaymentGatewayApi->query_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->query_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_payment_request** | [**QueryPaymentRequest**](PaymentGateway/QueryPaymentRequest.md)|  | 

### Return type

[**QueryPaymentResponse**](PaymentGateway/QueryPaymentResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query payment response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_order**
> refund_order(refund_order_request) -> RefundOrderResponse 

Refund Order - Payment Gateway

This API is used to refund the order from merchant's platform to DANA

### Example

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.RefundOrderRequest import RefundOrderRequest
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
    api_instance = PaymentGatewayApi(api_client)
    refund_order_request = RefundOrderRequest()

    try:
        api_response = api_instance.refund_order(refund_order_request)
        print("The response of PaymentGatewayApi->refund_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->refund_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_order_request** | [**RefundOrderRequest**](PaymentGateway/RefundOrderRequest.md)|  | 

### Return type

[**RefundOrderResponse**](PaymentGateway/RefundOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund order response |  -  |
**202** | Refund order in progress response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# Enum Types

```python
from dana.payment_gateway.v1.enum import *

# Example of using enum
enum_value = PayMethod.BALANCE
```

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
| `VIRTUAL_ACCOUNT_PANI` |  |

## AcquirementStatus
| Value | Description |
|-------|-------------|
| `INIT` |  |
| `SUCCESS` |  |
| `CLOSED` |  |
| `PAYING` |  |
| `MERCHANT_ACCEPT` |  |
| `CANCELLED` |  |

## ActorType
| Value | Description |
|-------|-------------|
| `USER` |  |
| `MERCHANT` |  |
| `MERCHANT_OPERATOR` |  |
| `BACK_OFFICE` |  |
| `SYSTEM` |  |

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

