# QueryUserProfileResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryUserProfileResponseResponseHead**](QueryUserProfileResponseResponseHead.md) |  | 
**body** | [**QueryUserProfileResponseResponseBody**](QueryUserProfileResponseResponseBody.md) |  | 

## Example

```python
from dana.widget.v1.models.query_user_profile_response_response import QueryUserProfileResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUserProfileResponseResponse from a JSON string
query_user_profile_response_response_instance = QueryUserProfileResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryUserProfileResponseResponse.to_json())

# convert the object into a dict
query_user_profile_response_response_dict = query_user_profile_response_response_instance.to_dict()
# create an instance of QueryUserProfileResponseResponse from a dict
query_user_profile_response_response_from_dict = QueryUserProfileResponseResponse.from_dict(query_user_profile_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


