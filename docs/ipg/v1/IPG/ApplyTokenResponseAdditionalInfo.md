# ApplyTokenResponseAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_info** | [**ApplyTokenResponseAdditionalInfoUserInfo**](ApplyTokenResponseAdditionalInfoUserInfo.md) |  | [optional] 

## Example

```python
from dana.ipg.v1.models.apply_token_response_additional_info import ApplyTokenResponseAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTokenResponseAdditionalInfo from a JSON string
apply_token_response_additional_info_instance = ApplyTokenResponseAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ApplyTokenResponseAdditionalInfo.to_json())

# convert the object into a dict
apply_token_response_additional_info_dict = apply_token_response_additional_info_instance.to_dict()
# create an instance of ApplyTokenResponseAdditionalInfo from a dict
apply_token_response_additional_info_from_dict = ApplyTokenResponseAdditionalInfo.from_dict(apply_token_response_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


