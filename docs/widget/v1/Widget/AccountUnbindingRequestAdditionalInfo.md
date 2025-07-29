# AccountUnbindingRequestAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Contains customer token, which has been obtained from binding process | 
**end_user_ip_address** | **str** | IP address of the end user (customer) using IPv4 format | [optional] 
**device_id** | **str** | Device identification on which the API services is currently being accessed by the end user (customer) | 
**latitude** | **str** | Location on which the API services is currently being accessed by the end user (customer), refer to ISO 6709 standard representation of geographic point location by coordinates | [optional] 
**longitude** | **str** | Location on which the API services is currently being accessed by the end user (customer), refer to ISO 6709 Standard representation of geographic point location by coordinates | [optional] 

## Example

```python
from dana.widget.v1.models.account_unbinding_request_additional_info import AccountUnbindingRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUnbindingRequestAdditionalInfo from a JSON string
account_unbinding_request_additional_info_instance = AccountUnbindingRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(AccountUnbindingRequestAdditionalInfo.to_json())

# convert the object into a dict
account_unbinding_request_additional_info_dict = account_unbinding_request_additional_info_instance.to_dict()
# create an instance of AccountUnbindingRequestAdditionalInfo from a dict
account_unbinding_request_additional_info_from_dict = AccountUnbindingRequestAdditionalInfo.from_dict(account_unbinding_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


