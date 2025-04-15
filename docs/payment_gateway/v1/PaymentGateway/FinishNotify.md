# FinishNotify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on DANA system | 
**original_reference_no** | **str** | Original transaction identifier on partner system | 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**merchant_id** | **str** | Unique identifier for each merchant | 
**sub_merchant_id** | **str** | Sub merchant identifier | [optional] 
**amount** | [**Money**](Money.md) |  | 
**latest_transaction_status** | **str** | Transaction status code:<br /> - 00 &#x3D; Success<br /> - 05 &#x3D; Cancelled (expired)<br />  | 
**transaction_status_desc** | **str** | Description of transaction status | [optional] 
**created_time** | **str** | Transaction creation time (GMT+7, Jakarta) | 
**finished_time** | **str** | Transaction completion time (GMT+7, Jakarta) | 
**external_store_id** | **str** | Store identifier | [optional] 
**additional_info** | [**PushNotifyAdditionalInfo**](PushNotifyAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.finish_notify import FinishNotify

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotify from a JSON string
finish_notify_instance = FinishNotify.from_json(json)
# print the JSON string representation of the object
print(FinishNotify.to_json())

# convert the object into a dict
finish_notify_dict = finish_notify_instance.to_dict()
# create an instance of FinishNotify from a dict
finish_notify_from_dict = FinishNotify.from_dict(finish_notify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


