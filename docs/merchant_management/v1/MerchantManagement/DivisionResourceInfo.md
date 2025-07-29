# DivisionResourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**division_id** | **str** | Division identifier | [optional] 
**merchant_id** | **str** | Merchant identifier | [optional] 
**parent_role_type** | **str** | Parent role type | [optional] 
**contact_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**division_description** | **str** | Division description | [optional] 
**division_type** | **str** | Division type | [optional] 
**division_name** | **str** | Division name | [optional] 
**external_division_id** | **str** | External division identifier | [optional] 
**pg_division_flag** | **str** | Flag if division is type PG | [optional] 

## Example

```python
from dana.merchant_management.v1.models.division_resource_info import DivisionResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DivisionResourceInfo from a JSON string
division_resource_info_instance = DivisionResourceInfo.from_json(json)
# print the JSON string representation of the object
print(DivisionResourceInfo.to_json())

# convert the object into a dict
division_resource_info_dict = division_resource_info_instance.to_dict()
# create an instance of DivisionResourceInfo from a dict
division_resource_info_from_dict = DivisionResourceInfo.from_dict(division_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


