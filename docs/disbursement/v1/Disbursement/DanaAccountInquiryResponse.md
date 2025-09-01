# DanaAccountInquiryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**session_id** | **str** | Session identifier | [optional] 
**customer_number** | **str** | Customer account number, in format 628xxx | [optional] 
**customer_name** | **str** | Customer account name | 
**customer_monthly_in_limit** | **str** | Limitation of transfer to DANA balance for customer per month | [optional] 
**min_amount** | [**Money**](Money.md) | Minimal amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**max_amount** | [**Money**](Money.md) | Maximal amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**fee_amount** | [**Money**](Money.md) | Fee amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**fee_type** | **str** | Type of fee for each transfer to DANA transaction. Such as admin fee | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.disbursement.v1.models.dana_account_inquiry_response import DanaAccountInquiryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DanaAccountInquiryResponse from a JSON string
dana_account_inquiry_response_instance = DanaAccountInquiryResponse.from_json(json)
# print the JSON string representation of the object
print(DanaAccountInquiryResponse.to_json())

# convert the object into a dict
dana_account_inquiry_response_dict = dana_account_inquiry_response_instance.to_dict()
# create an instance of DanaAccountInquiryResponse from a dict
dana_account_inquiry_response_from_dict = DanaAccountInquiryResponse.from_dict(dana_account_inquiry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


