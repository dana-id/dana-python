# CreateOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/243#paymentgatewayprod-paymentRedirect-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/243#paymentgatewayprod-paymentRedirect-ResponseCodeandMessage | 
**reference_no** | **str** | Transaction identifier on DANA system. Present if successfully processed | [optional] 
**partner_reference_no** | **str** | Transaction identifier on partner system | 
**web_redirect_url** | **str** | Checkout URLs. Present if successfully processed and payment method is not OVO/Virtual Account/QRIS | [optional] 
**additional_info** | [**CreateOrderResponseAdditionalInfo**](CreateOrderResponseAdditionalInfo.md) | Additional information | [optional] 
**external_order_id** | **str** | External order identifier | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.create_order_response import CreateOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponse from a JSON string
create_order_response_instance = CreateOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponse.to_json())

# convert the object into a dict
create_order_response_dict = create_order_response_instance.to_dict()
# create an instance of CreateOrderResponse from a dict
create_order_response_from_dict = CreateOrderResponse.from_dict(create_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


