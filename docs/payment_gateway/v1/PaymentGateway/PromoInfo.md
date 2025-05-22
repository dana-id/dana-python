# PromoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo_amount** | [**Money**](Money.md) | Promo amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | 
**promo_id** | **str** | Promo identifier | 
**promo_type** | **str** | Type&#39;s of promo, value always DIRECT_DISCOUNT | [default to 'DIRECT_DISCOUNT']

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


