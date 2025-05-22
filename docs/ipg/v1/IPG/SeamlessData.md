# SeamlessData

Schema that documents the fields that can be included in the seamlessData JSON object (which is sent as a URL-encoded string)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_uid** | **str** | External user identifier | [optional] 
**mobile** | **str** | User mobile number | [optional] 
**mobile_number** | **str** | Alternative field name for mobile number | [optional] 
**req_time** | **datetime** | Request timestamp | [optional] 
**verified_time** | **str** | Verification timestamp | [optional] 
**req_msg_id** | **str** | Request message ID | [optional] 
**skip_consult_register** | **bool** | Whether to skip consultation registration | [optional] 
**biz_scenario** | **str** | Business scenario | [optional] 

## Example

```python
from dana.ipg.v1.models.seamless_data import SeamlessData

# TODO update the JSON string below
json = "{}"
# create an instance of SeamlessData from a JSON string
seamless_data_instance = SeamlessData.from_json(json)
# print the JSON string representation of the object
print(SeamlessData.to_json())

# convert the object into a dict
seamless_data_dict = seamless_data_instance.to_dict()
# create an instance of SeamlessData from a dict
seamless_data_from_dict = SeamlessData.from_dict(seamless_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


