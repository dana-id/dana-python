# PicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pic_name** | **str** | PIC name | [optional] 
**pic_position** | **str** | PIC position | [optional] 

## Example

```python
from dana.merchant_management.v1.models.pic_info import PicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PicInfo from a JSON string
pic_info_instance = PicInfo.from_json(json)
# print the JSON string representation of the object
print(PicInfo.to_json())

# convert the object into a dict
pic_info_dict = pic_info_instance.to_dict()
# create an instance of PicInfo from a dict
pic_info_from_dict = PicInfo.from_dict(pic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


