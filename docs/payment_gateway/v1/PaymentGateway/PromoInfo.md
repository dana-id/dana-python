# PromoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo_amount** | [**Money**](Money.md) |  | 
**promo_id** | **str** |  | 
**promo_type** | **str** |  | [default to 'DIRECT_DISCOUNT']

## Example

```python
from dana.payment_gateway.v1.models.promo_info import PromoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PromoInfo from a JSON string
promo_info_instance = PromoInfo.from_json(json)
# print the JSON string representation of the object
print(PromoInfo.to_json())

# convert the object into a dict
promo_info_dict = promo_info_instance.to_dict()
# create an instance of PromoInfo from a dict
promo_info_from_dict = PromoInfo.from_dict(promo_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


