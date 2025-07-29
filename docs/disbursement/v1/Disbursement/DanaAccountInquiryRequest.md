# DanaAccountInquiryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**customer_number** | **str** | Customer account number, in format 628xxx | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**transaction_date** | **str** | Transaction date, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**additional_info** | [**DanaAccountInquiryRequestAdditionalInfo**](DanaAccountInquiryRequestAdditionalInfo.md) |  | 

## Example

```python
from dana.disbursement.v1.models.dana_account_inquiry_request import DanaAccountInquiryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DanaAccountInquiryRequest from a JSON string
dana_account_inquiry_request_instance = DanaAccountInquiryRequest.from_json(json)
# print the JSON string representation of the object
print(DanaAccountInquiryRequest.to_json())

# convert the object into a dict
dana_account_inquiry_request_dict = dana_account_inquiry_request_instance.to_dict()
# create an instance of DanaAccountInquiryRequest from a dict
dana_account_inquiry_request_from_dict = DanaAccountInquiryRequest.from_dict(dana_account_inquiry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


