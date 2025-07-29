# ApplyTokenAuthorizationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **Dict[str, object]** | Additional information | [optional] 
**grant_type** | **str** | Apply token request type. The value is AUTHORIZATION_CODE | 
**auth_code** | **str** | Authorization code. Please refer to https://dashboard.dana.id/api-docs/read/125. Required if grantType is AUTHORIZATION_CODE | 
**refresh_token** | **str** | This token is used for refresh session if existing token has been expired | [optional] 

## Example

```python
from dana.widget.v1.models.apply_token_authorization_code_request import ApplyTokenAuthorizationCodeRequest

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


