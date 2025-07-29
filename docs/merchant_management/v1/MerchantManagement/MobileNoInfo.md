# MobileNoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_no** | **str** | Mobile number. Accepted formats: 0xxxxxxxx, 62xxxxxxx, 62-xxxxxxx, +62xxxxxx | [optional] 
**mobile_id** | **str** | Mobile ID | [optional] 
**verified** | **str** | Verification status | [optional] 

## Example

```python
from dana.merchant_management.v1.models.mobile_no_info import MobileNoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MobileNoInfo from a JSON string
mobile_no_info_instance = MobileNoInfo.from_json(json)
# print the JSON string representation of the object
print(MobileNoInfo.to_json())

# convert the object into a dict
mobile_no_info_dict = mobile_no_info_instance.to_dict()
# create an instance of MobileNoInfo from a dict
mobile_no_info_from_dict = MobileNoInfo.from_dict(mobile_no_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


