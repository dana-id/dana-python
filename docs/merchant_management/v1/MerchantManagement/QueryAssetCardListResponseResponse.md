# QueryAssetCardListResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryAssetCardListResponseResponseHead**](QueryAssetCardListResponseResponseHead.md) |  | 
**body** | [**QueryAssetCardListResponseResponseBody**](QueryAssetCardListResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.query_asset_card_list_response_response import QueryAssetCardListResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAssetCardListResponseResponse from a JSON string
query_asset_card_list_response_response_instance = QueryAssetCardListResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryAssetCardListResponseResponse.to_json())

# convert the object into a dict
query_asset_card_list_response_response_dict = query_asset_card_list_response_response_instance.to_dict()
# create an instance of QueryAssetCardListResponseResponse from a dict
query_asset_card_list_response_response_from_dict = QueryAssetCardListResponseResponse.from_dict(query_asset_card_list_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


