# AssetCardListItem

One row in `assetCardList` (response body)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_biz_type** | **str** | Contact business type (&#x60;ContactBizTypeEnum&#x60;) | 
**card_index_no** | **str** | Card index number | 
**card_no_length** | **str** | Card number length based on card index number | 
**masked_card_no** | **str** | Card number (masked) | 
**asset_type** | **str** | Asset / card type (&#x60;AssetCardTypeEnum&#x60;) | 
**holder_name** | **Dict[str, object]** | Holder name (JSON object per DANA spec) | 
**inst_logo_url** | **str** | Institution logo URL | [optional] 
**inst_id** | **str** | Institution identifier | 
**inst_official_name** | **str** | Institution official name based on &#x60;instId&#x60; | 
**expiry_year** | **str** | Expiry year (e.g. debit, credit, virtual account) | 
**expiry_month** | **str** | Expiry month | 
**verified** | **str** | Whether the user&#39;s card is verified | 
**binding_id** | **str** | Asset card bind identifier | [optional] 
**default_asset** | **str** | Whether this asset is the user&#39;s default payment | [optional] 
**enable_status** | **str** | Whether the card status is enabled; &#x60;\&quot;true\&quot;&#x60; when &#x60;enableOnly&#x60; in request was true | [optional] 
**direct_debit** | **str** | Whether payment uses direct debit | [optional] 

## Example

```python
from dana.merchant_management.v1.models.asset_card_list_item import AssetCardListItem

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCardListItem from a JSON string
asset_card_list_item_instance = AssetCardListItem.from_json(json)
# print the JSON string representation of the object
print(AssetCardListItem.to_json())

# convert the object into a dict
asset_card_list_item_dict = asset_card_list_item_instance.to_dict()
# create an instance of AssetCardListItem from a dict
asset_card_list_item_from_dict = AssetCardListItem.from_dict(asset_card_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


