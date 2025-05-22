# QueryPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/126#HTML-API-QueryPayment-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/126#HTML-API-QueryPayment-ResponseCodeandMessage | 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system. Present if transaction found | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system. Present if transaction found | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator is based on the service code of the original transaction request:<br /> - IPG Cashier Pay - SNAP: 54<br /> - QRIS CPM (Acquirer) - SNAP: 60<br /> - QRIS MPM (Acquirer) - SNAP: 47<br /> - Payment Gateway: 54<br />  | [default to '54']
**latest_transaction_status** | **str** | Category code for the status of the transaction. The values include:<br /> - 00 &#x3D; Success, the order has been successfully in final state and paid<br /> - 01 &#x3D; Initiated, the order has been created, but has not been paid<br /> - 02 &#x3D; Paying, the order is in process, not in final state, payment is success<br /> - 05 &#x3D; Cancelled, the order has been closed<br /> - 07 &#x3D; Not found, the order is not found<br />  | 
**transaction_status_desc** | **str** | Description of transaction status | [optional] 
**original_response_code** | **str** | Original response code | [optional] 
**original_response_message** | **str** | Original response message | [optional] 
**session_id** | **str** | Session identifier | [optional] 
**request_id** | **str** | Transaction request identifier | [optional] 
**trans_amount** | [**Money**](Money.md) | Trans amount. Present if transaction found. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**amount** | [**Money**](Money.md) | Amount. Present if transaction found. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**fee_amount** | [**Money**](Money.md) | Fee amount. Present if transaction found. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**paid_time** | **str** | Transaction paid time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time). Present if transaction is paid | [optional] 
**title** | **str** | Brief description. Present if transaction found | [optional] 
**additional_info** | [**QueryPaymentResponseAdditionalInfo**](QueryPaymentResponseAdditionalInfo.md) | Additional information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.query_payment_response import QueryPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPaymentResponse from a JSON string
query_payment_response_instance = QueryPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(QueryPaymentResponse.to_json())

# convert the object into a dict
query_payment_response_dict = query_payment_response_instance.to_dict()
# create an instance of QueryPaymentResponse from a dict
query_payment_response_from_dict = QueryPaymentResponse.from_dict(query_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


