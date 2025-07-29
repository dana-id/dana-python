# UserName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 

## Example

```python
from dana.merchant_management.v1.models.user_name import UserName

# TODO update the JSON string below
json = "{}"
# create an instance of UserName from a JSON string
user_name_instance = UserName.from_json(json)
# print the JSON string representation of the object
print(UserName.to_json())

# convert the object into a dict
user_name_dict = user_name_instance.to_dict()
# create an instance of UserName from a dict
user_name_from_dict = UserName.from_dict(user_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


