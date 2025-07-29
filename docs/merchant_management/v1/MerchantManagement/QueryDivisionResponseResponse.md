# QueryDivisionResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**QueryDivisionResponseResponseHead**](QueryDivisionResponseResponseHead.md) |  | 
**body** | [**QueryDivisionResponseResponseBody**](QueryDivisionResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.query_division_response_response import QueryDivisionResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDivisionResponseResponse from a JSON string
query_division_response_response_instance = QueryDivisionResponseResponse.from_json(json)
# print the JSON string representation of the object
print(QueryDivisionResponseResponse.to_json())

# convert the object into a dict
query_division_response_response_dict = query_division_response_response_instance.to_dict()
# create an instance of QueryDivisionResponseResponse from a dict
query_division_response_response_from_dict = QueryDivisionResponseResponse.from_dict(query_division_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


