# VirtualAccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_account_code** | **str** | Virtual account code. Present if successfully processed and payment method is VIRTUAL_ACCOUNT | [optional] 
**virtual_account_expiry_time** | **str** | Expiry time of virtual account, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time). Present if successfully processed and payment method is VIRTUAL_ACCOUNT | [optional] 
**signature** | **str** | Signature of virtual account. Present if successfully processed and payment method is VIRTUAL_ACCOUNT | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.virtual_account_info import VirtualAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountInfo from a JSON string
virtual_account_info_instance = VirtualAccountInfo.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountInfo.to_json())

# convert the object into a dict
virtual_account_info_dict = virtual_account_info_instance.to_dict()
# create an instance of VirtualAccountInfo from a dict
virtual_account_info_from_dict = VirtualAccountInfo.from_dict(virtual_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


