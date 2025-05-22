# EnvInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | [optional] 
**token_id** | **str** | Token identifier | [optional] 
**website_language** | **str** | Website language | [optional] 
**client_ip** | **str** | Client IP address | [optional] 
**os_type** | **str** | Operating system type | [optional] 
**app_version** | **str** | App version | [optional] 
**sdk_version** | **str** | SDK version | [optional] 
**source_platform** | **str** | The source platform is always independent payment gateway (IPG) | 
**order_os_type** | **str** | Order operating system type | [optional] 
**merchant_app_version** | **str** | Merchant App version | [optional] 
**terminal_type** | **str** | Terminal type. The enums:<br /> * APP - Mobile Application<br /> * WEB - Browser Web<br /> * WAP - Mobile Wap<br /> * SYSTEM - System Call<br />  | 
**order_terminal_type** | **str** | Order terminal type. The enums:<br /> * APP - Mobile Application<br /> * WEB - Browser Web<br /> * WAP - Mobile Wap<br /> * SYSTEM - System Call<br />  | [optional] 
**extend_info** | **str** | Extend information | [optional] 

## Example

```python
from dana.ipg.v1.models.env_info import EnvInfo

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


