# PaymentView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_request_id** | **str** | Cashier request identifier | [optional] 
**paid_time** | **str** | Information of paid time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**pay_option_infos** | [**List[PayOptionInfo]**](PayOptionInfo.md) | Information of pay option | 
**pay_request_extend_info** | **str** | Extend information of pay request | [optional] 
**extend_info** | **str** | Extend information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.payment_view import PaymentView

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentView from a JSON string
payment_view_instance = PaymentView.from_json(json)
# print the JSON string representation of the object
print(PaymentView.to_json())

# convert the object into a dict
payment_view_dict = payment_view_instance.to_dict()
# create an instance of PaymentView from a dict
payment_view_from_dict = PaymentView.from_dict(payment_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


