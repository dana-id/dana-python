# IPGPaymentRequestAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support_deep_link_checkout_url** | **str** | Additional information of deeplink checkout URL. For Mini Program, DANA will treat as false | [optional] 
**phone_number** | **str** | Additional information of user&#39;s phone number | [optional] 
**public_user_id** | **str** | Additional information of public user&#39;s identifier | [optional] 
**product_code** | **str** | Additional information of product code | 
**service_info** | [**ServiceInfo**](ServiceInfo.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | 
**mcc** | **str** | Additional information of merchant category code. This parameter is used to identify the type of business in which a merchant is engaged. | 
**env_info** | [**EnvInfo**](EnvInfo.md) |  | 
**extend_info** | **str** | Additional information of extend | [optional] 

## Example

```python
from dana.ipg.v1.models.ipg_payment_request_additional_info import IPGPaymentRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IPGPaymentRequestAdditionalInfo from a JSON string
ipg_payment_request_additional_info_instance = IPGPaymentRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(IPGPaymentRequestAdditionalInfo.to_json())

# convert the object into a dict
ipg_payment_request_additional_info_dict = ipg_payment_request_additional_info_instance.to_dict()
# create an instance of IPGPaymentRequestAdditionalInfo from a dict
ipg_payment_request_additional_info_from_dict = IPGPaymentRequestAdditionalInfo.from_dict(ipg_payment_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


