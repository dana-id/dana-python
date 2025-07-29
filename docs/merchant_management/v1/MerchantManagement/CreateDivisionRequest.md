# CreateDivisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API Version. As per the respective API reference. Must be &gt; 2 | 
**merchant_id** | **str** | Merchant identifier | 
**parent_division_id** | **str** | Parent division identifier. Required when parentRoleType is DIVISION or EXTERNAL_DIVISION. Length depends on parentRoleType - DIVISION (21 max), EXTERNAL_DIVISION (64 max) | [optional] 
**parent_role_type** | **str** | Type of parent role | 
**division_name** | **str** | Division name | 
**division_address** | [**AddressInfo**](AddressInfo.md) |  | 
**division_description** | **str** | Division description | [optional] 
**division_type** | **str** | Division type | 
**external_division_id** | **str** | External division identifier | 
**logo_url_map** | **Dict[str, str]** | Logo URL map with base64 encoded images. Keys can be LOGO, PC_LOGO, MOBILE_LOGO | [optional] 
**ext_info** | [**CreateDivisionRequestExtInfo**](CreateDivisionRequestExtInfo.md) |  | 
**mcc_codes** | **List[str]** | Merchant category codes | 
**business_docs** | [**List[BusinessDocs]**](BusinessDocs.md) | Business documents. \&quot;individu\&quot; entity can only use KTP and SIM. Other entities can use SIUP and NIB | 
**business_entity** | **str** | Business entity type | 
**owner_name** | [**UserName**](UserName.md) |  | 
**owner_phone_number** | [**MobileNoInfo**](MobileNoInfo.md) |  | 
**owner_id_type** | **str** | Owner identifier type | 
**owner_id_no** | **str** | Owner identifier number. Length depends on ownerIdType - KTP (16), SIM (12-14), Passport (8), NIB (&gt;&#x3D;13), SIUP (free text) | 
**owner_address** | [**AddressInfo**](AddressInfo.md) |  | 
**director_pics** | [**List[PicInfo]**](PicInfo.md) | Director as a PIC of sub merchant | 
**non_director_pics** | [**List[PicInfo]**](PicInfo.md) | Non director which become a PIC of sub merchant | 
**size_type** | **str** | Size type | 
**pg_division_flag** | **str** | Flag if division is type PG | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_division_request import CreateDivisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDivisionRequest from a JSON string
create_division_request_instance = CreateDivisionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDivisionRequest.to_json())

# convert the object into a dict
create_division_request_dict = create_division_request_instance.to_dict()
# create an instance of CreateDivisionRequest from a dict
create_division_request_from_dict = CreateDivisionRequest.from_dict(create_division_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


