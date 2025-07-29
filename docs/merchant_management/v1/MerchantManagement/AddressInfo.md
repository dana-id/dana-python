# AddressInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country | [optional] 
**province** | **str** | Province | [optional] 
**city** | **str** | City | [optional] 
**area** | **str** | Area | [optional] 
**address1** | **str** | Primary address line | [optional] 
**address2** | **str** | Secondary address line | [optional] 
**postcode** | **str** | Postal code | [optional] 
**sub_district** | **str** | Sub district | [optional] 

## Example

```python
from dana.merchant_management.v1.models.address_info import AddressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInfo from a JSON string
address_info_instance = AddressInfo.from_json(json)
# print the JSON string representation of the object
print(AddressInfo.to_json())

# convert the object into a dict
address_info_dict = address_info_instance.to_dict()
# create an instance of AddressInfo from a dict
address_info_from_dict = AddressInfo.from_dict(address_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


