# AccountUnbindingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/108#HTML-AccountUnbinding-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/108#HTML-AccountUnbinding-ResponseCodeandMessage | 
**reference_no** | **str** | Transaction identifier on DANA system | [optional] 
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction | [optional] 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | [optional] 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**link_id** | **str** | Information of link identifier | [optional] 
**unlink_result** | **str** | Result of unlinking process | [optional] 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.ipg.v1.models.account_unbinding_response import AccountUnbindingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUnbindingResponse from a JSON string
account_unbinding_response_instance = AccountUnbindingResponse.from_json(json)
# print the JSON string representation of the object
print(AccountUnbindingResponse.to_json())

# convert the object into a dict
account_unbinding_response_dict = account_unbinding_response_instance.to_dict()
# create an instance of AccountUnbindingResponse from a dict
account_unbinding_response_from_dict = AccountUnbindingResponse.from_dict(account_unbinding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


