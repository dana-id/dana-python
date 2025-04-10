# OrderRedirectObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_title** | **str** |  | 
**merchant_trans_type** | **str** |  | [optional] 
**buyer** | [**Buyer**](Buyer.md) |  | 
**goods** | [**List[Goods]**](Goods.md) |  | [optional] 
**shipping_info** | [**List[ShippingInfo]**](ShippingInfo.md) |  | [optional] 
**extend_info** | **str** |  | [optional] 
**scenario** | **str** |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.order_redirect_object import OrderRedirectObject

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRedirectObject from a JSON string
order_redirect_object_instance = OrderRedirectObject.from_json(json)
# print the JSON string representation of the object
print(OrderRedirectObject.to_json())

# convert the object into a dict
order_redirect_object_dict = order_redirect_object_instance.to_dict()
# create an instance of OrderRedirectObject from a dict
order_redirect_object_from_dict = OrderRedirectObject.from_dict(order_redirect_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


