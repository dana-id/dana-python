# PaymentGatewayApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**consult_pay**](PaymentGatewayApi.md#consult_pay) | **POST** /v1.0/payment-gateway/consult-pay.htm | Consult Pay API
[**create_order**](PaymentGatewayApi.md#create_order) | **POST** /v1.0/payment-gateway/create-order.htm | Create Payment Order

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
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1.models.consult_pay_request import ConsultPayRequest
from dana.payment_gateway.v1.models.consult_pay_response import ConsultPayResponse
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
    api_instance = dana.payment_gateway.v1.PaymentGatewayApi(api_client)
    consult_pay_request = dana.payment_gateway.v1.ConsultPayRequest()

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

```python
from dana.payment_gateway.v1.models.create_order_by_redirect_request import CreateOrderByRedirectRequest
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.payment_gateway.v1.models.create_order_response import CreateOrderResponse
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
    api_instance = dana.payment_gateway.v1.PaymentGatewayApi(api_client)
    create_order_request = dana.payment_gateway.v1.CreateOrderByRedirectRequest()

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
**200** | Order creation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

