# QueryAssetCardListResponseResponseBody

Response body (`resultInfo` mandatory; `assetCardList` optional)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**MemberAssetResultInfo**](MemberAssetResultInfo.md) |  | 
**asset_card_list** | [**List[AssetCardListItem]**](AssetCardListItem.md) | Asset card list detail (present when applicable) | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_asset_card_list_response_response_body import QueryAssetCardListResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAssetCardListResponseResponseBody from a JSON string
query_asset_card_list_response_response_body_instance = QueryAssetCardListResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryAssetCardListResponseResponseBody.to_json())

# convert the object into a dict
query_asset_card_list_response_response_body_dict = query_asset_card_list_response_response_body_instance.to_dict()
# create an instance of QueryAssetCardListResponseResponseBody from a dict
query_asset_card_list_response_response_body_from_dict = QueryAssetCardListResponseResponseBody.from_dict(query_asset_card_list_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


