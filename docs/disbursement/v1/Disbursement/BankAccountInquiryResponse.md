# BankAccountInquiryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**account_type** | **str** | Customer account type | [optional] 
**beneficiary_account_number** | **str** | Beneficiary account number | 
**beneficiary_account_name** | **str** | Beneficiary account name | 
**beneficiary_bank_code** | **str** | Beneficiary Bank code | [optional] 
**beneficiary_bank_short_name** | **str** | Beneficiary Bank short name | [optional] 
**beneficiary_bank_name** | **str** | Beneficiary Bank name | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**additional_info** | [**BankAccountInquiryResponseAdditionalInfo**](BankAccountInquiryResponseAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.disbursement.v1.models.bank_account_inquiry_response import BankAccountInquiryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountInquiryResponse from a JSON string
bank_account_inquiry_response_instance = BankAccountInquiryResponse.from_json(json)
# print the JSON string representation of the object
print(BankAccountInquiryResponse.to_json())

# convert the object into a dict
bank_account_inquiry_response_dict = bank_account_inquiry_response_instance.to_dict()
# create an instance of BankAccountInquiryResponse from a dict
bank_account_inquiry_response_from_dict = BankAccountInquiryResponse.from_dict(bank_account_inquiry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


