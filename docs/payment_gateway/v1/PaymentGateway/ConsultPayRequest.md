# ConsultPayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | 
**additional_info** | [**ConsultPayRequestAdditionalInfo**](ConsultPayRequestAdditionalInfo.md) | Additional information | 

## Example

```python
from dana.payment_gateway.v1.models.consult_pay_request import ConsultPayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayRequest from a JSON string
consult_pay_request_instance = ConsultPayRequest.from_json(json)
# print the JSON string representation of the object
print(ConsultPayRequest.to_json())

# convert the object into a dict
consult_pay_request_dict = consult_pay_request_instance.to_dict()
# create an instance of ConsultPayRequest from a dict
consult_pay_request_from_dict = ConsultPayRequest.from_dict(consult_pay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


