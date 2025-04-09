# UrlParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 
**is_deeplink** | **str** |  | 

## Example

```python
from dana.payment_gateway.v1.models.url_param import UrlParam

# TODO update the JSON string below
json = "{}"
# create an instance of UrlParam from a JSON string
url_param_instance = UrlParam.from_json(json)
# print the JSON string representation of the object
print(UrlParam.to_json())

# convert the object into a dict
url_param_dict = url_param_instance.to_dict()
# create an instance of UrlParam from a dict
url_param_from_dict = UrlParam.from_dict(url_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


