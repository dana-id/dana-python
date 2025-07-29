# QueryDivisionResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**division_resource_info** | [**DivisionResourceInfo**](DivisionResourceInfo.md) |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_division_response_response_body import QueryDivisionResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDivisionResponseResponseBody from a JSON string
query_division_response_response_body_instance = QueryDivisionResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(QueryDivisionResponseResponseBody.to_json())

# convert the object into a dict
query_division_response_response_body_dict = query_division_response_response_body_instance.to_dict()
# create an instance of QueryDivisionResponseResponseBody from a dict
query_division_response_response_body_from_dict = QueryDivisionResponseResponseBody.from_dict(query_division_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


