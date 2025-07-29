# CreateShopResponseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head** | [**CreateShopResponseResponseHead**](CreateShopResponseResponseHead.md) |  | 
**body** | [**CreateShopResponseResponseBody**](CreateShopResponseResponseBody.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.create_shop_response_response import CreateShopResponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShopResponseResponse from a JSON string
create_shop_response_response_instance = CreateShopResponseResponse.from_json(json)
# print the JSON string representation of the object
print(CreateShopResponseResponse.to_json())

# convert the object into a dict
create_shop_response_response_dict = create_shop_response_response_instance.to_dict()
# create an instance of CreateShopResponseResponse from a dict
create_shop_response_response_from_dict = CreateShopResponseResponse.from_dict(create_shop_response_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


