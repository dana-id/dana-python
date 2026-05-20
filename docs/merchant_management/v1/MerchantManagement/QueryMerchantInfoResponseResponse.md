# QueryMerchantInfoResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryMerchantInfoResponseResponseHead**](QueryMerchantInfoResponseResponseHead.md) |  | [optional] 
**body** | [**QueryMerchantInfoResponseResponseBody**](QueryMerchantInfoResponseResponseBody.md) |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_info_response_response import QueryMerchantInfoResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantInfoResponseResponse from a JSON string
query_merchant_info_response_response_instance = QueryMerchantInfoResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantInfoResponseResponse.to_json())

# convert the object into a dict
query_merchant_info_response_response_dict = query_merchant_info_response_response_instance.to_dict()
# create an instance of QueryMerchantInfoResponseResponse from a dict
query_merchant_info_response_response_from_dict = QueryMerchantInfoResponseResponse.from_dict(query_merchant_info_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


