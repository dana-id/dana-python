# PayOptionAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | [optional] 
**payment_code** | **str** |  | [optional] 
**promo_infos** | [**List[PromoInfo]**](PromoInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.pay_option_additional_info import PayOptionAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionAdditionalInfo from a JSON string
pay_option_additional_info_instance = PayOptionAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(PayOptionAdditionalInfo.to_json())

# convert the object into a dict
pay_option_additional_info_dict = pay_option_additional_info_instance.to_dict()
# create an instance of PayOptionAdditionalInfo from a dict
pay_option_additional_info_from_dict = PayOptionAdditionalInfo.from_dict(pay_option_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


