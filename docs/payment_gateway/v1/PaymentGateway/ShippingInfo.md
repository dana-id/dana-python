# ShippingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_amount** | [**Money**](Money.md) |  | [optional] 
**last_name** | **str** | Last name | 
**tracking_no** | **str** | Number of tracking | [optional] 
**country_name** | **str** | Name of country | 
**merchant_shipping_id** | **str** | Merchant shipping identifier | 
**city_name** | **str** | Name of city | 
**address1** | **str** | Information of address 1 | 
**address2** | **str** | Information of address 2 | [optional] 
**phone_no** | **str** | Phone number | [optional] 
**area_name** | **str** | Name of area | [optional] 
**email** | **str** | Email | [optional] 
**zip_code** | **str** | Zip code | 
**state_name** | **str** | Name of state | 
**fax_no** | **str** | Fax number | [optional] 
**carrier** | **str** | Information of carrier | [optional] 
**first_name** | **str** | First name | 
**mobile_no** | **str** | Mobile number | [optional] 

## Example

```python
from dana.payment_gateway.v1.models.shipping_info import ShippingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingInfo from a JSON string
shipping_info_instance = ShippingInfo.from_json(json)
# print the JSON string representation of the object
print(ShippingInfo.to_json())

# convert the object into a dict
shipping_info_dict = shipping_info_instance.to_dict()
# create an instance of ShippingInfo from a dict
shipping_info_from_dict = ShippingInfo.from_dict(shipping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


