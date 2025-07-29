# CreateDivisionResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**division_id** | **str** | Division identifier. Present when successfully processed | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_division_response_response_body import CreateDivisionResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDivisionResponseResponseBody from a JSON string
create_division_response_response_body_instance = CreateDivisionResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(CreateDivisionResponseResponseBody.to_json())

# convert the object into a dict
create_division_response_response_body_dict = create_division_response_response_body_instance.to_dict()
# create an instance of CreateDivisionResponseResponseBody from a dict
create_division_response_response_body_from_dict = CreateDivisionResponseResponseBody.from_dict(create_division_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


