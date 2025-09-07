# FinishNotifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on DANA system | 
**original_reference_no** | **str** | Original transaction identifier on partner system | 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**merchant_id** | **str** | Unique identifier per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | 
**latest_transaction_status** | **str** | Transaction status code:<br /> - 00 &#x3D; Success, the order has been paid<br /> - 05 &#x3D; Cancelled, the order has been closed because it is expired<br />  | 
**transaction_status_desc** | **str** | Description of transaction status | [optional] 
**created_time** | **str** | Transaction created time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**finished_time** | **str** | Transaction finished time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**additional_info** | [**FinishNotifyRequestAdditionalInfo**](FinishNotifyRequestAdditionalInfo.md) | Additional information | [optional] 

## Example

```python
from dana.webhook.finish_notify_request import FinishNotifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotifyRequest from a JSON string
finish_notify_request_instance = FinishNotifyRequest.from_json(json)
# print the JSON string representation of the object
print(FinishNotifyRequest.to_json())

# convert the object into a dict
finish_notify_request_dict = finish_notify_request_instance.to_dict()
# create an instance of FinishNotifyRequest from a dict
finish_notify_request_from_dict = FinishNotifyRequest.from_dict(finish_notify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


