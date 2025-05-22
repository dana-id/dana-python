# ConsultPayRequestAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | [**Buyer**](Buyer.md) | Additional information of buyer | 
**env_info** | [**EnvInfo**](EnvInfo.md) | Additional information of environment info | 
**merchant_trans_type** | **str** | Additional information of merchant transaction type | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.consult_pay_request_additional_info import ConsultPayRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayRequestAdditionalInfo from a JSON string
consult_pay_request_additional_info_instance = ConsultPayRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ConsultPayRequestAdditionalInfo.to_json())

# convert the object into a dict
consult_pay_request_additional_info_dict = consult_pay_request_additional_info_instance.to_dict()
# create an instance of ConsultPayRequestAdditionalInfo from a dict
consult_pay_request_additional_info_from_dict = ConsultPayRequestAdditionalInfo.from_dict(consult_pay_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


