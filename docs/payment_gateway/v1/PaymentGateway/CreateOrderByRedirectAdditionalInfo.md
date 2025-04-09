# CreateOrderByRedirectAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcc** | **str** |  | 
**extend_info** | **str** |  | [optional] 
**env_info** | [**EnvInfo**](EnvInfo.md) |  | 
**order** | [**OrderRedirectObject**](OrderRedirectObject.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.create_order_by_redirect_additional_info import CreateOrderByRedirectAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderByRedirectAdditionalInfo from a JSON string
create_order_by_redirect_additional_info_instance = CreateOrderByRedirectAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(CreateOrderByRedirectAdditionalInfo.to_json())

# convert the object into a dict
create_order_by_redirect_additional_info_dict = create_order_by_redirect_additional_info_instance.to_dict()
# create an instance of CreateOrderByRedirectAdditionalInfo from a dict
create_order_by_redirect_additional_info_from_dict = CreateOrderByRedirectAdditionalInfo.from_dict(create_order_by_redirect_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


