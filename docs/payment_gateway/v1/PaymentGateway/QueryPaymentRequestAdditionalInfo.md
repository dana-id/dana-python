# QueryPaymentRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_scenario** | **str** | Additional information of business scenario | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.query_payment_request_additional_info import QueryPaymentRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPaymentRequestAdditionalInfo from a JSON string
query_payment_request_additional_info_instance = QueryPaymentRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(QueryPaymentRequestAdditionalInfo.to_json())

# convert the object into a dict
query_payment_request_additional_info_dict = query_payment_request_additional_info_instance.to_dict()
# create an instance of QueryPaymentRequestAdditionalInfo from a dict
query_payment_request_additional_info_from_dict = QueryPaymentRequestAdditionalInfo.from_dict(query_payment_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


