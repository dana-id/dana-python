# MerchantContactMobileNo

Contact mobile number (`contactMobileNo` in merchantInformation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_no** | **str** | Mobile phone number | [optional] 
**is_verified** | **str** | Whether the mobile number is verified (API may return true/false or TRUE/FALSE) | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_contact_mobile_no import MerchantContactMobileNo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantContactMobileNo from a JSON string
merchant_contact_mobile_no_instance = MerchantContactMobileNo.from_json(json)
# print the JSON string representation of the object
print(MerchantContactMobileNo.to_json())

# convert the object into a dict
merchant_contact_mobile_no_dict = merchant_contact_mobile_no_instance.to_dict()
# create an instance of MerchantContactMobileNo from a dict
merchant_contact_mobile_no_from_dict = MerchantContactMobileNo.from_dict(merchant_contact_mobile_no_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


