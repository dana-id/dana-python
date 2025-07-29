# QueryMerchantResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryMerchantResourceResponseResponse**](QueryMerchantResourceResponseResponse.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_resource_response import QueryMerchantResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantResourceResponse from a JSON string
query_merchant_resource_response_instance = QueryMerchantResourceResponse.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantResourceResponse.to_json())

# convert the object into a dict
query_merchant_resource_response_dict = query_merchant_resource_response_instance.to_dict()
# create an instance of QueryMerchantResourceResponse from a dict
query_merchant_resource_response_from_dict = QueryMerchantResourceResponse.from_dict(query_merchant_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


