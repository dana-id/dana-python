# BankAccountInquiryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**customer_number** | **str** | Customer account number, in format 628xxx | 
**beneficiary_account_number** | **str** | Beneficiary account number | 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**additional_info** | [**BankAccountInquiryRequestAdditionalInfo**](BankAccountInquiryRequestAdditionalInfo.md) |  | 

## Example

```python
from dana.disbursement.v1.models.bank_account_inquiry_request import BankAccountInquiryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountInquiryRequest from a JSON string
bank_account_inquiry_request_instance = BankAccountInquiryRequest.from_json(json)
# print the JSON string representation of the object
print(BankAccountInquiryRequest.to_json())

# convert the object into a dict
bank_account_inquiry_request_dict = bank_account_inquiry_request_instance.to_dict()
# create an instance of BankAccountInquiryRequest from a dict
bank_account_inquiry_request_from_dict = BankAccountInquiryRequest.from_dict(bank_account_inquiry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


