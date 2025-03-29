# ConsultPayRequestAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of amount. Following ISO-4217, for IDR the value includes 2 decimal digits separated with point e.g. IDR 10.000,- will be placed with 10000.00 | 
**currency** | **str** | Currency of money following ISO-4217 | 

## Example

```python
from dana_python.payment_gateway.payment_gateway.models.consult_pay_request_amount import ConsultPayRequestAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayRequestAmount from a JSON string
consult_pay_request_amount_instance = ConsultPayRequestAmount.from_json(json)
# print the JSON string representation of the object
print(ConsultPayRequestAmount.to_json())

# convert the object into a dict
consult_pay_request_amount_dict = consult_pay_request_amount_instance.to_dict()
# create an instance of ConsultPayRequestAmount from a dict
consult_pay_request_amount_from_dict = ConsultPayRequestAmount.from_dict(consult_pay_request_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


