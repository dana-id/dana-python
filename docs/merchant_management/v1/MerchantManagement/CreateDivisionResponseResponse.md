# CreateDivisionResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**CreateDivisionResponseResponseHead**](CreateDivisionResponseResponseHead.md) |  | 
**body** | [**CreateDivisionResponseResponseBody**](CreateDivisionResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.create_division_response_response import CreateDivisionResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDivisionResponseResponse from a JSON string
create_division_response_response_instance = CreateDivisionResponseResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDivisionResponseResponse.to_json())

# convert the object into a dict
create_division_response_response_dict = create_division_response_response_instance.to_dict()
# create an instance of CreateDivisionResponseResponse from a dict
create_division_response_response_from_dict = CreateDivisionResponseResponse.from_dict(create_division_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


