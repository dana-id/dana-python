# UpdateDivisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**UpdateDivisionResponseResponse**](UpdateDivisionResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.update_division_response import UpdateDivisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDivisionResponse from a JSON string
update_division_response_instance = UpdateDivisionResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDivisionResponse.to_json())

# convert the object into a dict
update_division_response_dict = update_division_response_instance.to_dict()
# create an instance of UpdateDivisionResponse from a dict
update_division_response_from_dict = UpdateDivisionResponse.from_dict(update_division_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


