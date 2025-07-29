# BalanceInquiryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | [optional] 
**balance_types** | **List[str]** | Information of balance types to specify which balance type expected to be returned. Will return all available balance type if this parameter empty | [optional] 
**additional_info** | [**BalanceInquiryRequestAdditionalInfo**](BalanceInquiryRequestAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.widget.v1.models.balance_inquiry_request import BalanceInquiryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceInquiryRequest from a JSON string
balance_inquiry_request_instance = BalanceInquiryRequest.from_json(json)
# print the JSON string representation of the object
print(BalanceInquiryRequest.to_json())

# convert the object into a dict
balance_inquiry_request_dict = balance_inquiry_request_instance.to_dict()
# create an instance of BalanceInquiryRequest from a dict
balance_inquiry_request_from_dict = BalanceInquiryRequest.from_dict(balance_inquiry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


