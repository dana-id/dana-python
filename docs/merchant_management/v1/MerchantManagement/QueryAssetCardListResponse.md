# QueryAssetCardListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryAssetCardListResponseResponse**](QueryAssetCardListResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_asset_card_list_response import QueryAssetCardListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAssetCardListResponse from a JSON string
query_asset_card_list_response_instance = QueryAssetCardListResponse.from_json(json)
# print the JSON string representation of the object
print(QueryAssetCardListResponse.to_json())

# convert the object into a dict
query_asset_card_list_response_dict = query_asset_card_list_response_instance.to_dict()
# create an instance of QueryAssetCardListResponse from a dict
query_asset_card_list_response_from_dict = QueryAssetCardListResponse.from_dict(query_asset_card_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


