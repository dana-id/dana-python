# ApplyOTTResponseUserResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Information of resource type. List of resource retrieved - OTT | [optional] 
**value** | **str** | Value of OTT | [optional] 

## Example

```python
from dana.ipg.v1.models.apply_ott_response_user_resources_inner import ApplyOTTResponseUserResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyOTTResponseUserResourcesInner from a JSON string
apply_ott_response_user_resources_inner_instance = ApplyOTTResponseUserResourcesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyOTTResponseUserResourcesInner.to_json())

# convert the object into a dict
apply_ott_response_user_resources_inner_dict = apply_ott_response_user_resources_inner_instance.to_dict()
# create an instance of ApplyOTTResponseUserResourcesInner from a dict
apply_ott_response_user_resources_inner_from_dict = ApplyOTTResponseUserResourcesInner.from_dict(apply_ott_response_user_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


