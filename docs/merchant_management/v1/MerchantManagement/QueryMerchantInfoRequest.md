# QueryMerchantInfoRequest

Business fields mapped to `request.body` in the JSON envelope (head/signature are handled by the client/runtime).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | Login identifier value (format depends on &#x60;loginType&#x60;, e.g. &#x60;{countryCode}-{mobileNo}&#x60; when &#x60;loginType&#x60; is &#x60;MOBILE_NO&#x60;) | 
**login_type** | **str** | Login identifier type used with &#x60;roleId&#x60; | 
**is_query_account** | **bool** | When true, include merchant account list in the response | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_info_request import QueryMerchantInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantInfoRequest from a JSON string
query_merchant_info_request_instance = QueryMerchantInfoRequest.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantInfoRequest.to_json())

# convert the object into a dict
query_merchant_info_request_dict = query_merchant_info_request_instance.to_dict()
# create an instance of QueryMerchantInfoRequest from a dict
query_merchant_info_request_from_dict = QueryMerchantInfoRequest.from_dict(query_merchant_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


