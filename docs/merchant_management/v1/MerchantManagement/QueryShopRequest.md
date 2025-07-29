# QueryShopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier. Required when shopIdType is EXTERNAL_ID | [optional] 
**shop_id** | **str** | Shop identifier. Length depends on shopIdType - INNER_ID (21 max), EXTERNAL_ID (64 max) | 
**shop_id_type** | **str** | Shop identifier type | 

## Example

```python
from dana.merchant_management.v1.models.query_shop_request import QueryShopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryShopRequest from a JSON string
query_shop_request_instance = QueryShopRequest.from_json(json)
# print the JSON string representation of the object
print(QueryShopRequest.to_json())

# convert the object into a dict
query_shop_request_dict = query_shop_request_instance.to_dict()
# create an instance of QueryShopRequest from a dict
query_shop_request_from_dict = QueryShopRequest.from_dict(query_shop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


