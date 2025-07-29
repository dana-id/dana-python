# CreateDivisionRequestExtInfo

Extended information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pic_email** | **str** | PIC email address | [optional] 
**pic_phonenumber** | **str** | PIC phone number | [optional] 
**submitter_email** | **str** | Submitter email address | [optional] 
**goods_sold_type** | **str** | Type of goods sold | [optional] 
**usecase** | **str** | Use case type | [optional] 
**user_profiling** | **str** | User profiling type | [optional] 
**avg_ticket** | **str** | Average ticket size | [optional] 
**omzet** | **str** | Revenue range | [optional] 
**ext_urls** | **str** | External URLs | [optional] 
**brand_name** | **str** | Brand name | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_division_request_ext_info import CreateDivisionRequestExtInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDivisionRequestExtInfo from a JSON string
create_division_request_ext_info_instance = CreateDivisionRequestExtInfo.from_json(json)
# print the JSON string representation of the object
print(CreateDivisionRequestExtInfo.to_json())

# convert the object into a dict
create_division_request_ext_info_dict = create_division_request_ext_info_instance.to_dict()
# create an instance of CreateDivisionRequestExtInfo from a dict
create_division_request_ext_info_from_dict = CreateDivisionRequestExtInfo.from_dict(create_division_request_ext_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


