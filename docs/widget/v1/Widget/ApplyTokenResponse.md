# ApplyTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/110#HTML-ApplyToken-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/110#HTML-ApplyToken-ResponseCodeandMessage | 
**token_type** | **str** | Token type. Present if successfully processed | [optional] 
**access_token** | **str** | This token is called Customer Token that will be used as a parameter on header in other API “Authorization-Customer”. Present if successfully processed | 
**access_token_expiry_time** | **str** | Expiry time for access token was given to user, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time). Present if successfully processed | [optional] 
**refresh_token** | **str** | This token is used for refresh session if existing token has been expired. Present if successfully processed | [optional] 
**refresh_token_expiry_time** | **str** | Expiry time for refresh token was given to user, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time). Present if successfully processed | [optional] 
**additional_info** | [**ApplyTokenResponseAdditionalInfo**](ApplyTokenResponseAdditionalInfo.md) | Additional information | [optional] 

## Example

```python
from dana.widget.v1.models.apply_token_response import ApplyTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyTokenResponse from a JSON string
apply_token_response_instance = ApplyTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyTokenResponse.to_json())

# convert the object into a dict
apply_token_response_dict = apply_token_response_instance.to_dict()
# create an instance of ApplyTokenResponse from a dict
apply_token_response_from_dict = ApplyTokenResponse.from_dict(apply_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


