# UpdateShopResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**UpdateShopResponseResponse**](UpdateShopResponseResponse.md) |  | 
**signature** | **str** | Signature | [optional] 

## Example

```python
from dana.merchant_management.v1.models.update_shop_response import UpdateShopResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShopResponse from a JSON string
update_shop_response_instance = UpdateShopResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateShopResponse.to_json())

# convert the object into a dict
update_shop_response_dict = update_shop_response_instance.to_dict()
# create an instance of UpdateShopResponse from a dict
update_shop_response_from_dict = UpdateShopResponse.from_dict(update_shop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


