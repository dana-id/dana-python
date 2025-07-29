# QueryShopResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryShopResponseResponse**](QueryShopResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_shop_response import QueryShopResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryShopResponse from a JSON string
query_shop_response_instance = QueryShopResponse.from_json(json)
# print the JSON string representation of the object
print(QueryShopResponse.to_json())

# convert the object into a dict
query_shop_response_dict = query_shop_response_instance.to_dict()
# create an instance of QueryShopResponse from a dict
query_shop_response_from_dict = QueryShopResponse.from_dict(query_shop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


