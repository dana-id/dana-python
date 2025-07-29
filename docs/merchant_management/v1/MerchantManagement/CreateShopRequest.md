# CreateShopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | Merchant id | 
**parent_division_id** | **str** | Parent division ID. Required when shopParentType is DIVISION or EXTERNAL_DIVISION | [optional] 
**shop_parent_type** | **str** | Parent type for the shop | 
**main_name** | **str** | Shop name | 
**shop_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**shop_desc** | **str** | Shop description | [optional] 
**external_shop_id** | **str** | External shop identifier | 
**logo_url_map** | **Dict[str, str]** | Logo images encoded in base64. Keys can be LOGO, PC_LOGO, MOBILE_LOGO. Images must be PNG format. | [optional] 
**mcc_codes** | **List[str]** | MCC codes | [optional] 
**size_type** | **str** | Size type of the shop | 
**ln** | **str** | Longitude | [optional] 
**lat** | **str** | Latitude | [optional] 
**tax_no** | **str** | Tax number (NPWP). Must be 15 digits | [optional] 
**brand_name** | **str** | Legal name/tax name | [optional] 
**tax_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**loyalty** | **str** | Flag for loyalty category | [optional] 
**api_version** | **str** | API version flag. Use &gt; 2 for new attributes | [optional] 
**business_entity** | **str** | Business entity type. Required if apiVersion &gt; 2 | [optional] 
**business_docs** | [**List[BusinessDocs]**](BusinessDocs.md) | Business documents. Required if apiVersion &gt; 2 | [optional] 
**owner_name** | [**UserName**](UserName.md) |  | [optional] 
**owner_id_type** | **str** | Owner ID type. Required if apiVersion &gt; 2 | [optional] 
**owner_id_no** | **str** | Owner ID number. Required if apiVersion &gt; 2 | [optional] 
**owner_address** | [**AddressInfo**](AddressInfo.md) |  | [optional] 
**owner_phone_number** | [**MobileNoInfo**](MobileNoInfo.md) |  | [optional] 
**shop_owning** | **str** | Shop ownership type. Required if apiVersion &gt; 2 | [optional] 
**device_number** | **str** | Device number. Required if apiVersion &gt; 2 | [optional] 
**pos_number** | **str** | POS number. Required if apiVersion &gt; 2 | [optional] 
**director_pics** | [**List[PicInfo]**](PicInfo.md) | Director PICs. Required if apiVersion &gt; 2 | [optional] 
**non_director_pics** | [**List[PicInfo]**](PicInfo.md) | Non-director PICs. Required if apiVersion &gt; 2 | [optional] 
**shop_biz_type** | **str** | Shop business type | [optional] 
**ext_info** | **Dict[str, object]** | Extended information | [optional] 

## Example

```python
from dana.merchant_management.v1.models.create_shop_request import CreateShopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShopRequest from a JSON string
create_shop_request_instance = CreateShopRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShopRequest.to_json())

# convert the object into a dict
create_shop_request_dict = create_shop_request_instance.to_dict()
# create an instance of CreateShopRequest from a dict
create_shop_request_from_dict = CreateShopRequest.from_dict(create_shop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


