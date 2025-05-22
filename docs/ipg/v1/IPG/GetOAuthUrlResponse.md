# GetOAuthUrlResponse

Response object for OAuth 2.0 URL generation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list | 
**response_message** | **str** | Refer to response code list | 
**state** | **str** | Random string for CSRF protection purposes | 
**auth_code** | **str** | An authorization code which the caller can use to obtain an access token | 

## Example

```python
from dana.ipg.v1.models.get_o_auth_url_response import GetOAuthUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthUrlResponse from a JSON string
get_o_auth_url_response_instance = GetOAuthUrlResponse.from_json(json)
# print the JSON string representation of the object
print(GetOAuthUrlResponse.to_json())

# convert the object into a dict
get_o_auth_url_response_dict = get_o_auth_url_response_instance.to_dict()
# create an instance of GetOAuthUrlResponse from a dict
get_o_auth_url_response_from_dict = GetOAuthUrlResponse.from_dict(get_o_auth_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


