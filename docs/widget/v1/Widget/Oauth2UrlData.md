# Oauth2UrlData

Data needed to construct Oauth2Url

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Identifier from merchant | 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**seamless_data** | [**Oauth2UrlDataSeamlessData**](Oauth2UrlDataSeamlessData.md) |  | [optional] 
**scopes** | **List[str]** | The scopes of the authorization | [optional] 
**redirect_url** | **str** | When user authorization is success, the user will be redirected to this URL | 
**state** | **str** | Random string for CSRF protection purposes | [optional] 
**lang** | **str** | Service language code. ISO 639-1 | [optional] [default to 'id']
**allow_registration** | **str** | If value equals true, provider may enable registration process during binding. Default true | [optional] [default to 'true']
**mode** | **str** | Mode of the authorization. The possible values are API or DEEPLINK | [optional] 

## Example

```python
from dana.widget.v1.models.oauth2_url_data import Oauth2UrlData

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2UrlData from a JSON string
oauth2_url_data_instance = Oauth2UrlData.from_json(json)
# print the JSON string representation of the object
print(Oauth2UrlData.to_json())

# convert the object into a dict
oauth2_url_data_dict = oauth2_url_data_instance.to_dict()
# create an instance of Oauth2UrlData from a dict
oauth2_url_data_from_dict = Oauth2UrlData.from_dict(oauth2_url_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


