# QueryMerchantInfoResponseResponseHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | API version | [optional] [default to '2.0']
**function** | **str** | API interface | [optional] 
**client_id** | **str** | Client ID provided by DANA, used to identify partner and application system | [optional] 
**resp_time** | **str** | DateTime with timezone (ISO-8601), GMT+7 (Jakarta time) | [optional] 
**req_msg_id** | **str** | Request message ID | [optional] 
**client_secret** | **str** | As a secret key of client. Assigned client secret during registration | [optional] 
**reserve** | **object** |  | [optional] 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_info_response_response_head import QueryMerchantInfoResponseResponseHead

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantInfoResponseResponseHead from a JSON string
query_merchant_info_response_response_head_instance = QueryMerchantInfoResponseResponseHead.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantInfoResponseResponseHead.to_json())

# convert the object into a dict
query_merchant_info_response_response_head_dict = query_merchant_info_response_response_head_instance.to_dict()
# create an instance of QueryMerchantInfoResponseResponseHead from a dict
query_merchant_info_response_response_head_from_dict = QueryMerchantInfoResponseResponseHead.from_dict(query_merchant_info_response_response_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


