# CreateOrderResponseAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_code** | **str** | Additional information of payment code. Only use for Payment Gateway service. Present if payment using Virtual Account/QRIS | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.create_order_response_additional_info import CreateOrderResponseAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponseAdditionalInfo from a JSON string
create_order_response_additional_info_instance = CreateOrderResponseAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponseAdditionalInfo.to_json())

# convert the object into a dict
create_order_response_additional_info_dict = create_order_response_additional_info_instance.to_dict()
# create an instance of CreateOrderResponseAdditionalInfo from a dict
create_order_response_additional_info_from_dict = CreateOrderResponseAdditionalInfo.from_dict(create_order_response_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


