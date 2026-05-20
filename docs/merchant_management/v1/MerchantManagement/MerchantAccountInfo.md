# MerchantAccountInfo

One merchant account row (`accounts` in merchantInformation)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** | Merchant account number | [optional] 
**status** | **str** | Merchant account status | [optional] 
**debit_freeze_status** | **str** | Debit freeze status (merchant cannot accept money from DANA when frozen/closed) | [optional] 
**credit_freeze_status** | **str** | Credit freeze status (merchant cannot disburse when frozen/closed) | [optional] 
**total_amount** | **str** | Total amount as JSON string with &#x60;amount&#x60; and &#x60;currency&#x60; fields  | [optional] 
**available_amount** | **str** | Available amount as JSON string with &#x60;amount&#x60; and &#x60;currency&#x60; fields  | [optional] 
**currency** | **str** | Currency code (ISO) | [optional] 
**account_type** | **str** | Account type | [optional] 

## Example

```python
from dana.merchant_management.v1.models.merchant_account_info import MerchantAccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAccountInfo from a JSON string
merchant_account_info_instance = MerchantAccountInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAccountInfo.to_json())

# convert the object into a dict
merchant_account_info_dict = merchant_account_info_instance.to_dict()
# create an instance of MerchantAccountInfo from a dict
merchant_account_info_from_dict = MerchantAccountInfo.from_dict(merchant_account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


