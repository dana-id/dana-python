# TransferToDanaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | 
**session_id** | **str** | Session identifier | [optional] 
**customer_number** | **str** | Customer account number, in format 628xxx | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_dana_response import TransferToDanaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToDanaResponse from a JSON string
transfer_to_dana_response_instance = TransferToDanaResponse.from_json(json)
# print the JSON string representation of the object
print(TransferToDanaResponse.to_json())

# convert the object into a dict
transfer_to_dana_response_dict = transfer_to_dana_response_instance.to_dict()
# create an instance of TransferToDanaResponse from a dict
transfer_to_dana_response_from_dict = TransferToDanaResponse.from_dict(transfer_to_dana_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


