# QueryUserProfileResponseResponseHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | API version | [optional] [default to '2.0']
**function** | **str** | API interface | [optional] 
**client_id** | **str** | Client ID provided by DANA, used to identify partner and application system | [optional] 
**resp_time** | **str** | Response time, dateTime with timezone, which follows the ISO-8601 standard. Refer to RFC 3339 Section 5.6 | [optional] 
**req_msg_id** | **str** | Each request will be assigned with a unique id (uuid) | [optional] 
**reserve** | **str** | Reserved for future implementation (Key/Value) | [optional] 

## Example

```python
from dana.widget.v1.models.query_user_profile_response_response_head import QueryUserProfileResponseResponseHead

# TODO update the JSON string below
json = "{}"
# create an instance of QueryUserProfileResponseResponseHead from a JSON string
query_user_profile_response_response_head_instance = QueryUserProfileResponseResponseHead.from_json(json)
# print the JSON string representation of the object
print(QueryUserProfileResponseResponseHead.to_json())

# convert the object into a dict
query_user_profile_response_response_head_dict = query_user_profile_response_response_head_instance.to_dict()
# create an instance of QueryUserProfileResponseResponseHead from a dict
query_user_profile_response_response_head_from_dict = QueryUserProfileResponseResponseHead.from_dict(query_user_profile_response_response_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


