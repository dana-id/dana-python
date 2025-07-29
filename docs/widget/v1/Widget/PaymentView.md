# PaymentView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_request_id** | **str** | Cashier request identifier | [optional] 
**paid_time** | **str** | Paid time in format YYYY-MM-DDTHH:mm:ss+07:00 (Jakarta time) | [optional] 
**pay_option_infos** | [**List[PayOptionInfo]**](PayOptionInfo.md) | Information of pay options | [optional] 
**pay_request_extend_info** | **str** | Extend information of pay request | [optional] 
**extend_info** | **str** | Additional extend information | [optional] 

## Example

```python
from dana.widget.v1.models.payment_view import PaymentView

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


