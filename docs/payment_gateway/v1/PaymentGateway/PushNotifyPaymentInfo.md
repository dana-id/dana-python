# PushNotifyPaymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_request_id** | **str** | Cashier request identifier | 
**paid_time** | **str** | Time of paid transaction (format in YYYY-MM-DDTHH:mm:ss+07:00) | 
**pay_option_infos** | [**List[PayOptionInfo]**](PayOptionInfo.md) | Information of pay options | 
**pay_request_extend_info** | **str** | Extend information of pay request | [optional] 
**extend_info** | **str** | Additional extended information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.push_notify_payment_info import PushNotifyPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotifyPaymentInfo from a JSON string
push_notify_payment_info_instance = PushNotifyPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(PushNotifyPaymentInfo.to_json())

# convert the object into a dict
push_notify_payment_info_dict = push_notify_payment_info_instance.to_dict()
# create an instance of PushNotifyPaymentInfo from a dict
push_notify_payment_info_from_dict = PushNotifyPaymentInfo.from_dict(push_notify_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


