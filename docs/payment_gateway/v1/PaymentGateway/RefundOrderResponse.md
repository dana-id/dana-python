# RefundOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/127#HTML-API-RefundOrder-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/127#HTML-API-RefundOrder-ResponseCodeandMessage | 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**original_capture_no** | **str** | DANA&#39;s capture identifier. Use to refund the corresponding capture order | [optional] 
**refund_no** | **str** | Refund number identifier on DANA system | [optional] 
**partner_refund_no** | **str** | Reference number from merchant for the refund | 
**refund_amount** | [**Money**](Money.md) | Refund amount. Contains two sub-fields - 1. Value (Amount, including the cents) and 2. Currency (Currency code based on ISO) | 
**refund_time** | **str** | Refund time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.refund_order_response import RefundOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrderResponse from a JSON string
refund_order_response_instance = RefundOrderResponse.from_json(json)
# print the JSON string representation of the object
print(RefundOrderResponse.to_json())

# convert the object into a dict
refund_order_response_dict = refund_order_response_instance.to_dict()
# create an instance of RefundOrderResponse from a dict
refund_order_response_from_dict = RefundOrderResponse.from_dict(refund_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


