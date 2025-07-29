# BalanceInquiryRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Contains customer token, which has been obtained from binding process, refer to Account Binding &amp; Unbinding documentation  | 

## Example

```python
from dana.widget.v1.models.balance_inquiry_request_additional_info import BalanceInquiryRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceInquiryRequestAdditionalInfo from a JSON string
balance_inquiry_request_additional_info_instance = BalanceInquiryRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(BalanceInquiryRequestAdditionalInfo.to_json())

# convert the object into a dict
balance_inquiry_request_additional_info_dict = balance_inquiry_request_additional_info_instance.to_dict()
# create an instance of BalanceInquiryRequestAdditionalInfo from a dict
balance_inquiry_request_additional_info_from_dict = BalanceInquiryRequestAdditionalInfo.from_dict(balance_inquiry_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


