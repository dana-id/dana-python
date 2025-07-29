# UpdateDivisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant identifier | 
**division_id** | **str** | Division identifier. Required when divisionIdType is INNER_ID | [optional] 
**division_name** | **str** | Division name | 
**division_address** | [**AddressInfo**](AddressInfo.md) |  | 
**division_description** | **str** | Division description | [optional] 
**division_type** | **str** | Division type | 
**division_id_type** | **str** | Division identifier type | 
**external_division_id** | **str** | External division identifier. Required when divisionIdType is EXTERNAL_ID | [optional] 
**new_external_division_id** | **str** | New external division identifier | 
**logo_url_map** | **Dict[str, str]** | Logo URL map with base64 encoded images. Keys can be LOGO, PC_LOGO, MOBILE_LOGO | [optional] 
**mcc_codes** | **List[str]** | Merchant category codes | 
**ext_info** | **Dict[str, object]** | Extended information | 
**api_version** | **str** | API version flag. Use &gt; 2 for new attributes | [optional] 
**business_docs** | [**List[BusinessDocs]**](BusinessDocs.md) | Business documents. Required when apiVersion &gt; 2. \&quot;individu\&quot; entity can only use KTP and SIM. Other entities can use SIUP and NIB | [optional] 
**business_entity** | **str** | Business entity type. Required when apiVersion &gt; 2 | [optional] 
**business_end_date** | **str** | Business end date, in format YYYY-MM-DD. Required when apiVersion &gt; 2 | [optional] 
**owner_name** | [**UserName**](UserName.md) |  | [optional] 
**owner_phone_number** | [**MobileNoInfo**](MobileNoInfo.md) |  | [optional] 
**owner_id_type** | **str** | Owner identifier type. Required when apiVersion &gt; 2 | [optional] 
**owner_id_no** | **str** | Owner identifier number. Required when apiVersion &gt; 2. Length depends on ownerIdType - KTP (16), SIM (12-14), Passport (8), NIB (&gt;&#x3D;13), SIUP (free text) | [optional] 
**owner_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**director_pics** | [**List[PicInfo]**](PicInfo.md) | Director as a PIC of sub merchant. Required when apiVersion &gt; 2 | [optional] 
**non_director_pics** | [**List[PicInfo]**](PicInfo.md) | Non director which become a PIC of sub merchant. Required when apiVersion &gt; 2 | [optional] 
**size_type** | **str** | Size type. Required when apiVersion &gt; 2 | [optional] 
**pg_division_flag** | **str** | Flag if division is type PG | [optional] 

## Example

```python
from dana.merchant_management.v1.models.update_division_request import UpdateDivisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDivisionRequest from a JSON string
update_division_request_instance = UpdateDivisionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDivisionRequest.to_json())

# convert the object into a dict
update_division_request_dict = update_division_request_instance.to_dict()
# create an instance of UpdateDivisionRequest from a dict
update_division_request_from_dict = UpdateDivisionRequest.from_dict(update_division_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


