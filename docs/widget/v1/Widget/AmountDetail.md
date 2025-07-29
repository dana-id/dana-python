# AmountDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_amount** | [**Money**](Money.md) | Order amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | 
**pay_amount** | [**Money**](Money.md) | Pay amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**void_amount** | [**Money**](Money.md) | Void amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**confirm_amount** | [**Money**](Money.md) | Confirm amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**refund_amount** | [**Money**](Money.md) | Refund amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**chargeback_amount** | [**Money**](Money.md) | Chargeback amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**charge_amount** | [**Money**](Money.md) | Charge amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 

## Example

```python
from dana.widget.v1.models.amount_detail import AmountDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AmountDetail from a JSON string
amount_detail_instance = AmountDetail.from_json(json)
# print the JSON string representation of the object
print(AmountDetail.to_json())

# convert the object into a dict
amount_detail_dict = amount_detail_instance.to_dict()
# create an instance of AmountDetail from a dict
amount_detail_from_dict = AmountDetail.from_dict(amount_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


