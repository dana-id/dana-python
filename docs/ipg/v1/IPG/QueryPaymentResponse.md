# QueryPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list:<br /> * 2005500 - Successful<br /> * 4005500 - Bad Request - Retry request with proper parameter<br /> * 4005501 - Invalid Field Format - Retry request with proper parameter<br /> * 4005502 - Invalid Mandatory Field - Retry request with proper parameter<br /> * 4015500 - Unauthorized. [reason] - Retry request with proper parameter<br /> * 4015501 - Invalid Token (B2B) - Retry request with proper parameter<br /> * 4045501 - Transaction Not Found - Try to create a new order<br /> * 4295500 - Too Many Requests - Retry request periodically<br /> * 5005500 - General Error - Retry request periodically<br /> * 5005501 - Internal Server Error - Retry request periodically<br />  | 
**response_message** | **str** | Refer to response code list  | 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator:<br /> - IPG Cashier Pay - SNAP: 54<br /> - QRIS CPM (Acquirer) - SNAP: 60<br /> - QRIS MPM (Acquirer) - SNAP: 47<br /> - Payment Gateway: 54<br />  | [default to '54']
**latest_transaction_status** | **str** | Status code:<br /> - 00 &#x3D; Success. Order has been successfully in final state and paid<br /> - 01 &#x3D; Initiated. Waiting for payment. Mark Payment as Pending<br /> - 02 &#x3D; Paying. The order is in process, not in final state, payment is success. Mark Payment as Success<br /> - 05 &#x3D; Cancelled. Order has been cancelled. Mark Payment as Failed<br /> - 07 &#x3D; Not found. Order is not found. Mark Payment as Failed<br />  | 
**transaction_status_desc** | **str** | Description of transaction status | [optional] 
**original_response_code** | **str** | Original response code | [optional] 
**original_response_message** | **str** | Original response message | [optional] 
**session_id** | **str** | Session identifier | [optional] 
**request_id** | **str** | Transaction request identifier | [optional] 
**trans_amount** | [**Money**](Money.md) |  | [optional] 
**amount** | [**Money**](Money.md) |  | [optional] 
**fee_amount** | [**Money**](Money.md) |  | [optional] 
**paid_time** | **str** | Payment timestamp in format YYYY-MM-DDTHH:mm:ss+07:00 (Jakarta time) | [optional] 
**title** | **str** | Brief description of transaction | [optional] 
**additional_info** | [**QueryPaymentResponseAdditionalInfo**](QueryPaymentResponseAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.ipg.v1.models.query_payment_response import QueryPaymentResponse

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


