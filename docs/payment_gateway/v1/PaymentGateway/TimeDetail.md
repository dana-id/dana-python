# TimeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **str** | Time of created order, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**expiry_time** | **str** | Time of expiry order, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**paid_times** | **List[str]** | Time of paid order, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**confirmed_times** | **List[str]** | Time of confirmed order, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**cancelled_time** | **str** | Time of cancelled order, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.time_detail import TimeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDetail from a JSON string
time_detail_instance = TimeDetail.from_json(json)
# print the JSON string representation of the object
print(TimeDetail.to_json())

# convert the object into a dict
time_detail_dict = time_detail_instance.to_dict()
# create an instance of TimeDetail from a dict
time_detail_from_dict = TimeDetail.from_dict(time_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


