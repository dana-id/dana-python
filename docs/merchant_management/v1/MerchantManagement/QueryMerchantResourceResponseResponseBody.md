# QueryMerchantResourceResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**merchant_resource_informations** | [**List[MerchantResourceInformation]**](MerchantResourceInformation.md) | Merchant resource information list - will be filled if success | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_resource_response_response_body import QueryMerchantResourceResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantResourceResponseResponseBody from a JSON string
query_merchant_resource_response_response_body_instance = QueryMerchantResourceResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantResourceResponseResponseBody.to_json())

# convert the object into a dict
query_merchant_resource_response_response_body_dict = query_merchant_resource_response_response_body_instance.to_dict()
# create an instance of QueryMerchantResourceResponseResponseBody from a dict
query_merchant_resource_response_response_body_from_dict = QueryMerchantResourceResponseResponseBody.from_dict(query_merchant_resource_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


