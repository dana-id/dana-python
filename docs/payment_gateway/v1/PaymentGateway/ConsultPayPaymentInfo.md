# ConsultPayPaymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** |  | 
**pay_option** | **str** |  | [optional] 
**promo_infos** | [**List[PromoInfo]**](PromoInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.consult_pay_payment_info import ConsultPayPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayPaymentInfo from a JSON string
consult_pay_payment_info_instance = ConsultPayPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(ConsultPayPaymentInfo.to_json())

# convert the object into a dict
consult_pay_payment_info_dict = consult_pay_payment_info_instance.to_dict()
# create an instance of ConsultPayPaymentInfo from a dict
consult_pay_payment_info_from_dict = ConsultPayPaymentInfo.from_dict(consult_pay_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


