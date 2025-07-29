# ResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_status** | **str** | Result status (S&#x3D;Success, F&#x3D;Failure, U&#x3D;Unknown) | 
**result_code_id** | **str** | Result code identifier | 
**result_code** | **str** | Result code | 
**result_msg** | **str** | Result message | 

## Example

```python
from dana.widget.v1.models.result_info import ResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResultInfo from a JSON string
result_info_instance = ResultInfo.from_json(json)
# print the JSON string representation of the object
print(ResultInfo.to_json())

# convert the object into a dict
result_info_dict = result_info_instance.to_dict()
# create an instance of ResultInfo from a dict
result_info_from_dict = ResultInfo.from_dict(result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


