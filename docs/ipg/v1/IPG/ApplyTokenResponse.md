# ApplyTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list:<br /> * 2007400 - Successful<br /> * 4007400 - Bad Request - Retry request with proper parameter<br /> * 4007401 - Invalid Field Format - Retry request with proper parameter<br /> * 4007402 - Invalid Mandatory Field - Retry request with proper parameter<br /> * 4017400 - Unauthorized. [reason] - Retry request with proper parameter<br /> * 4297400 - Too Many Requests - Retry request periodically by sending same request payload<br /> * 5007400 - General Error - Retry request periodically<br /> * 5007401 - Internal Server Error - Retry request periodically by sending same request payload<br />  | 
**response_message** | **str** | Refer to response code list | 
**token_type** | **str** | Token type | [optional] 
**access_token** | **str** | Access token that can be used as user authorization | 
**access_token_expiry_time** | **str** | Access token expiry time | [optional] 
**refresh_token** | **str** | Token that can be used to refresh the accessToken when it expires | [optional] 
**refresh_token_expiry_time** | **str** | Refresh token expiry time | [optional] 
**additional_info** | [**ApplyTokenResponseAdditionalInfo**](ApplyTokenResponseAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.ipg.v1.models.apply_token_response import ApplyTokenResponse

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


