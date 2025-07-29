# UpdateShopResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**UpdateShopResponseResponseHead**](UpdateShopResponseResponseHead.md) |  | 
**body** | [**UpdateDivisionResponseResponseBody**](UpdateDivisionResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.update_shop_response_response import UpdateShopResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShopResponseResponse from a JSON string
update_shop_response_response_instance = UpdateShopResponseResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateShopResponseResponse.to_json())

# convert the object into a dict
update_shop_response_response_dict = update_shop_response_response_instance.to_dict()
# create an instance of UpdateShopResponseResponse from a dict
update_shop_response_response_from_dict = UpdateShopResponseResponse.from_dict(update_shop_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


