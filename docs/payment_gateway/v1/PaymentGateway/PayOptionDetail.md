# PayOptionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_method** | **str** |  | 
**pay_option** | **str** |  | 
**trans_amount** | [**Money**](Money.md) |  | 
**fee_amount** | [**Money**](Money.md) |  | [optional] 
**card_token** | **str** |  | [optional] 
**merchant_token** | **str** |  | [optional] 
**additional_info** | [**PayOptionAdditionalInfo**](PayOptionAdditionalInfo.md) |  | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.pay_option_detail import PayOptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PayOptionDetail from a JSON string
pay_option_detail_instance = PayOptionDetail.from_json(json)
# print the JSON string representation of the object
print(PayOptionDetail.to_json())

# convert the object into a dict
pay_option_detail_dict = pay_option_detail_instance.to_dict()
# create an instance of PayOptionDetail from a dict
pay_option_detail_from_dict = PayOptionDetail.from_dict(pay_option_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


