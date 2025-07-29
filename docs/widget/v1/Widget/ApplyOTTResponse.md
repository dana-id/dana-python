# ApplyOTTResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. https://dashboard.dana.id/api-docs/read/109#HTML-API-ApplyOTT-ResponseCodeandMessage | 
**response_message** | **str** | Response message. https://dashboard.dana.id/api-docs/read/109#HTML-API-ApplyOTT-ResponseCodeandMessage | 
**user_resources** | [**List[ApplyOTTResponseUserResourcesInner]**](ApplyOTTResponseUserResourcesInner.md) | User resources | 
**additional_info** | **object** | Additional information | [optional] 

## Example

```python
from dana.widget.v1.models.apply_ott_response import ApplyOTTResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyOTTResponse from a JSON string
apply_ott_response_instance = ApplyOTTResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyOTTResponse.to_json())

# convert the object into a dict
apply_ott_response_dict = apply_ott_response_instance.to_dict()
# create an instance of ApplyOTTResponse from a dict
apply_ott_response_from_dict = ApplyOTTResponse.from_dict(apply_ott_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


