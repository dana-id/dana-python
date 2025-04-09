# OrderApiObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_title** | **str** |  | 
**merchant_trans_type** | **str** |  | [optional] 
**buyer** | [**Buyer**](Buyer.md) |  | 
**goods** | [**List[Goods]**](Goods.md) |  | [optional] 
**shipping_info** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 
**extend_info** | **str** |  | [optional] 
**scenario** | **str** |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.order_api_object import OrderApiObject

# TODO update the JSON string below
json = "{}"
# create an instance of OrderApiObject from a JSON string
order_api_object_instance = OrderApiObject.from_json(json)
# print the JSON string representation of the object
print(OrderApiObject.to_json())

# convert the object into a dict
order_api_object_dict = order_api_object_instance.to_dict()
# create an instance of OrderApiObject from a dict
order_api_object_from_dict = OrderApiObject.from_dict(order_api_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


