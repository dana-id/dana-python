# ApplyTokenRefreshTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **Dict[str, object]** | Additional information | [optional] 
**grant_type** | **str** | Apply token request type. The values are AUTHORIZATION_CODE or REFRESH_TOKEN | 
**auth_code** | **str** |  | [optional] [default to '']
**refresh_token** | **str** | This token is used for refresh session if existing token has been expired | 

## Example

```python
from dana.ipg.v1.models.apply_token_refresh_token_request import ApplyTokenRefreshTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTokenRefreshTokenRequest from a JSON string
apply_token_refresh_token_request_instance = ApplyTokenRefreshTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyTokenRefreshTokenRequest.to_json())

# convert the object into a dict
apply_token_refresh_token_request_dict = apply_token_refresh_token_request_instance.to_dict()
# create an instance of ApplyTokenRefreshTokenRequest from a dict
apply_token_refresh_token_request_from_dict = ApplyTokenRefreshTokenRequest.from_dict(apply_token_refresh_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


