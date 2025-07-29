# BankAccountInquiryRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_type** | **str** | Additional information of withdraw fund type, i.e.<br /> MERCHANT_WITHDRAW_FOR_CORPORATE  | 
**external_division_id** | **str** | Additional information of external division identifier. (fundType: MERCHANT_WITHDRAW_FOR_CORPORATE)<br /> Notes: The required of this parameter is Optional, but if \&quot;additionalInfo.chargeTarget\&quot; has value DIVISION then the required of this parameter will be changed to Mandatory  | [optional] 
**charge_target** | **str** | Additional information of charge target. The values are:<br /> • null<br /> • DIVISION<br /> • MERCHANT<br /> Notes: If the value is DIVISION, externalDivisionId will be Mandatory  | [optional] 
**beneficiary_bank_code** | **str** | Additional information of beneficiary Bank code | 
**beneficiary_account_name** | **str** | Additional information of beneficiary account name for validation purpose | [optional] 
**account_type** | **str** | Additional information of account type | [optional] 
**access_token** | **str** | Contains customer token, which has been obtained from binding process, refer to Account Binding &amp; Unbinding documentation<br /> If request is coming from user interaction, this field is mandatory. If not, just filled customerNumber  | [optional] 

## Example

```python
from dana.disbursement.v1.models.bank_account_inquiry_request_additional_info import BankAccountInquiryRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountInquiryRequestAdditionalInfo from a JSON string
bank_account_inquiry_request_additional_info_instance = BankAccountInquiryRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(BankAccountInquiryRequestAdditionalInfo.to_json())

# convert the object into a dict
bank_account_inquiry_request_additional_info_dict = bank_account_inquiry_request_additional_info_instance.to_dict()
# create an instance of BankAccountInquiryRequestAdditionalInfo from a dict
bank_account_inquiry_request_additional_info_from_dict = BankAccountInquiryRequestAdditionalInfo.from_dict(bank_account_inquiry_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


