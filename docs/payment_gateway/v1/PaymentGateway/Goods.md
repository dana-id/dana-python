# Goods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Goods unit | [optional] 
**category** | **str** | Goods category | 
**price** | [**Money**](Money.md) |  | 
**merchant_shipping_id** | **str** | Shipment identifier provided by merchant | [optional] 
**merchant_goods_id** | **str** | Goods identifier provided by merchant | 
**description** | **str** | Goods description | 
**snapshot_url** | **str** | The URL of good’s snapshot web page | [optional] 
**quantity** | **str** | Count of items | 
**extend_info** | **str** | Extend information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.goods import Goods

# TODO update the JSON string below
json = "{}"
# create an instance of Goods from a JSON string
goods_instance = Goods.from_json(json)
# print the JSON string representation of the object
print(Goods.to_json())

# convert the object into a dict
goods_dict = goods_instance.to_dict()
# create an instance of Goods from a dict
goods_from_dict = Goods.from_dict(goods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


