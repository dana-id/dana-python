# InternationalOrderInfo

Additional information for international orders (non-IDR currency transactions)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_order_amount** | [**Money**](Money.md) | Origin order amount in the original currency. Contains value (amount including cents) and currency (code based on ISO) | [optional] 
**exchange_rate** | [**InternationalOrderInfoExchangeRate**](InternationalOrderInfoExchangeRate.md) |  | [optional] 
**total_amount** | [**Money**](Money.md) | Total amount after conversion. Contains value (amount including cents) and currency (code based on ISO) | [optional] 
**payment_promo_info** | [**PaymentPromoInfo**](PaymentPromoInfo.md) | Define the detail of payment promo information, contains promotion that handled and set by merchant | [optional] 
**refund_promo_info** | [**RefundPromoInfo**](RefundPromoInfo.md) | Define the detail of refund promo information | [optional] 

## Example

```python
from dana.widget.v1.models.international_order_info import InternationalOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalOrderInfo from a JSON string
international_order_info_instance = InternationalOrderInfo.from_json(json)
# print the JSON string representation of the object
print(InternationalOrderInfo.to_json())

# convert the object into a dict
international_order_info_dict = international_order_info_instance.to_dict()
# create an instance of InternationalOrderInfo from a dict
international_order_info_from_dict = InternationalOrderInfo.from_dict(international_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


