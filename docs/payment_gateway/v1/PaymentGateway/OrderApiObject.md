# OrderApiObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_title** | **str** | Additional information of order title | 
**merchant_trans_type** | **str** | Additional information of merchant transaction type | [optional] 
**buyer** | [**Buyer**](Buyer.md) | Additional information of buyer | [optional] 
**goods** | [**List[Goods]**](Goods.md) | Additional information of goods | [optional] 
**shipping_info** | [**List[ShippingInfo]**](ShippingInfo.md) | Additional information of shipping info | [optional] 
**extend_info** | **str** | Additional information of extend | [optional] 
**created_time** | **str** | Additional information of created time | [optional] 
**order_memo** | **str** | Additional information of order | [optional] 
**scenario** | **str** | For Payment Gateway scenario, need to fill it as API | [optional] 

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


