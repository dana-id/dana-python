# PaymentGatewayApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](PaymentGatewayApi.md#cancel_order) | **POST** /v1.0/debit/cancel.htm | Cancel Order API
[**consult_pay**](PaymentGatewayApi.md#consult_pay) | **POST** /v1.0/payment-gateway/consult-pay.htm | Consult Pay API
[**create_order**](PaymentGatewayApi.md#create_order) | **POST** /v1.0/payment-gateway/payment.htm | Create Payment Order
[**query_payment**](PaymentGatewayApi.md#query_payment) | **POST** /v1.0/debit/status.htm | Query Payment
[**refund_order**](PaymentGatewayApi.md#refund_order) | **POST** /v1.0/debit/refund.htm | Refund Order API


### Webhooks

The following webhook notifications may be sent to the URLs specified in your API requests.

Model | Description
------------- | -------------
[**FinishNotify**](PaymentGateway/FinishNotify.md) | FinishNotify

# **cancel_order**
> cancel_order(cancel_order_request) -> CancelOrderResponse 

Cancel Order API

This API is used to cancel the order from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.CancelOrderRequest import CancelOrderRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consult_pay**
> consult_pay(consult_pay_request) -> ConsultPayResponse 

Consult Pay API

This API is used to consult the list of payment methods or payment channels that user has and used in certain transactions or orders

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH
* ENV

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.ConsultPayRequest import ConsultPayRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
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
**200** | Payment consultation request sent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> create_order(create_order_request) -> CreateOrderResponse 

Create Payment Order

Create an order to process a payment through DANA Payment Gateway

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH
* ENV

```python
from dana.payment_gateway.v1.models.create_order_by_api_request import CreateOrderByApiRequest
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
    )
)

with ApiClient(configuration) as api_client:
    api_instance = PaymentGatewayApi(api_client)
    create_order_request = CreateOrderByApiRequest()

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
 **create_order_request** | [**CreateOrderByApiRequest**](PaymentGateway/CreateOrderByApiRequest.md) or [**CreateOrderByRedirectRequest**](PaymentGateway/CreateOrderByRedirectRequest.md)|  | 

### Return type

[**CreateOrderResponse**](PaymentGateway/CreateOrderResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order creation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_payment**
> query_payment(query_payment_request) -> QueryPaymentResponse 

Query Payment

Inquiry payment status and information from merchant’s platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.QueryPaymentRequest import QueryPaymentRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
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

Refund Order API

This API is used to refund the order from merchant's platform to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH

```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1 import PaymentGatewayApi
from dana.payment_gateway.v1.models.RefundOrderRequest import RefundOrderRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

