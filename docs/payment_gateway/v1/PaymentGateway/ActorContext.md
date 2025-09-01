# ActorContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_id** | **str** | Actor identifier | [optional] 
**actor_type** | **str** | Actor type. The enums:<br /> * USER - User<br /> * MERCHANT - Merchant<br /> * MERCHANT_OPERATOR - Merchant operator<br /> * BACK_OFFICE - Back office<br /> * SYSTEM - System<br />  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.actor_context import ActorContext

# TODO update the JSON string below
json = "{}"
# create an instance of ActorContext from a JSON string
actor_context_instance = ActorContext.from_json(json)
# print the JSON string representation of the object
print(ActorContext.to_json())

# convert the object into a dict
actor_context_dict = actor_context_instance.to_dict()
# create an instance of ActorContext from a dict
actor_context_from_dict = ActorContext.from_dict(actor_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


