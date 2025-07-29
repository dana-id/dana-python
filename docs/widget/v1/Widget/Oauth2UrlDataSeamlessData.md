# Oauth2UrlDataSeamlessData

Option for binding process.Please refer sample below to know how to include seamlessData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biz_scenario** | **str** | User’s bizScenario | [optional] 
**mobile_number** | **str** | User&#39;s phone number. If this field is filled in, the user must log in with the number that has been included | [optional] 
**verified_time** | **str** | Value which states that the mobile number that has been included in seamlessData has verified ownership and does not require OTP verification by the provider, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**external_uid** | **str** | User identifier on partner application | [optional] 
**device_id** | **str** | User&#39;s device identifier | [optional] 
**skip_register_consult** | **bool** | Identifier to differentiate seamless registration flow. The possible values are true or false | [optional] 

## Example

```python
from dana.widget.v1.models.oauth2_url_data_seamless_data import Oauth2UrlDataSeamlessData

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2UrlDataSeamlessData from a JSON string
oauth2_url_data_seamless_data_instance = Oauth2UrlDataSeamlessData.from_json(json)
# print the JSON string representation of the object
print(Oauth2UrlDataSeamlessData.to_json())

# convert the object into a dict
oauth2_url_data_seamless_data_dict = oauth2_url_data_seamless_data_instance.to_dict()
# create an instance of Oauth2UrlDataSeamlessData from a dict
oauth2_url_data_seamless_data_from_dict = Oauth2UrlDataSeamlessData.from_dict(oauth2_url_data_seamless_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


