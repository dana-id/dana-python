# CreateShopResponseResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_info** | [**ResultInfo**](ResultInfo.md) |  | 
**shop_id** | **str** | The shop ID that was created. Present when resultCodeId is 00000000 | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_shop_response_response_body import CreateShopResponseResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShopResponseResponseBody from a JSON string
create_shop_response_response_body_instance = CreateShopResponseResponseBody.from_json(json)
# print the JSON string representation of the object
print(CreateShopResponseResponseBody.to_json())

# convert the object into a dict
create_shop_response_response_body_dict = create_shop_response_response_body_instance.to_dict()
# create an instance of CreateShopResponseResponseBody from a dict
create_shop_response_response_body_from_dict = CreateShopResponseResponseBody.from_dict(create_shop_response_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


