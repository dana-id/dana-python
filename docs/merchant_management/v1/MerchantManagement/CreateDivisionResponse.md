# CreateDivisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateDivisionResponseResponse**](CreateDivisionResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_division_response import CreateDivisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDivisionResponse from a JSON string
create_division_response_instance = CreateDivisionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDivisionResponse.to_json())

# convert the object into a dict
create_division_response_dict = create_division_response_instance.to_dict()
# create an instance of CreateDivisionResponse from a dict
create_division_response_from_dict = CreateDivisionResponse.from_dict(create_division_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


