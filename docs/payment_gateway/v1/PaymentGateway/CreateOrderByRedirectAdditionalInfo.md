# CreateOrderByRedirectAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcc** | **str** | Additional information of merchant category code. This parameter is used to identify the type of business in which a merchant is engaged. Refer to Details of https://dashboard.dana.id/api-docs/read/197#OpenAPI-MerchantCategoryCode | 
**extend_info** | **str** | Additional information of extend such as partner passthrough and risk information | [optional] 
**env_info** | [**EnvInfo**](EnvInfo.md) | Additional information of environment info | 
**order** | [**OrderRedirectObject**](OrderRedirectObject.md) | Additional information of order | [optional] 

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


