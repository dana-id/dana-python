# CancelOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**reason** | **str** | Cancellation reason | [optional] 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub fields - Value (Transaction amount, including the cents) and Currency (Currency code based on ISO 4217) | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.cancel_order_request import CancelOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderRequest from a JSON string
cancel_order_request_instance = CancelOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CancelOrderRequest.to_json())

# convert the object into a dict
cancel_order_request_dict = cancel_order_request_instance.to_dict()
# create an instance of CancelOrderRequest from a dict
cancel_order_request_from_dict = CancelOrderRequest.from_dict(cancel_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


