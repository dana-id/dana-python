# QueryPaymentResponseAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier | [optional] 
**buyer** | [**Buyer**](Buyer.md) |  | [optional] 
**seller** | [**Seller**](Seller.md) |  | [optional] 
**amount_detail** | [**AmountDetail**](AmountDetail.md) |  | [optional] 
**time_detail** | [**TimeDetail**](TimeDetail.md) |  | [optional] 
**goods** | [**List[Goods]**](Goods.md) | Additional information of goods | [optional] 
**shipping_info** | [**List[ShippingInfo]**](ShippingInfo.md) | Additional information of shipping | [optional] 
**order_memo** | **str** | Additional information of memo | [optional] 
**payment_views** | [**List[PaymentView]**](PaymentView.md) | Additional information of payment views | [optional] 
**extend_info** | **str** | Additional information of extend | [optional] 
**status_detail** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**close_reason** | **str** | Additional information of close reason | [optional] 
**virtual_account_info** | [**VirtualAccountInfo**](VirtualAccountInfo.md) |  | [optional] 

## Example

```python
from dana.ipg.v1.models.query_payment_response_additional_info import QueryPaymentResponseAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPaymentResponseAdditionalInfo from a JSON string
query_payment_response_additional_info_instance = QueryPaymentResponseAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(QueryPaymentResponseAdditionalInfo.to_json())

# convert the object into a dict
query_payment_response_additional_info_dict = query_payment_response_additional_info_instance.to_dict()
# create an instance of QueryPaymentResponseAdditionalInfo from a dict
query_payment_response_additional_info_from_dict = QueryPaymentResponseAdditionalInfo.from_dict(query_payment_response_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


