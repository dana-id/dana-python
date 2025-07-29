# UpdateShopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **str** | Shop identifier. Length depends on shopIdType - INNER_ID (21 max), EXTERNAL_ID (64 max) | 
**merchant_id** | **str** | Merchant identifier | 
**shop_id_type** | **str** | Shop identifier type | 
**main_name** | **str** | Shop name | [optional] 
**shop_address** | [**AddressInfo**](AddressInfo.md) |  | 
**shop_desc** | **str** | Shop description | [optional] 
**new_external_shop_id** | **str** | New external shop identifier | [optional] 
**mcc_codes** | **List[str]** | Merchant category code | [optional] 
**logo_url_map** | **Dict[str, str]** | Logo URL map with base64 encoded images. Keys can be LOGO, PC_LOGO, MOBILE_LOGO | [optional] 
**ext_info** | **Dict[str, object]** | Extend information | [optional] 
**size_type** | **str** | Size type | [optional] 
**ln** | **str** | Longitude of shop&#39;s location | [optional] 
**lat** | **str** | Latitude of shop&#39;s location | [optional] 
**loyalty** | **str** | Flag for loyalty category | [optional] 
**owner_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**owner_name** | [**UserName**](UserName.md) |  | [optional] 
**owner_phone_number** | [**MobileNoInfo**](MobileNoInfo.md) |  | [optional] 
**owner_id_type** | **str** | Owner identifier type | [optional] 
**owner_id_no** | **str** | Owner identifier number. Length depends on ownerIdType - KTP (16), SIM (12-14), Passport (8), NIB (&gt;&#x3D;13), SIUP (free text) | [optional] 
**device_number** | **str** | Device number | [optional] 
**pos_number** | **str** | POS number | [optional] 
**api_version** | **str** | API version flag. Use &gt; 2 for new attributes | [optional] 
**business_entity** | **str** | Business entity type | [optional] 
**shop_owning** | **str** | Shop owning information | [optional] 
**shop_biz_type** | **str** | Shop business type | [optional] 
**business_docs** | [**List[BusinessDocs]**](BusinessDocs.md) | Business documents. \&quot;individu\&quot; entity can only use KTP and SIM. Other entities can use SIUP and NIB | [optional] 
**business_end_date** | **str** | Business end date, in format YYYY-MM-dd | [optional] 
**tax_no** | **str** | Tax number (NPWP). Must be 15 digits | [optional] 
**tax_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**brand_name** | **str** | Brand name on legal name or tax name | [optional] 
**director_pics** | [**List[PicInfo]**](PicInfo.md) | Director as a PIC of shop | [optional] 
**non_director_pics** | [**List[PicInfo]**](PicInfo.md) | Non director which become an PIC of shop | [optional] 

## Example

```python
from dana.merchant_management.v1.models.update_shop_request import UpdateShopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShopRequest from a JSON string
update_shop_request_instance = UpdateShopRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShopRequest.to_json())

# convert the object into a dict
update_shop_request_dict = update_shop_request_instance.to_dict()
# create an instance of UpdateShopRequest from a dict
update_shop_request_from_dict = UpdateShopRequest.from_dict(update_shop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


