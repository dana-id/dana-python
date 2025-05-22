# QueryPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on partner system. Required if originalReferenceNo is not filled | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system. Required if originalPartnerReferenceNo is not filled | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator is based on the service code of the original transaction request:<br /> - IPG Cashier Pay - SNAP: 54<br /> - QRIS CPM (Acquirer) - SNAP: 60<br /> - QRIS MPM (Acquirer) - SNAP: 47<br /> - Payment Gateway: 54<br />  | [default to '54']
**transaction_date** | **str** | Transaction date, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | [optional] 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.query_payment_request import QueryPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPaymentRequest from a JSON string
query_payment_request_instance = QueryPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(QueryPaymentRequest.to_json())

# convert the object into a dict
query_payment_request_dict = query_payment_request_instance.to_dict()
# create an instance of QueryPaymentRequest from a dict
query_payment_request_from_dict = QueryPaymentRequest.from_dict(query_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


