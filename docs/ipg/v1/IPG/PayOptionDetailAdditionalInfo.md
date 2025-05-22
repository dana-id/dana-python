# PayOptionDetailAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topup_and_pay** | **bool** | Top up and pay | [optional] 
**payer_account_no** | **str** | Number account of payer | [optional] 
**save_card_after_pay** | **bool** | Information save card after payment process | [optional] 
**channel_info** | **str** | Information of channel | [optional] 
**issuing_country** | **str** | Information of issuing country | [optional] 
**asset_type** | **str** | Type of asset | [optional] 
**extend_info** | **str** | Extend information | [optional] 

## Example

```python
from dana.ipg.v1.models.pay_option_detail_additional_info import PayOptionDetailAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionDetailAdditionalInfo from a JSON string
pay_option_detail_additional_info_instance = PayOptionDetailAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(PayOptionDetailAdditionalInfo.to_json())

# convert the object into a dict
pay_option_detail_additional_info_dict = pay_option_detail_additional_info_instance.to_dict()
# create an instance of PayOptionDetailAdditionalInfo from a dict
pay_option_detail_additional_info_from_dict = PayOptionDetailAdditionalInfo.from_dict(pay_option_detail_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


