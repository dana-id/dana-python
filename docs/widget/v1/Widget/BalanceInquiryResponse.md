# BalanceInquiryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**name** | **str** | Customer account name | [optional] 
**account_infos** | [**List[AccountInfo]**](AccountInfo.md) | Account information | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.widget.v1.models.balance_inquiry_response import BalanceInquiryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceInquiryResponse from a JSON string
balance_inquiry_response_instance = BalanceInquiryResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceInquiryResponse.to_json())

# convert the object into a dict
balance_inquiry_response_dict = balance_inquiry_response_instance.to_dict()
# create an instance of BalanceInquiryResponse from a dict
balance_inquiry_response_from_dict = BalanceInquiryResponse.from_dict(balance_inquiry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


