# BusinessDocs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_type** | **str** | Document type. \&quot;individu\&quot; entity can only use KTP and SIM. Other entities can use SIUP and NIB | [optional] 
**doc_id** | **str** | Document ID | [optional] 
**doc_file** | **str** | Document file encoded in base64 | [optional] 

## Example

```python
from dana.merchant_management.v1.models.business_docs import BusinessDocs

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDocs from a JSON string
business_docs_instance = BusinessDocs.from_json(json)
# print the JSON string representation of the object
print(BusinessDocs.to_json())

# convert the object into a dict
business_docs_dict = business_docs_instance.to_dict()
# create an instance of BusinessDocs from a dict
business_docs_from_dict = BusinessDocs.from_dict(business_docs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


