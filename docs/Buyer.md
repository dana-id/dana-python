# Buyer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_user_type** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**external_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from dana_python.payment_gateway.payment_gateway.models.buyer import Buyer

# TODO update the JSON string below
json = "{}"
# create an instance of Buyer from a JSON string
buyer_instance = Buyer.from_json(json)
# print the JSON string representation of the object
print(Buyer.to_json())

# convert the object into a dict
buyer_dict = buyer_instance.to_dict()
# create an instance of Buyer from a dict
buyer_from_dict = Buyer.from_dict(buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


