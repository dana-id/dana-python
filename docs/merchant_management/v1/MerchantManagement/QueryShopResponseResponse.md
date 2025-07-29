# QueryShopResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryShopResponseResponseHead**](QueryShopResponseResponseHead.md) |  | 
**body** | [**QueryShopResponseResponseBody**](QueryShopResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.query_shop_response_response import QueryShopResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryShopResponseResponse from a JSON string
query_shop_response_response_instance = QueryShopResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryShopResponseResponse.to_json())

# convert the object into a dict
query_shop_response_response_dict = query_shop_response_response_instance.to_dict()
# create an instance of QueryShopResponseResponse from a dict
query_shop_response_response_from_dict = QueryShopResponseResponse.from_dict(query_shop_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


