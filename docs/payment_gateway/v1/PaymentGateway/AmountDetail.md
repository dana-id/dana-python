# AmountDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_amount** | [**Money**](Money.md) | Order amount including cents and currency (ISO format) | 
**pay_amount** | [**Money**](Money.md) | Pay amount including cents and currency (ISO format) | [optional] 
**void_amount** | [**Money**](Money.md) | Void amount including cents and currency (ISO format) | [optional] 
**confirm_amount** | [**Money**](Money.md) | Confirm amount including cents and currency (ISO format) | [optional] 
**refund_amount** | [**Money**](Money.md) | Refund amount including cents and currency (ISO format) | [optional] 
**chargeback_amount** | [**Money**](Money.md) | Chargeback amount including cents and currency (ISO format) | [optional] 
**charge_amount** | [**Money**](Money.md) | Charge amount including cents and currency (ISO format) | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.amount_detail import AmountDetail

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


