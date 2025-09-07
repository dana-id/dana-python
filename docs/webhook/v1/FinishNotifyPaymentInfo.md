# FinishNotifyPaymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_request_id** | **str** | Cashier request identifier | 
**paid_time** | **str** | Information of paid time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**pay_option_infos** | [**List[PayOptionInfo]**](PayOptionInfo.md) | Information of pay option. Refer to payOptionInfos for the detailed | 
**pay_request_extend_info** | **str** | Extend information of pay request | [optional] 
**extend_info** | **str** | Extend information | [optional] 

## Example

```python
from dana.webhook.finish_notify_payment_info import FinishNotifyPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotifyPaymentInfo from a JSON string
finish_notify_payment_info_instance = FinishNotifyPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(FinishNotifyPaymentInfo.to_json())

# convert the object into a dict
finish_notify_payment_info_dict = finish_notify_payment_info_instance.to_dict()
# create an instance of FinishNotifyPaymentInfo from a dict
finish_notify_payment_info_from_dict = FinishNotifyPaymentInfo.from_dict(finish_notify_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


