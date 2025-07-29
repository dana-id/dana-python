# QueryUserProfileResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**user_resource_infos** | [**List[UserResourceInfo]**](UserResourceInfo.md) | The querying resource list value | [optional] 

## Example

```python
from dana.widget.v1.models.query_user_profile_response_response_body import QueryUserProfileResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUserProfileResponseResponseBody from a JSON string
query_user_profile_response_response_body_instance = QueryUserProfileResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryUserProfileResponseResponseBody.to_json())

# convert the object into a dict
query_user_profile_response_response_body_dict = query_user_profile_response_response_body_instance.to_dict()
# create an instance of QueryUserProfileResponseResponseBody from a dict
query_user_profile_response_response_body_from_dict = QueryUserProfileResponseResponseBody.from_dict(query_user_profile_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


