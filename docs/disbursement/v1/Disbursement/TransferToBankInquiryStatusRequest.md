# TransferToBankInquiryStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on partner system<br /> Notes:<br /> Required to be filled using the partnerReferenceNo that is the same as the one used in Transfer to Bank  | [optional] 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator is based on the service code of the original transaction request, value always 00 | [default to '00']
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_bank_inquiry_status_request import TransferToBankInquiryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToBankInquiryStatusRequest from a JSON string
transfer_to_bank_inquiry_status_request_instance = TransferToBankInquiryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransferToBankInquiryStatusRequest.to_json())

# convert the object into a dict
transfer_to_bank_inquiry_status_request_dict = transfer_to_bank_inquiry_status_request_instance.to_dict()
# create an instance of TransferToBankInquiryStatusRequest from a dict
transfer_to_bank_inquiry_status_request_from_dict = TransferToBankInquiryStatusRequest.from_dict(transfer_to_bank_inquiry_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


