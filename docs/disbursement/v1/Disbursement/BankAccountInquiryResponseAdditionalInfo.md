# BankAccountInquiryResponseAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_amount** | [**Money**](Money.md) | Additional information of fee amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 

## Example

```python
from dana.disbursement.v1.models.bank_account_inquiry_response_additional_info import BankAccountInquiryResponseAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountInquiryResponseAdditionalInfo from a JSON string
bank_account_inquiry_response_additional_info_instance = BankAccountInquiryResponseAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(BankAccountInquiryResponseAdditionalInfo.to_json())

# convert the object into a dict
bank_account_inquiry_response_additional_info_dict = bank_account_inquiry_response_additional_info_instance.to_dict()
# create an instance of BankAccountInquiryResponseAdditionalInfo from a dict
bank_account_inquiry_response_additional_info_from_dict = BankAccountInquiryResponseAdditionalInfo.from_dict(bank_account_inquiry_response_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


