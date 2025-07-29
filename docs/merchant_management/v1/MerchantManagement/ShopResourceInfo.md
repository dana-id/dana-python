# ShopResourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier | [optional] 
**parent_division_id** | **str** | Parent division identifier | [optional] 
**parent_role_type** | **str** | Parent role type | [optional] 
**main_name** | **str** | Shop name | [optional] 
**size_type** | **str** | Size type | [optional] 
**shop_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**external_shop_id** | **str** | External shop identifier | [optional] 
**logo_url_map** | **Dict[str, str]** | Logo URL map with base64 encoded images | [optional] 
**ext_info** | **object** | Extended information | [optional] 
**ln** | **str** | Longitude | [optional] 
**lat** | **str** | Latitude | [optional] 
**nmid** | **str** | Network merchant identifier | [optional] 

## Example

```python
from dana.merchant_management.v1.models.shop_resource_info import ShopResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShopResourceInfo from a JSON string
shop_resource_info_instance = ShopResourceInfo.from_json(json)
# print the JSON string representation of the object
print(ShopResourceInfo.to_json())

# convert the object into a dict
shop_resource_info_dict = shop_resource_info_instance.to_dict()
# create an instance of ShopResourceInfo from a dict
shop_resource_info_from_dict = ShopResourceInfo.from_dict(shop_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


