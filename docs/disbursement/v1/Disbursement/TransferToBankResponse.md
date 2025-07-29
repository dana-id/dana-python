# TransferToBankResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**transaction_date** | **str** | Transaction date, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**reference_number** | **str** | Reference number | 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_bank_response import TransferToBankResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToBankResponse from a JSON string
transfer_to_bank_response_instance = TransferToBankResponse.from_json(json)
# print the JSON string representation of the object
print(TransferToBankResponse.to_json())

# convert the object into a dict
transfer_to_bank_response_dict = transfer_to_bank_response_instance.to_dict()
# create an instance of TransferToBankResponse from a dict
transfer_to_bank_response_from_dict = TransferToBankResponse.from_dict(transfer_to_bank_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


