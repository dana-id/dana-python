# ApplyOTTRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | [**ApplyOTTRequestAdditionalInfo**](ApplyOTTRequestAdditionalInfo.md) |  | 

## Example

```python
from dana.ipg.v1.models.apply_ott_request import ApplyOTTRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyOTTRequest from a JSON string
apply_ott_request_instance = ApplyOTTRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyOTTRequest.to_json())

# convert the object into a dict
apply_ott_request_dict = apply_ott_request_instance.to_dict()
# create an instance of ApplyOTTRequest from a dict
apply_ott_request_from_dict = ApplyOTTRequest.from_dict(apply_ott_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


