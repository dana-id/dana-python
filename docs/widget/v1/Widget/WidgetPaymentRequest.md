# WidgetPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction | 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** |  | [optional] 
**amount** | [**Money**](Money.md) |  | 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**valid_up_to** | **str** | The time when the payment will be automatically expired, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | 
**point_of_initiation** | **str** | Used for getting more info regarding source of request of the user | [optional] 
**disabled_pay_methods** | **str** | Payment method(s) that cannot be used for this payment | [optional] 
**pay_option_details** | [**List[PayOptionDetail]**](PayOptionDetail.md) | Payment option that will be used for this payment | [optional] 
**additional_info** | [**WidgetPaymentRequestAdditionalInfo**](WidgetPaymentRequestAdditionalInfo.md) |  | 
**url_params** | [**List[UrlParam]**](UrlParam.md) | Notify URL that DANA must send the payment notification to | [optional] 

## Example

```python
from dana.widget.v1.models.widget_payment_request import WidgetPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPaymentRequest from a JSON string
widget_payment_request_instance = WidgetPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(WidgetPaymentRequest.to_json())

# convert the object into a dict
widget_payment_request_dict = widget_payment_request_instance.to_dict()
# create an instance of WidgetPaymentRequest from a dict
widget_payment_request_from_dict = WidgetPaymentRequest.from_dict(widget_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


