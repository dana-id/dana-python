# RefundOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**original_capture_no** | **str** | DANA&#39;s capture identifier. Use to refund the corresponding capture order | [optional] 
**partner_refund_no** | **str** | Reference number from merchant for the refund | 
**refund_amount** | [**Money**](Money.md) | Refund amount. Contains two sub-fields - 1. Value (Transaction amount, including the cents) and 2. Currency (Currency code based on ISO) | 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**reason** | **str** | Refund reason | [optional] 
**additional_info** | [**RefundOrderRequestAdditionalInfo**](RefundOrderRequestAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.widget.v1.models.refund_order_request import RefundOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrderRequest from a JSON string
refund_order_request_instance = RefundOrderRequest.from_json(json)
# print the JSON string representation of the object
print(RefundOrderRequest.to_json())

# convert the object into a dict
refund_order_request_dict = refund_order_request_instance.to_dict()
# create an instance of RefundOrderRequest from a dict
refund_order_request_from_dict = RefundOrderRequest.from_dict(refund_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


