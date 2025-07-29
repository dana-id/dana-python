# InternationalOrderInfoExchangeRate

Define the detail of exchange rate information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **str** | Rate of exchange value represents the relation between two currencies. For example, 15917.2690 indicates that one USD is equivalent to 15917.2690 IDR | [optional] 
**exchange_relation** | **str** | Exchange rate between two currencies. For example USD/IDR, refers to how much of one currency (in this case, Indonesian Rupiah or IDR) can be exchanged for one unit of another currency (in this case, US Dollar or USD) | [optional] 

## Example

```python
from dana.widget.v1.models.international_order_info_exchange_rate import InternationalOrderInfoExchangeRate

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalOrderInfoExchangeRate from a JSON string
international_order_info_exchange_rate_instance = InternationalOrderInfoExchangeRate.from_json(json)
# print the JSON string representation of the object
print(InternationalOrderInfoExchangeRate.to_json())

# convert the object into a dict
international_order_info_exchange_rate_dict = international_order_info_exchange_rate_instance.to_dict()
# create an instance of InternationalOrderInfoExchangeRate from a dict
international_order_info_exchange_rate_from_dict = InternationalOrderInfoExchangeRate.from_dict(international_order_info_exchange_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


