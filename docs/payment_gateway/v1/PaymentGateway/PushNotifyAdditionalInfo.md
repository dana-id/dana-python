# PushNotifyAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_info** | [**PushNotifyPaymentInfo**](PushNotifyPaymentInfo.md) |  | [optional] 
**shop_info** | **object** | Additional information of shop | [optional] 
**extend_info** | **str** | Extended information (as a JSON string) | [optional] 
**extend_info_closed_reason** | **str** | Reason for order closure (if order is closed) | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.push_notify_additional_info import PushNotifyAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotifyAdditionalInfo from a JSON string
push_notify_additional_info_instance = PushNotifyAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(PushNotifyAdditionalInfo.to_json())

# convert the object into a dict
push_notify_additional_info_dict = push_notify_additional_info_instance.to_dict()
# create an instance of PushNotifyAdditionalInfo from a dict
push_notify_additional_info_from_dict = PushNotifyAdditionalInfo.from_dict(push_notify_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


