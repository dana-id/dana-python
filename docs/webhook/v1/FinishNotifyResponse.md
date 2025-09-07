# FinishNotifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/123#HTML-API-FinishNotify-ResponseCodeandMessage | 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/123#HTML-API-FinishNotify-ResponseCodeandMessage | 

## Example

```python
from dana.webhook.finish_notify_response import FinishNotifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinishNotifyResponse from a JSON string
finish_notify_response_instance = FinishNotifyResponse.from_json(json)
# print the JSON string representation of the object
print(FinishNotifyResponse.to_json())

# convert the object into a dict
finish_notify_response_dict = finish_notify_response_instance.to_dict()
# create an instance of FinishNotifyResponse from a dict
finish_notify_response_from_dict = FinishNotifyResponse.from_dict(finish_notify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


