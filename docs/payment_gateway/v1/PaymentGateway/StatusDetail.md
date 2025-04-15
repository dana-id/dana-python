# StatusDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirement_status** | **str** | The status of acquirement | 
**frozen** | **bool** | Whether the frozen is true or not | [optional] 
**cancelled** | **bool** | Whether the cancelled is true or not | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.status_detail import StatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDetail from a JSON string
status_detail_instance = StatusDetail.from_json(json)
# print the JSON string representation of the object
print(StatusDetail.to_json())

# convert the object into a dict
status_detail_dict = status_detail_instance.to_dict()
# create an instance of StatusDetail from a dict
status_detail_from_dict = StatusDetail.from_dict(status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


