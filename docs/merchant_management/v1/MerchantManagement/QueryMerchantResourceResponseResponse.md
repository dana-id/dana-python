# QueryMerchantResourceResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryMerchantResourceResponseResponseHead**](QueryMerchantResourceResponseResponseHead.md) |  | 
**body** | [**QueryMerchantResourceResponseResponseBody**](QueryMerchantResourceResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_resource_response_response import QueryMerchantResourceResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantResourceResponseResponse from a JSON string
query_merchant_resource_response_response_instance = QueryMerchantResourceResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantResourceResponseResponse.to_json())

# convert the object into a dict
query_merchant_resource_response_response_dict = query_merchant_resource_response_response_instance.to_dict()
# create an instance of QueryMerchantResourceResponseResponse from a dict
query_merchant_resource_response_response_from_dict = QueryMerchantResourceResponseResponse.from_dict(query_merchant_resource_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


