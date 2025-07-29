# WidgetPaymentResponse

Response object for Direct Debit Payment API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Refer to response code list:<br /> * 2005400 - Successful<br /> * 4005400 - Bad Request - Retry request with proper parameter<br /> * 4005401 - Invalid Field Format - Retry request with proper parameter<br /> * 4005402 - Invalid Mandatory Field - Retry request with proper parameter<br /> * 4015400 - Unauthorized. [reason] - Retry request with proper parameter<br /> * 4035402 - Exceeds Transaction Amount Limit - Try to adjust the order amount<br /> * 4035405 - Do Not Honor - Retry request with proper parameter or can contact DANA to check the user/account status<br /> * 4035415 - Transaction Not Permitted - Retry request periodically or consult to DANA<br /> * 4045408 - Invalid Merchant - Retry request with proper parameter<br /> * 4045418 - Inconsistent Request - Retry with proper parameter<br /> * 4295400 - Too Many Requests - Retry request periodically by sending same request payload<br /> * 5005400 - General Error - Retry request periodically<br /> * 5005401 - Internal Server Error - Retry request periodically by sending same request payload<br />  | 
**response_message** | **str** | Human readable response message | 
**reference_no** | **str** | Transaction identifier on DANA system, returned when transaction is successfully processed | [optional] 
**partner_reference_no** | **str** | Transaction identifier on partner system which assigned to each transaction | 
**web_redirect_url** | **str** | DANA checkout URL, returned when transaction is successfully processed | [optional] 
**additional_info** | **Dict[str, object]** | Additional information | [optional] 

## Example

```python
from dana.widget.v1.models.widget_payment_response import WidgetPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetPaymentResponse from a JSON string
widget_payment_response_instance = WidgetPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetPaymentResponse.to_json())

# convert the object into a dict
widget_payment_response_dict = widget_payment_response_instance.to_dict()
# create an instance of WidgetPaymentResponse from a dict
widget_payment_response_from_dict = WidgetPaymentResponse.from_dict(widget_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


