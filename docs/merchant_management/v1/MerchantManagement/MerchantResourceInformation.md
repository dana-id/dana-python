# MerchantResourceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Type of merchant resource | 
**value** | **str** | JSON string containing amount and currency information | 

## Example

```python
from dana.merchant_management.v1.models.merchant_resource_information import MerchantResourceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantResourceInformation from a JSON string
merchant_resource_information_instance = MerchantResourceInformation.from_json(json)
# print the JSON string representation of the object
print(MerchantResourceInformation.to_json())

# convert the object into a dict
merchant_resource_information_dict = merchant_resource_information_instance.to_dict()
# create an instance of MerchantResourceInformation from a dict
merchant_resource_information_from_dict = MerchantResourceInformation.from_dict(merchant_resource_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


