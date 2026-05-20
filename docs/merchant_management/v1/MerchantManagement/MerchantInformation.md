# MerchantInformation

Merchant profile detail (`merchantInformation` in response body)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number | [optional] 
**merchant_id** | **str** | Merchant identifier | [optional] 
**merchant_type** | **str** | Merchant type | [optional] 
**merchant_sub_type** | **str** | Merchant sub type | [optional] 
**mcc_codes** | **List[str]** | Merchant category codes (MCC) | [optional] 
**logo_url** | **str** | Logo URL | [optional] 
**logo_url_map** | **Dict[str, str]** | Logo map. Keys may be &#x60;LOGO&#x60;, &#x60;PC_LOGO&#x60;, &#x60;MOBILE_LOGO&#x60;. Values are base64-encoded PNG image data.  | [optional] 
**short_name_code** | **str** | Merchant short name code | [optional] 
**official_name** | **str** | Merchant official name | [optional] 
**english_name** | **str** | Merchant English name | [optional] 
**local_name** | **str** | Merchant local (Indonesian) name | [optional] 
**certificate** | [**MerchantCertificateInfo**](MerchantCertificateInfo.md) |  | [optional] 
**registered_address** | [**MerchantContactAddress**](MerchantContactAddress.md) |  | [optional] 
**business_address** | [**MerchantContactAddress**](MerchantContactAddress.md) |  | [optional] 
**office_telephone** | **str** | Merchant official telephone number | [optional] 
**fax_telephone** | **str** | Merchant official fax telephone number | [optional] 
**corporate_official_name** | [**UserName**](UserName.md) |  | [optional] 
**corporate_certificate** | [**MerchantCorporateCertificate**](MerchantCorporateCertificate.md) |  | [optional] 
**contact_official_name** | [**UserName**](UserName.md) |  | [optional] 
**contact_mobile_no** | [**MerchantContactMobileNo**](MerchantContactMobileNo.md) |  | [optional] 
**contact_telephone** | **str** | Contact telephone number | [optional] 
**contact_email** | [**MerchantContactEmail**](MerchantContactEmail.md) |  | [optional] 
**created_time** | **str** | Merchant creation time, YYYY-MM-DDTHH:mm:ss+07:00 (GMT+7) | [optional] 
**modified_time** | **str** | Merchant last modified time, YYYY-MM-DDTHH:mm:ss+07:00 (GMT+7) | [optional] 
**merchant_status** | **str** | Merchant status | [optional] 
**register_source** | **str** | Registered source platform | [optional] 
**size_type** | **str** | Size type | [optional] 
**platform_mid** | **str** | Merchant platform identifier | [optional] 
**tax_no** | **str** | Tax number (NPWP), 15 digits | [optional] 
**accounts** | [**List[MerchantAccountInfo]**](MerchantAccountInfo.md) | Merchant account list (present when &#x60;isQueryAccount&#x60; is true in request) | [optional] 
**brand_name** | **str** | Brand name on legal name or tax name | [optional] 
**tax_address** | [**MerchantContactAddress**](MerchantContactAddress.md) |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_information import MerchantInformation

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInformation from a JSON string
merchant_information_instance = MerchantInformation.from_json(json)
# print the JSON string representation of the object
print(MerchantInformation.to_json())

# convert the object into a dict
merchant_information_dict = merchant_information_instance.to_dict()
# create an instance of MerchantInformation from a dict
merchant_information_from_dict = MerchantInformation.from_dict(merchant_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


