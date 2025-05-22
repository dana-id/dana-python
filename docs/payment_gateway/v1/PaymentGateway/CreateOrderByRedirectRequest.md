# CreateOrderByRedirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | [**CreateOrderByRedirectAdditionalInfo**](CreateOrderByRedirectAdditionalInfo.md) |  | [optional] 
**partner_reference_no** | **str** | Transaction identifier on partner system | 
**merchant_id** | **str** | Merchant identifier that is unique per each merchant | 
**sub_merchant_id** | **str** | Information of sub merchant identifier | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO<br />  | 
**external_store_id** | **str** | Store identifier to indicate to which store this payment belongs to | [optional] 
**valid_up_to** | **str** | The time when the payment will be automatically expired, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**disabled_pay_methods** | **str** | Payment method(s) that cannot be used for this | [optional] 
**url_params** | [**List[UrlParam]**](UrlParam.md) | Notify URL that DANA must send the payment notification to | 

## Example

```python
from dana.payment_gateway.v1.models.create_order_by_redirect_request import CreateOrderByRedirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderByRedirectRequest from a JSON string
create_order_by_redirect_request_instance = CreateOrderByRedirectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderByRedirectRequest.to_json())

# convert the object into a dict
create_order_by_redirect_request_dict = create_order_by_redirect_request_instance.to_dict()
# create an instance of CreateOrderByRedirectRequest from a dict
create_order_by_redirect_request_from_dict = CreateOrderByRedirectRequest.from_dict(create_order_by_redirect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


