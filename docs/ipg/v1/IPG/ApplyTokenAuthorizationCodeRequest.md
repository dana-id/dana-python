# ApplyTokenAuthorizationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **Dict[str, object]** | Additional information | [optional] 

## Example

```python
from dana.ipg.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTokenAuthorizationCodeRequest from a JSON string
apply_token_authorization_code_request_instance = ApplyTokenAuthorizationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyTokenAuthorizationCodeRequest.to_json())

# convert the object into a dict
apply_token_authorization_code_request_dict = apply_token_authorization_code_request_instance.to_dict()
# create an instance of ApplyTokenAuthorizationCodeRequest from a dict
apply_token_authorization_code_request_from_dict = ApplyTokenAuthorizationCodeRequest.from_dict(apply_token_authorization_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


