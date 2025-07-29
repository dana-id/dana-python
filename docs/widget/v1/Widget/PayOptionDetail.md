# PayOptionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** | Payment Method, e.g. CREDIT_CARD | 
**pay_option** | **str** | Payment option which shows the provider of this payment e.g. CREDIT_CARD_VISA | 
**trans_amount** | [**Money**](Money.md) | Trans amount. Contains value and currency | [optional] 
**fee_amount** | [**Money**](Money.md) | Fee amount. Contains value and currency | [optional] 
**card_token** | **str** | Card token used for this payment | [optional] 
**merchant_token** | **str** | Merchant token used for this payment | [optional] 
**additional_info** | [**PayOptionDetailAdditionalInfo**](PayOptionDetailAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.widget.v1.models.pay_option_detail import PayOptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionDetail from a JSON string
pay_option_detail_instance = PayOptionDetail.from_json(json)
# print the JSON string representation of the object
print(PayOptionDetail.to_json())

# convert the object into a dict
pay_option_detail_dict = pay_option_detail_instance.to_dict()
# create an instance of PayOptionDetail from a dict
pay_option_detail_from_dict = PayOptionDetail.from_dict(pay_option_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


