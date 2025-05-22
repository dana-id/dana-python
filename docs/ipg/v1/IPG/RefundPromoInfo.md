# RefundPromoInfo

Information about the refund promotion that was applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo_id** | **str** | Promotion identifier | 
**promo_name** | **str** | Promotion name | 
**promo_type** | **str** | Type of promotion | 
**refund_amount** | [**Money**](Money.md) | Refund amount from this promotion. Contains value (amount including cents) and currency (code based on ISO) | 

## Example

```python
from dana.ipg.v1.models.refund_promo_info import RefundPromoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefundPromoInfo from a JSON string
refund_promo_info_instance = RefundPromoInfo.from_json(json)
# print the JSON string representation of the object
print(RefundPromoInfo.to_json())

# convert the object into a dict
refund_promo_info_dict = refund_promo_info_instance.to_dict()
# create an instance of RefundPromoInfo from a dict
refund_promo_info_from_dict = RefundPromoInfo.from_dict(refund_promo_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


