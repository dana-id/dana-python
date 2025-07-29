# CreateShopResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateShopResponseResponse**](CreateShopResponseResponse.md) |  | 

## Example

```python
from dana.merchant_management.v1.models.create_shop_response import CreateShopResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShopResponse from a JSON string
create_shop_response_instance = CreateShopResponse.from_json(json)
# print the JSON string representation of the object
print(CreateShopResponse.to_json())

# convert the object into a dict
create_shop_response_dict = create_shop_response_instance.to_dict()
# create an instance of CreateShopResponse from a dict
create_shop_response_from_dict = CreateShopResponse.from_dict(create_shop_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


