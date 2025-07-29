# TransferToBankRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**customer_number** | **str** | Customer account number, in format 628xxx | 
**account_type** | **str** | Customer account type | [optional] 
**beneficiary_account_number** | **str** | Beneficiary account number | 
**beneficiary_bank_code** | **str** | Beneficiary Bank code | 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**additional_info** | [**TransferToBankRequestAdditionalInfo**](TransferToBankRequestAdditionalInfo.md) |  | 

## Example

```python
from dana.disbursement.v1.models.transfer_to_bank_request import TransferToBankRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToBankRequest from a JSON string
transfer_to_bank_request_instance = TransferToBankRequest.from_json(json)
# print the JSON string representation of the object
print(TransferToBankRequest.to_json())

# convert the object into a dict
transfer_to_bank_request_dict = transfer_to_bank_request_instance.to_dict()
# create an instance of TransferToBankRequest from a dict
transfer_to_bank_request_from_dict = TransferToBankRequest.from_dict(transfer_to_bank_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


