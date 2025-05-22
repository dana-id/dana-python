# Money


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of amount. Following ISO-4217, for IDR the value includes 2 decimal digits separated with point e.g. ,IDR 10.000,- will be placed with 10000.00 | 
**currency** | **str** | Currency. Following ISO-4217 | 

## Example

```python
from dana.ipg.v1.models.money import Money

# TODO update the JSON string below
json = "{}"
# create an instance of Money from a JSON string
money_instance = Money.from_json(json)
# print the JSON string representation of the object
print(Money.to_json())

# convert the object into a dict
money_dict = money_instance.to_dict()
# create an instance of Money from a dict
money_from_dict = Money.from_dict(money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


