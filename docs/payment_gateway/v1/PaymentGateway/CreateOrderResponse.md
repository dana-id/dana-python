# CreateOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | Response code for the transaction result. Example values include:<br /> * 2005400 - Successful<br /> * 4005400 - Bad Request - Retry request with proper parameter<br /> * 4005401 - Invalid Field Format - Retry request with proper parameter<br /> * 4005402 - Invalid Mandatory Field - Retry request with proper parameter<br /> * 4015400 - Unauthorized. Invalid Signature - Retry request with proper parameter<br /> * 4035402 - Exceeds Transaction Amount Limit - Try to adjust the order amount<br /> * 4035405 - Do Not Honor - Retry request with proper parameter or can contact DANA to check the user/account status<br /> * 4035415 - Transaction Not Permitted - Retry request periodically or consult to DANA<br /> * 4045408 - Invalid Merchant - Retry request with proper parameter<br /> * 4045418 - Inconsistent Request - Retry with proper parameter<br /> * 4295400 - Too Many Requests - Retry request periodically by sending same request payload<br /> * 5005400 - General Error - Retry request periodically<br /> * 5005401 - Internal Server Error - Retry request periodically by sending same request payload<br />  | 
**response_message** | **str** | Message corresponding to the response code | 
**reference_no** | **str** | Transaction identifier on DANA system (present if successfully processed) | [optional] 
**partner_reference_no** | **str** | Transaction identifier on partner system | 
**web_redirect_url** | **str** | Checkout URL (present if payment method is not OVO/Virtual Account/QRIS) | [optional] 
**additional_info** | [**CreateOrderResponseAdditionalInfo**](CreateOrderResponseAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.create_order_response import CreateOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponse from a JSON string
create_order_response_instance = CreateOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponse.to_json())

# convert the object into a dict
create_order_response_dict = create_order_response_instance.to_dict()
# create an instance of CreateOrderResponse from a dict
create_order_response_from_dict = CreateOrderResponse.from_dict(create_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


