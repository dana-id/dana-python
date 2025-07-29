# QueryUserProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryUserProfileResponseResponse**](QueryUserProfileResponseResponse.md) |  | 
**signature** | **str** | Signature string | [optional] 

## Example

```python
from dana.widget.v1.models.query_user_profile_response import QueryUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUserProfileResponse from a JSON string
query_user_profile_response_instance = QueryUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print(QueryUserProfileResponse.to_json())

# convert the object into a dict
query_user_profile_response_dict = query_user_profile_response_instance.to_dict()
# create an instance of QueryUserProfileResponse from a dict
query_user_profile_response_from_dict = QueryUserProfileResponse.from_dict(query_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


