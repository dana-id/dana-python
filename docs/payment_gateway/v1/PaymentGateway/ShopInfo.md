# ShopInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **str** | Shop identifier (required if externalShopId is blank) | [optional] 
**external_shop_id** | **str** | External shop identifier (required if shopId is blank) | [optional] 
**operator_id** | **str** | Operator identifier | [optional] 
**shop_address** | **str** | Shop address | [optional] 
**division_id** | **str** | Division identifier | [optional] 
**external_division_id** | **str** | External division identifier | [optional] 
**division_type** | **str** | Division type | [optional] 
**shop_name** | **str** | Shop name | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.shop_info import ShopInfo

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


