# TransferToBankRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_type** | **str** | Additional information of withdraw fund type, i.e.<br /> MERCHANT_WITHDRAW_FOR_CORPORATE  | 
**external_division_id** | **str** | Additional information of external division identifier. (fundType: MERCHANT_WITHDRAW_FOR_CORPORATE)<br /> Notes: The required of this parameter is Optional, but if \&quot;additionalInfo.chargeTarget\&quot; has value DIVISION then the required of this parameter will be changed to Mandatory  | [optional] 
**charge_target** | **str** | Additional information of charge target. The values are:<br /> • null<br /> • DIVISION<br /> • MERCHANT<br /> Notes: If the value is DIVISION, externalDivisionId will be Mandatory  | [optional] 
**need_notify** | **bool** | Additional information of flag result notification on transaction completed (result sync/async) | [optional] 
**beneficiary_account_name** | **str** | Additional information of beneficiary account name for validation purpose | [optional] 
**access_token** | **str** | Contains customer token, which has been obtained from binding process, refer to Account Binding &amp; Unbinding documentation<br /> If request is coming from user interaction, this field is mandatory. If not, just filled customerNumber  | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_bank_request_additional_info import TransferToBankRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToBankRequestAdditionalInfo from a JSON string
transfer_to_bank_request_additional_info_instance = TransferToBankRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(TransferToBankRequestAdditionalInfo.to_json())

# convert the object into a dict
transfer_to_bank_request_additional_info_dict = transfer_to_bank_request_additional_info_instance.to_dict()
# create an instance of TransferToBankRequestAdditionalInfo from a dict
transfer_to_bank_request_additional_info_from_dict = TransferToBankRequestAdditionalInfo.from_dict(transfer_to_bank_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


