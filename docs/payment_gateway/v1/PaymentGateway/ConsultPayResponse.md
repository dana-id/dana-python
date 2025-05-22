# ConsultPayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code. Refer to https://dashboard.dana.id/api-docs/read/237#paymentgatewayprod-ConsultPay-ResponseCodeandMessage | [optional] 
**response_message** | **str** | Response message. Refer to https://dashboard.dana.id/api-docs/read/237#paymentgatewayprod-ConsultPay-ResponseCodeandMessage | [optional] 
**payment_infos** | [**List[ConsultPayPaymentInfo]**](ConsultPayPaymentInfo.md) | Define list of payment information that includes payment method and payment option for transaction | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.consult_pay_response import ConsultPayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConsultPayResponse from a JSON string
consult_pay_response_instance = ConsultPayResponse.from_json(json)
# print the JSON string representation of the object
print(ConsultPayResponse.to_json())

# convert the object into a dict
consult_pay_response_dict = consult_pay_response_instance.to_dict()
# create an instance of ConsultPayResponse from a dict
consult_pay_response_from_dict = ConsultPayResponse.from_dict(consult_pay_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


