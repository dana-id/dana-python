# QueryDivisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QueryDivisionResponseResponse**](QueryDivisionResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_division_response import QueryDivisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDivisionResponse from a JSON string
query_division_response_instance = QueryDivisionResponse.from_json(json)
# print the JSON string representation of the object
print(QueryDivisionResponse.to_json())

# convert the object into a dict
query_division_response_dict = query_division_response_instance.to_dict()
# create an instance of QueryDivisionResponse from a dict
query_division_response_from_dict = QueryDivisionResponse.from_dict(query_division_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


