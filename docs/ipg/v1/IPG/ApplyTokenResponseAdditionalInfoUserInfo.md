# ApplyTokenResponseAdditionalInfoUserInfo

Additional information of user. Contains publicUserId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_user_id** | **str** | Static unique identifier for one user | [optional] 

## Example

```python
from dana.ipg.v1.models.apply_token_response_additional_info_user_info import ApplyTokenResponseAdditionalInfoUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTokenResponseAdditionalInfoUserInfo from a JSON string
apply_token_response_additional_info_user_info_instance = ApplyTokenResponseAdditionalInfoUserInfo.from_json(json)
# print the JSON string representation of the object
print(ApplyTokenResponseAdditionalInfoUserInfo.to_json())

# convert the object into a dict
apply_token_response_additional_info_user_info_dict = apply_token_response_additional_info_user_info_instance.to_dict()
# create an instance of ApplyTokenResponseAdditionalInfoUserInfo from a dict
apply_token_response_additional_info_user_info_from_dict = ApplyTokenResponseAdditionalInfoUserInfo.from_dict(apply_token_response_additional_info_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


