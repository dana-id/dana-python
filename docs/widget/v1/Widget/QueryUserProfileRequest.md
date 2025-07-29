# QueryUserProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_resources** | **List[str]** | The resource type list that the merchant server wants to get from DANA | 

## Example

```python
from dana.widget.v1.models.query_user_profile_request import QueryUserProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUserProfileRequest from a JSON string
query_user_profile_request_instance = QueryUserProfileRequest.from_json(json)
# print the JSON string representation of the object
print(QueryUserProfileRequest.to_json())

# convert the object into a dict
query_user_profile_request_dict = query_user_profile_request_instance.to_dict()
# create an instance of QueryUserProfileRequest from a dict
query_user_profile_request_from_dict = QueryUserProfileRequest.from_dict(query_user_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


