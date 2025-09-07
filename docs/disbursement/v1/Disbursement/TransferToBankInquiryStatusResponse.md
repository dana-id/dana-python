# TransferToBankInquiryStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator is based on the service code of the original transaction request, value always 00 | [default to '00']
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**latest_transaction_status** | **str** | Status of latest transaction:<br /> 00 - Success<br /> 01 - Initiated<br /> 02 - Paying<br /> 03 - Pending<br /> 04 - Refunded<br /> 05 - Cancelled<br /> 06 - Failed<br /> 07 - Not found  | 
**transaction_status_desc** | **str** | Description of transaction status | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_bank_inquiry_status_response import TransferToBankInquiryStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToBankInquiryStatusResponse from a JSON string
transfer_to_bank_inquiry_status_response_instance = TransferToBankInquiryStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TransferToBankInquiryStatusResponse.to_json())

# convert the object into a dict
transfer_to_bank_inquiry_status_response_dict = transfer_to_bank_inquiry_status_response_instance.to_dict()
# create an instance of TransferToBankInquiryStatusResponse from a dict
transfer_to_bank_inquiry_status_response_from_dict = TransferToBankInquiryStatusResponse.from_dict(transfer_to_bank_inquiry_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


