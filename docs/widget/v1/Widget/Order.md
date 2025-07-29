# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | [**Buyer**](Buyer.md) |  | [optional] 
**seller** | [**Seller**](Seller.md) |  | [optional] 
**order_title** | **str** | Additional information of order title | 
**merchant_trans_type** | **str** | Additional information of merchant transaction type | [optional] 
**order_memo** | **str** | Additional information of order memo | [optional] 
**created_time** | **str** | Additional information of created time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**goods** | [**List[Goods]**](Goods.md) |  | [optional] 
**shipping_info** | [**List[ShippingInfo]**](ShippingInfo.md) | Additional information of shipping | [optional] 
**international_order_info** | [**InternationalOrderInfo**](InternationalOrderInfo.md) | Additional information of international order. Only use for Mini Program service | [optional] 
**extend_info** | **str** | Additional information of extend | [optional] 

## Example

```python
from dana.widget.v1.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


