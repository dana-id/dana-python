# AuditInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_reason** | **str** | Action trigger reason | [optional] 
**third_client_id** | **str** | Third party client identifier | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.audit_info import AuditInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuditInfo from a JSON string
audit_info_instance = AuditInfo.from_json(json)
# print the JSON string representation of the object
print(AuditInfo.to_json())

# convert the object into a dict
audit_info_dict = audit_info_instance.to_dict()
# create an instance of AuditInfo from a dict
audit_info_from_dict = AuditInfo.from_dict(audit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


