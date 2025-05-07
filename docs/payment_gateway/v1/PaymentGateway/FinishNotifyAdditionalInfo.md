# FinishNotifyAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_info** | [**FinishNotifyPaymentInfo**](FinishNotifyPaymentInfo.md) |  | [optional] 
**shop_info** | **object** | Additional information of shop | [optional] 
**extend_info** | **str** | Extended information (as a JSON string) | [optional] 
**extend_info_closed_reason** | **str** | Reason for order closure (if order is closed) | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.finish_notify_additional_info import FinishNotifyAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotifyAdditionalInfo from a JSON string
finish_notify_additional_info_instance = FinishNotifyAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(FinishNotifyAdditionalInfo.to_json())

# convert the object into a dict
finish_notify_additional_info_dict = finish_notify_additional_info_instance.to_dict()
# create an instance of FinishNotifyAdditionalInfo from a dict
finish_notify_additional_info_from_dict = FinishNotifyAdditionalInfo.from_dict(finish_notify_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


