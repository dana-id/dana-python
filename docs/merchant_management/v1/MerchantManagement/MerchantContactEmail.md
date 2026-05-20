# MerchantContactEmail

Contact email (`contactEmail` in merchantInformation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Merchant contact email | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_contact_email import MerchantContactEmail

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantContactEmail from a JSON string
merchant_contact_email_instance = MerchantContactEmail.from_json(json)
# print the JSON string representation of the object
print(MerchantContactEmail.to_json())

# convert the object into a dict
merchant_contact_email_dict = merchant_contact_email_instance.to_dict()
# create an instance of MerchantContactEmail from a dict
merchant_contact_email_from_dict = MerchantContactEmail.from_dict(merchant_contact_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


