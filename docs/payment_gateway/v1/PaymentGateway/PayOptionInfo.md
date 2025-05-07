# PayOptionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** | Payment method name | 
**pay_option** | **str** | Payment provider name | [optional] 
**pay_amount** | [**Money**](Money.md) |  | [optional] 
**trans_amount** | [**Money**](Money.md) |  | [optional] 
**charge_amount** | [**Money**](Money.md) |  | [optional] 
**pay_option_bill_extend_info** | **str** | Extended bill information for pay option | [optional] 
**extend_info** | **str** | Additional extend information | [optional] 
**payment_code** | **str** | Payment code | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.pay_option_info import PayOptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionInfo from a JSON string
pay_option_info_instance = PayOptionInfo.from_json(json)
# print the JSON string representation of the object
print(PayOptionInfo.to_json())

# convert the object into a dict
pay_option_info_dict = pay_option_info_instance.to_dict()
# create an instance of PayOptionInfo from a dict
pay_option_info_from_dict = PayOptionInfo.from_dict(pay_option_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


