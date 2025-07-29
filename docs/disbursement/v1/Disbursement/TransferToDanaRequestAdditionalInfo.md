# TransferToDanaRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend_info** | **str** | Additional information of extend | [optional] 
**account_type** | **str** | Additional information of account type | [optional] 
**fund_type** | **str** | Additional information of transfer to DANA fund type, i.e.<br /> AGENT_TOPUP_FOR_USER_SETTLE  | 
**external_division_id** | **str** | Additional information of external division identifier. This parameter only used for Transfer to DANA subMerchant (fundType : AGENT_TOPUP_FOR_USER_SETTLE)<br /> Notes:<br /> The required of this parameter is Optional, but if \&quot;additionalInfo.chargeTarget\&quot; has value DIVISION then the required of this parameter will be changed to Mandatory  | [optional] 
**charge_target** | **str** | Additional information of charge target. This parameter only used for Transfer to DANA subMerchant. The value are:<br /> • null<br /> • DIVISION<br /> • MERCHANT<br /> if the value is DIVISION, externalDivisionId will be Mandatory  | [optional] 
**access_token** | **str** | Contains customer token, which has been obtained from binding process, refer to Account Binding &amp; Unbinding documentation<br /> If request is coming from user interaction, this field is mandatory. If not, just filled customerNumber  | [optional] 
**customer_id** | **str** | Public user identifier of DANA user.<br /> Notes: If used, requires customerNumber to be filled with default phone number literal \&quot;620000000000\&quot;  | [optional] 

## Example

```python
from dana.disbursement.v1.models.transfer_to_dana_request_additional_info import TransferToDanaRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransferToDanaRequestAdditionalInfo from a JSON string
transfer_to_dana_request_additional_info_instance = TransferToDanaRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(TransferToDanaRequestAdditionalInfo.to_json())

# convert the object into a dict
transfer_to_dana_request_additional_info_dict = transfer_to_dana_request_additional_info_instance.to_dict()
# create an instance of TransferToDanaRequestAdditionalInfo from a dict
transfer_to_dana_request_additional_info_from_dict = TransferToDanaRequestAdditionalInfo.from_dict(transfer_to_dana_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


