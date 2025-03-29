# EnvInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**website_language** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**os_type** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**sdk_version** | **str** |  | [optional] 
**source_platform** | **str** |  | 
**order_os_type** | **str** |  | [optional] 
**merchant_app_version** | **str** |  | [optional] 
**terminal_type** | **str** |  | 
**order_terminal_type** | **str** |  | 
**extend_info** | **str** |  | [optional] 

## Example

```python
from dana_python.payment_gateway.payment_gateway.models.env_info import EnvInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnvInfo from a JSON string
env_info_instance = EnvInfo.from_json(json)
# print the JSON string representation of the object
print(EnvInfo.to_json())

# convert the object into a dict
env_info_dict = env_info_instance.to_dict()
# create an instance of EnvInfo from a dict
env_info_from_dict = EnvInfo.from_dict(env_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


