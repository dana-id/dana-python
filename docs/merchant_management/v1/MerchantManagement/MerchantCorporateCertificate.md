# MerchantCorporateCertificate

Corporate certificate (`corporateCertificate` in merchantInformation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_no** | **str** | Certificate number | [optional] 
**certificate_type** | **str** | Type of certificate | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_corporate_certificate import MerchantCorporateCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCorporateCertificate from a JSON string
merchant_corporate_certificate_instance = MerchantCorporateCertificate.from_json(json)
# print the JSON string representation of the object
print(MerchantCorporateCertificate.to_json())

# convert the object into a dict
merchant_corporate_certificate_dict = merchant_corporate_certificate_instance.to_dict()
# create an instance of MerchantCorporateCertificate from a dict
merchant_corporate_certificate_from_dict = MerchantCorporateCertificate.from_dict(merchant_corporate_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


