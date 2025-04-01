# ConsultPayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** |  | [optional] 
**response_message** | **str** | The response code - response message:<br /> * 2000000 - Successful<br /> * 4000000 - Bad Request - Retry request with proper parameter<br /> * 4000001 - Invalid format for certain field - Retry request with proper parameter<br /> * 4000002 - Missing or invalid format on mandatory field - Retry request with proper parameter<br /> * 4010000 - Signature is invalid - Retry request with proper parameter<br /> * 4030005 - Account or user status is abnormal - Retry request with proper parameter or can contact DANA to check the user/account status<br /> * 4030015 - Transaction not permitted - Retry request periodically or consult to DANA<br /> * 4040008 - Merchant does not exist or status abnormal - Retry request with proper parameter<br /> * 4290000 - Maximum transaction limit exceeded - Retry request periodically by sending same request payload<br /> * 5000000 - General error - Retry request periodically<br />  | [optional] 
**payment_infos** | [**List[PaymentInfo]**](PaymentInfo.md) |  | [optional] 

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


