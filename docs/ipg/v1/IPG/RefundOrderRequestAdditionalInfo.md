# RefundOrderRequestAdditionalInfo

Additional information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_account_no** | **str** | Additional information of payout account number. This param need to be filled if want to refund to specific payout account not that specified by DANA | [optional] 
**refund_applied_time** | **str** | Additional information of refund applied time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) | [optional] 
**actor_type** | **str** | Additional information of actor type, refer to ActorTypeEnum | [optional] 
**return_charge_to_payer** | **str** | Additional information of return charge to payer | [optional] 
**destination** | **str** | Additional information of destination | [optional] 
**env_info** | **object** | Additional information of environment | 
**audit_info** | **object** | Additional information of audit | [optional] 
**actor_context** | **object** | Additional information of actor context | [optional] 
**refund_option_bill** | **List[object]** | Additional information of refund option bill | [optional] 
**extend_info** | **str** | Additional information of extend | [optional] 
**async_refund** | **str** | Additional information of async refund to determine the process of refund whether sync or async. The values is true/false | [optional] 

## Example

```python
from dana.ipg.v1.models.refund_order_request_additional_info import RefundOrderRequestAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RefundOrderRequestAdditionalInfo from a JSON string
refund_order_request_additional_info_instance = RefundOrderRequestAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(RefundOrderRequestAdditionalInfo.to_json())

# convert the object into a dict
refund_order_request_additional_info_dict = refund_order_request_additional_info_instance.to_dict()
# create an instance of RefundOrderRequestAdditionalInfo from a dict
refund_order_request_additional_info_from_dict = RefundOrderRequestAdditionalInfo.from_dict(refund_order_request_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


