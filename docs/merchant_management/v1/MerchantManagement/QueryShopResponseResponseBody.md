# QueryShopResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**shop_resource_info** | [**ShopResourceInfo**](ShopResourceInfo.md) |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_shop_response_response_body import QueryShopResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryShopResponseResponseBody from a JSON string
query_shop_response_response_body_instance = QueryShopResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryShopResponseResponseBody.to_json())

# convert the object into a dict
query_shop_response_response_body_dict = query_shop_response_response_body_instance.to_dict()
# create an instance of QueryShopResponseResponseBody from a dict
query_shop_response_response_body_from_dict = QueryShopResponseResponseBody.from_dict(query_shop_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


