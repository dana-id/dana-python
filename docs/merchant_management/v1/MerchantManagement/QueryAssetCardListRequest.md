# QueryAssetCardListRequest

Business fields mapped to `request.body` in the JSON envelope (head/signature are handled by the client/runtime).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | User identifier or merchant identifier | 
**binding_id** | **str** | Asset card bind identifier | [optional] 
**enable_only** | **str** | Return only active cards when &#x60;\&quot;true\&quot;&#x60; | [optional] 
**contact_biz_type_list** | **List[str]** | Contact biz type list (&#x60;ContactBizTypeEnum&#x60;) | [optional] 
**asset_type_list** | **List[str]** | Asset type list (&#x60;AssetCardTypeEnum&#x60;) | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_asset_card_list_request import QueryAssetCardListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAssetCardListRequest from a JSON string
query_asset_card_list_request_instance = QueryAssetCardListRequest.from_json(json)
# print the JSON string representation of the object
print(QueryAssetCardListRequest.to_json())

# convert the object into a dict
query_asset_card_list_request_dict = query_asset_card_list_request_instance.to_dict()
# create an instance of QueryAssetCardListRequest from a dict
query_asset_card_list_request_from_dict = QueryAssetCardListRequest.from_dict(query_asset_card_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


