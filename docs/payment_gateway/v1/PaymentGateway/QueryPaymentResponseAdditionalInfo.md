# QueryPaymentResponseAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer** | [**Buyer**](Buyer.md) | Additional information of buyer | [optional] 
**seller** | [**Seller**](Seller.md) | Additional information of seller | [optional] 
**amount_detail** | [**AmountDetail**](AmountDetail.md) | Additional information of amount detail. Present if transaction found | [optional] 
**time_detail** | [**TimeDetail**](TimeDetail.md) | Additional information of time detail. Present if transaction found | [optional] 
**goods** | [**List[Goods]**](Goods.md) | Additional information of goods | [optional] 
**shipping_info** | [**List[ShippingInfo]**](ShippingInfo.md) | Additional information of shipping | [optional] 
**order_memo** | **str** | Additional information of memo | [optional] 
**payment_views** | [**List[PaymentView]**](PaymentView.md) | Additional information of payment views. Present if transaction found | [optional] 
**extend_info** | **str** | Additional information of extend | [optional] 
**status_detail** | [**StatusDetail**](StatusDetail.md) | Additional information of status detail | [optional] 
**close_reason** | **str** | Additional information of close reason | [optional] 
**virtual_account_info** | [**VirtualAccountInfo**](VirtualAccountInfo.md) | Additional information of virtual account. Only use for Payment Gateway service | [optional] 
**merchant_id** | **str** | Merchant identifier | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.query_payment_response_additional_info import QueryPaymentResponseAdditionalInfo

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


