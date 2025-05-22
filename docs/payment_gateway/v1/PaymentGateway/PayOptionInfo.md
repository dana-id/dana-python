# PayOptionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** | Payment method name. The enums:<br />   * BALANCE - Payment method with balance<br />   * COUPON - Payment method with coupon<br />   * NET_BANKING - Payment method with internet banking<br />   * CREDIT_CARD - Payment method with credit card<br />   * DEBIT_CARD - Payment method with debit card<br />   * VIRTUAL_ACCOUNT - Payment method with virtual account<br />   * OTC - Payment method with OTC<br />   * DIRECT_DEBIT_CREDIT_CARD - Payment method with direct debit of credit card<br />   * DIRECT_DEBIT_DEBIT_CARD - Payment method with direct debit of debit card<br />   * ONLINE_CREDIT - Payment method with online Credit<br />   * LOAN_CREDIT - Payment method with DANA Cicil<br />  | 
**pay_option** | **str** | Payment option which shows the provider of this payment. The enums:<br />   * NETWORK_PAY_PG_SPAY - Payment method with ShopeePay e-wallet<br />   * NETWORK_PAY_PG_OVO - Payment method with OVO e-wallet<br />   * NETWORK_PAY_PG_GOPAY - Payment method with GoPay e-wallet<br />   * NETWORK_PAY_PG_LINKAJA - Payment method with LinkAja e-wallet<br />   * NETWORK_PAY_PG_CARD - Payment method with Card<br />   * VIRTUAL_ACCOUNT_BCA - Payment method with BCA virtual account<br />   * VIRTUAL_ACCOUNT_BNI - Payment method with BNI virtual account<br />   * VIRTUAL_ACCOUNT_MANDIRI - Payment method with Mandiri virtual account<br />   * VIRTUAL_ACCOUNT_BRI - Payment method with BRI virtual account<br />   * VIRTUAL_ACCOUNT_BTPN - Payment method with BTPN virtual account<br />   * VIRTUAL_ACCOUNT_CIMB - Payment method with CIMB virtual account<br />   * VIRTUAL_ACCOUNT_PERMATA - Payment method with Permata virtual account<br />  | [optional] 
**pay_amount** | [**Money**](Money.md) | Pay amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**trans_amount** | [**Money**](Money.md) | Trans amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**charge_amount** | [**Money**](Money.md) | Charge amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**pay_option_bill_extend_info** | **str** | Extend information of pay option bill | [optional] 
**extend_info** | **str** | Extend information | [optional] 
**payment_code** | **str** | Payment code | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.pay_option_info import PayOptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionInfo from a JSON string
pay_option_info_instance = PayOptionInfo.from_json(json)
# print the JSON string representation of the object
print(PayOptionInfo.to_json())

# convert the object into a dict
pay_option_info_dict = pay_option_info_instance.to_dict()
# create an instance of PayOptionInfo from a dict
pay_option_info_from_dict = PayOptionInfo.from_dict(pay_option_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


