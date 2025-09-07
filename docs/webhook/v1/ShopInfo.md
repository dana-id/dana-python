# ShopInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **str** | Information of shop identifier. Required if externalShopId is blank | [optional] 
**external_shop_id** | **str** | Information of external shop identifier. Required if shopId is blank | [optional] 
**operator_id** | **str** | Information of operator identifier | [optional] 
**shop_address** | **str** | Information of shop address | [optional] 
**division_id** | **str** | Information of division identifier | [optional] 
**external_division_id** | **str** | Information of external division identifier | [optional] 
**division_type** | **str** | Information of division type | [optional] 
**shop_name** | **str** | Information of shop name | [optional] 

## Example

```python
from dana.webhook.shop_info import ShopInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShopInfo from a JSON string
shop_info_instance = ShopInfo.from_json(json)
# print the JSON string representation of the object
print(ShopInfo.to_json())

# convert the object into a dict
shop_info_dict = shop_info_instance.to_dict()
# create an instance of ShopInfo from a dict
shop_info_from_dict = ShopInfo.from_dict(shop_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


