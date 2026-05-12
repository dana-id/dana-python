# MemberAssetResultInfo

Result information for member asset Open APIs (`resultInfo` per DANA spec)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_status** | **str** | Request status (&#x60;ResultStatus&#x60;). S&#x3D;Success, F&#x3D;Failure, U&#x3D;Unknown | 
**result_code_id** | **str** | Result code identifier (&#x60;ResultCodeId&#x60;) | 
**result_code** | **str** | Result code (&#x60;ResultCode&#x60;) | 
**result_msg** | **str** | Result message (&#x60;ResultMsg&#x60;). Optional per API contract | [optional] 

## Example

```python
from dana.merchant_management.v1.models.member_asset_result_info import MemberAssetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemberAssetResultInfo from a JSON string
member_asset_result_info_instance = MemberAssetResultInfo.from_json(json)
# print the JSON string representation of the object
print(MemberAssetResultInfo.to_json())

# convert the object into a dict
member_asset_result_info_dict = member_asset_result_info_instance.to_dict()
# create an instance of MemberAssetResultInfo from a dict
member_asset_result_info_from_dict = MemberAssetResultInfo.from_dict(member_asset_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


