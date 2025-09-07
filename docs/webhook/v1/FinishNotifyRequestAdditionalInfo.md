# FinishNotifyRequestAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_info** | [**FinishNotifyPaymentInfo**](FinishNotifyPaymentInfo.md) | Additional information of payment | [optional] 
**shop_info** | [**ShopInfo**](ShopInfo.md) | Additional information of shop | [optional] 
**extend_info** | **str** | Additional information of extend (As a JSON string) | [optional] 
**extend_info_closed_reason** | **str** | Additional information of closed reason. Required if order is closed | [optional] 

## Example

```python
from dana.webhook.finish_notify_request_additional_info import FinishNotifyRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotifyRequestAdditionalInfo from a JSON string
finish_notify_request_additional_info_instance = FinishNotifyRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(FinishNotifyRequestAdditionalInfo.to_json())

# convert the object into a dict
finish_notify_request_additional_info_dict = finish_notify_request_additional_info_instance.to_dict()
# create an instance of FinishNotifyRequestAdditionalInfo from a dict
finish_notify_request_additional_info_from_dict = FinishNotifyRequestAdditionalInfo.from_dict(finish_notify_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


