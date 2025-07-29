# WidgetPaymentRequestAdditionalInfo


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
from dana.widget.v1.models.widget_payment_request_additional_info import WidgetPaymentRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPaymentRequestAdditionalInfo from a JSON string
widget_payment_request_additional_info_instance = WidgetPaymentRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(WidgetPaymentRequestAdditionalInfo.to_json())

# convert the object into a dict
widget_payment_request_additional_info_dict = widget_payment_request_additional_info_instance.to_dict()
# create an instance of WidgetPaymentRequestAdditionalInfo from a dict
widget_payment_request_additional_info_from_dict = WidgetPaymentRequestAdditionalInfo.from_dict(widget_payment_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


