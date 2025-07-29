# UpdateDivisionResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**UpdateDivisionResponseResponseHead**](UpdateDivisionResponseResponseHead.md) |  | 
**body** | [**UpdateDivisionResponseResponseBody**](UpdateDivisionResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.update_division_response_response import UpdateDivisionResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDivisionResponseResponse from a JSON string
update_division_response_response_instance = UpdateDivisionResponseResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDivisionResponseResponse.to_json())

# convert the object into a dict
update_division_response_response_dict = update_division_response_response_instance.to_dict()
# create an instance of UpdateDivisionResponseResponse from a dict
update_division_response_response_from_dict = UpdateDivisionResponseResponse.from_dict(update_division_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


