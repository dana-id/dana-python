# TransferToDanaInquiryStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_partner_reference_no** | **str** | Original transaction identifier on partner system | 
**original_reference_no** | **str** | Original transaction identifier on DANA system | [optional] 
**original_external_id** | **str** | Original external identifier on header message | [optional] 
**service_code** | **str** | Transaction type indicator is based on the service code of the original transaction request, value always 38 | [default to '38']
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_dana_inquiry_status_request import TransferToDanaInquiryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToDanaInquiryStatusRequest from a JSON string
transfer_to_dana_inquiry_status_request_instance = TransferToDanaInquiryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransferToDanaInquiryStatusRequest.to_json())

# convert the object into a dict
transfer_to_dana_inquiry_status_request_dict = transfer_to_dana_inquiry_status_request_instance.to_dict()
# create an instance of TransferToDanaInquiryStatusRequest from a dict
transfer_to_dana_inquiry_status_request_from_dict = TransferToDanaInquiryStatusRequest.from_dict(transfer_to_dana_inquiry_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


