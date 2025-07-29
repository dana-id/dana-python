# PaymentPromoInfo

Information about the payment promotion that was applied

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo_id** | **str** | Promotion identifier | 
**promo_name** | **str** | Promotion name | 
**promo_type** | **str** | Type of promotion | 
**savings_amount** | [**Money**](Money.md) | Savings amount from this promotion. Contains value (amount including cents) and currency (code based on ISO) | 

## Example

```python
from dana.widget.v1.models.payment_promo_info import PaymentPromoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPromoInfo from a JSON string
payment_promo_info_instance = PaymentPromoInfo.from_json(json)
# print the JSON string representation of the object
print(PaymentPromoInfo.to_json())

# convert the object into a dict
payment_promo_info_dict = payment_promo_info_instance.to_dict()
# create an instance of PaymentPromoInfo from a dict
payment_promo_info_from_dict = PaymentPromoInfo.from_dict(payment_promo_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


