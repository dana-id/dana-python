# UserResourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Type of user resource | 
**value** | **str** | Resource value | 

## Example

```python
from dana.widget.v1.models.user_resource_info import UserResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourceInfo from a JSON string
user_resource_info_instance = UserResourceInfo.from_json(json)
# print the JSON string representation of the object
print(UserResourceInfo.to_json())

# convert the object into a dict
user_resource_info_dict = user_resource_info_instance.to_dict()
# create an instance of UserResourceInfo from a dict
user_resource_info_from_dict = UserResourceInfo.from_dict(user_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


