# PayOptionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** |  | 
**pay_option** | **str** |  | 
**trans_amount** | [**Money**](Money.md) |  | 
**fee_amount** | [**Money**](Money.md) |  | [optional] 
**card_token** | **str** |  | [optional] 
**merchant_token** | **str** |  | [optional] 
**additional_info** | [**PayOptionAdditionalInfo**](PayOptionAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.pay_option_details import PayOptionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionDetails from a JSON string
pay_option_details_instance = PayOptionDetails.from_json(json)
# print the JSON string representation of the object
print(PayOptionDetails.to_json())

# convert the object into a dict
pay_option_details_dict = pay_option_details_instance.to_dict()
# create an instance of PayOptionDetails from a dict
pay_option_details_from_dict = PayOptionDetails.from_dict(pay_option_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


