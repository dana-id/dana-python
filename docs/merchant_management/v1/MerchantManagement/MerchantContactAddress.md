# MerchantContactAddress

Merchant contact address (`registeredAddress`, `businessAddress`, `taxAddress`)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**country** | **str** | Country name | [optional] 
**province** | **str** | Province name | [optional] 
**city** | **str** | City name | [optional] 
**area** | **str** | Area name | [optional] 
**zipcode** | **str** | Zipcode | [optional] 
**contact_address_type** | **str** | Contact address type | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_contact_address import MerchantContactAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantContactAddress from a JSON string
merchant_contact_address_instance = MerchantContactAddress.from_json(json)
# print the JSON string representation of the object
print(MerchantContactAddress.to_json())

# convert the object into a dict
merchant_contact_address_dict = merchant_contact_address_instance.to_dict()
# create an instance of MerchantContactAddress from a dict
merchant_contact_address_from_dict = MerchantContactAddress.from_dict(merchant_contact_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


