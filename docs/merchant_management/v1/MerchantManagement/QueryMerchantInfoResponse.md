# QueryMerchantInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryMerchantInfoResponseResponse**](QueryMerchantInfoResponseResponse.md) |  | [optional] 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_info_response import QueryMerchantInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantInfoResponse from a JSON string
query_merchant_info_response_instance = QueryMerchantInfoResponse.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantInfoResponse.to_json())

# convert the object into a dict
query_merchant_info_response_dict = query_merchant_info_response_instance.to_dict()
# create an instance of QueryMerchantInfoResponse from a dict
query_merchant_info_response_from_dict = QueryMerchantInfoResponse.from_dict(query_merchant_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


