# QueryMerchantInfoResponseResponseBody

Response body (`resultInfo` and `merchantInformation` optional per API contract)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**MemberAssetResultInfo**](MemberAssetResultInfo.md) |  | [optional] 
**merchant_information** | [**MerchantInformation**](MerchantInformation.md) |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_info_response_response_body import QueryMerchantInfoResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantInfoResponseResponseBody from a JSON string
query_merchant_info_response_response_body_instance = QueryMerchantInfoResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantInfoResponseResponseBody.to_json())

# convert the object into a dict
query_merchant_info_response_response_body_dict = query_merchant_info_response_response_body_instance.to_dict()
# create an instance of QueryMerchantInfoResponseResponseBody from a dict
query_merchant_info_response_response_body_from_dict = QueryMerchantInfoResponseResponseBody.from_dict(query_merchant_info_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


