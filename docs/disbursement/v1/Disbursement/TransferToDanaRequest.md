# TransferToDanaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_reference_no** | **str** | Unique transaction identifier on partner system which assigned to each transaction<br /> Notes:<br /> If the partner receives a timeout or an unexpected response from DANA and partner expects to perform retry request to DANA, please use the partnerReferenceNo that is the same as the one used in the transaction request process before  | 
**customer_number** | **str** | Customer account number, in format 628xxx | [optional] 
**amount** | [**Money**](Money.md) | Amount. Contains two sub-fields:<br /> 1. Value: Transaction amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**fee_amount** | [**Money**](Money.md) | Fee amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | 
**transaction_date** | **str** | Transaction date, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**session_id** | **str** | Session identifier | [optional] 
**category_id** | **float** | Category identifier | [optional] 
**notes** | **str** | Transaction notes | [optional] 
**additional_info** | [**TransferToDanaRequestAdditionalInfo**](TransferToDanaRequestAdditionalInfo.md) |  | 

## Example

```python
from dana.disbursement.v1.models.transfer_to_dana_request import TransferToDanaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToDanaRequest from a JSON string
transfer_to_dana_request_instance = TransferToDanaRequest.from_json(json)
# print the JSON string representation of the object
print(TransferToDanaRequest.to_json())

# convert the object into a dict
transfer_to_dana_request_dict = transfer_to_dana_request_instance.to_dict()
# create an instance of TransferToDanaRequest from a dict
transfer_to_dana_request_from_dict = TransferToDanaRequest.from_dict(transfer_to_dana_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


