# MerchantCertificateInfo

Merchant certificate (`certificate` in merchantInformation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_no** | **str** | Certificate number | [optional] 
**certificate_type** | **str** | Certificate type | [optional] 
**certificate_urls** | **List[str]** | Certificate URLs | [optional] 
**certificate_expiry_date** | **str** | Certificate expiry date, in format YYYY-MM-DDTHH:mm:ss+07:00 (GMT+7) | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_certificate_info import MerchantCertificateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCertificateInfo from a JSON string
merchant_certificate_info_instance = MerchantCertificateInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantCertificateInfo.to_json())

# convert the object into a dict
merchant_certificate_info_dict = merchant_certificate_info_instance.to_dict()
# create an instance of MerchantCertificateInfo from a dict
merchant_certificate_info_from_dict = MerchantCertificateInfo.from_dict(merchant_certificate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


