# AccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_type** | **str** | Account information of balance type to specify which balance type expected to be returned. Will return all available balance type if this parameter empty | [optional] 
**amount** | [**Money**](Money.md) | Account information of amount which include the net active amount. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**float_amount** | [**Money**](Money.md) | Account information of float amount which include the inactive amount due to cut off period. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**hold_amount** | [**Money**](Money.md) | Account information of hold amount which include the unusable amount due to certain type of transaction. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**available_balance** | [**Money**](Money.md) | Account information of available balance which include the active amount that can be used for transaction. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**ledger_balance** | [**Money**](Money.md) | Account information of ledger balance which include the starting balance for this day. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**current_multilateral_limit** | [**Money**](Money.md) | Account information of current multilateral limit. Contains two sub-fields:<br /> 1. Value: Amount, including the cents<br /> 2. Currency: Currency code based on ISO  | [optional] 
**registration_status_code** | **str** | Account information of customer registration status | [optional] 
**status** | **str** | Account information of status. The values include:<br /> 1 &#x3D; Active Account<br /> 2 &#x3D; Closed Account<br /> 4 &#x3D; New Account<br /> 6 &#x3D; Restricted Account<br /> 7 &#x3D; Frozen Account  | [optional] 

## Example

```python
from dana.widget.v1.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print(AccountInfo.to_json())

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_from_dict = AccountInfo.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


