# RefundOptionBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** | Payment method name. The enums:<br />   * BALANCE - Payment method with balance<br />   * COUPON - Payment method with coupon<br />   * NET_BANKING - Payment method with internet banking<br />   * CREDIT_CARD - Payment method with credit card<br />   * DEBIT_CARD - Payment method with debit card<br />   * VIRTUAL_ACCOUNT - Payment method with virtual account<br />   * OTC - Payment method with OTC<br />   * DIRECT_DEBIT_CREDIT_CARD - Payment method with direct debit of credit card<br />   * DIRECT_DEBIT_DEBIT_CARD - Payment method with direct debit of debit card<br />   * ONLINE_CREDIT - Payment method with online Credit<br />   * LOAN_CREDIT - Payment method with DANA Cicil<br />  | [optional] 
**trans_amount** | [**Money**](Money.md) | Trans amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.refund_option_bill import RefundOptionBill

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOptionBill from a JSON string
refund_option_bill_instance = RefundOptionBill.from_json(json)
# print the JSON string representation of the object
print(RefundOptionBill.to_json())

# convert the object into a dict
refund_option_bill_dict = refund_option_bill_instance.to_dict()
# create an instance of RefundOptionBill from a dict
refund_option_bill_from_dict = RefundOptionBill.from_dict(refund_option_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


