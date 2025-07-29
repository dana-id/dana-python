# QueryMerchantResourceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_merchant_id** | **str** | This is a merchantId of DANA | 
**merchant_resource_info_list** | **List[str]** | This is a constant merchant resource info request, currently available for value of constant these: MERCHANT_DEPOSIT_BALANCE MERCHANT_AVAILABLE_BALANCE MERCHANT_TOTAL_BALANCE value for this request can&#39;t be empty or wrong constant info  | 

## Example

```python
from dana.merchant_management.v1.models.query_merchant_resource_request import QueryMerchantResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantResourceRequest from a JSON string
query_merchant_resource_request_instance = QueryMerchantResourceRequest.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantResourceRequest.to_json())

# convert the object into a dict
query_merchant_resource_request_dict = query_merchant_resource_request_instance.to_dict()
# create an instance of QueryMerchantResourceRequest from a dict
query_merchant_resource_request_from_dict = QueryMerchantResourceRequest.from_dict(query_merchant_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


