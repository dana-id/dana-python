# DisbursementApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment and https://api.saas.dana.id for production environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_account_inquiry**](DisbursementApi.md#bank_account_inquiry) | **POST** /v1.0/emoney/bank-account-inquiry.htm | Transfer to Bank Account Inquiry
[**dana_account_inquiry**](DisbursementApi.md#dana_account_inquiry) | **POST** /v1.0/emoney/account-inquiry.htm | DANA Account Inquiry
[**transfer_to_bank**](DisbursementApi.md#transfer_to_bank) | **POST** /v1.0/emoney/transfer-bank.htm | Transfer to Bank
[**transfer_to_bank_inquiry_status**](DisbursementApi.md#transfer_to_bank_inquiry_status) | **POST** /v1.0/emoney/transfer-bank-status.htm | Transfer to Bank Inquiry Status
[**transfer_to_dana**](DisbursementApi.md#transfer_to_dana) | **POST** /v1.0/emoney/topup.htm | Transfer to DANA
[**transfer_to_dana_inquiry_status**](DisbursementApi.md#transfer_to_dana_inquiry_status) | **POST** /v1.0/emoney/topup-status.htm | Transfer to DANA Inquiry Status


# **bank_account_inquiry**
> bank_account_inquiry(bank_account_inquiry_request) -> BankAccountInquiryResponse 

Transfer to Bank Account Inquiry

This API is used for merchant to do inquiry Bank account info via DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.BankAccountInquiryRequest import BankAccountInquiryRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    bank_account_inquiry_request = BankAccountInquiryRequest()

    try:
        api_response = api_instance.bank_account_inquiry(bank_account_inquiry_request)
        print("The response of DisbursementApi->bank_account_inquiry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->bank_account_inquiry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_inquiry_request** | [**BankAccountInquiryRequest**](Disbursement/BankAccountInquiryRequest.md)|  | 

### Return type

[**BankAccountInquiryResponse**](Disbursement/BankAccountInquiryResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank account inquiry response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dana_account_inquiry**
> dana_account_inquiry(dana_account_inquiry_request) -> DanaAccountInquiryResponse 

DANA Account Inquiry

This API is used for merchant to do account inquiry to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.DanaAccountInquiryRequest import DanaAccountInquiryRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    dana_account_inquiry_request = DanaAccountInquiryRequest()

    try:
        api_response = api_instance.dana_account_inquiry(dana_account_inquiry_request)
        print("The response of DisbursementApi->dana_account_inquiry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->dana_account_inquiry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dana_account_inquiry_request** | [**DanaAccountInquiryRequest**](Disbursement/DanaAccountInquiryRequest.md)|  | 

### Return type

[**DanaAccountInquiryResponse**](Disbursement/DanaAccountInquiryResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DANA account inquiry response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_to_bank**
> transfer_to_bank(transfer_to_bank_request) -> TransferToBankResponse 

Transfer to Bank

This API is used for merchant to do transfer to Bank request via DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.TransferToBankRequest import TransferToBankRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    transfer_to_bank_request = TransferToBankRequest()

    try:
        api_response = api_instance.transfer_to_bank(transfer_to_bank_request)
        print("The response of DisbursementApi->transfer_to_bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->transfer_to_bank: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_to_bank_request** | [**TransferToBankRequest**](Disbursement/TransferToBankRequest.md)|  | 

### Return type

[**TransferToBankResponse**](Disbursement/TransferToBankResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer to bank response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |
**202** | Transfer to bank in progress |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_to_bank_inquiry_status**
> transfer_to_bank_inquiry_status(transfer_to_bank_inquiry_status_request) -> TransferToBankInquiryStatusResponse 

Transfer to Bank Inquiry Status

This API is used for merchant to do inquiry status transfer to Bank transaction to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.TransferToBankInquiryStatusRequest import TransferToBankInquiryStatusRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    transfer_to_bank_inquiry_status_request = TransferToBankInquiryStatusRequest()

    try:
        api_response = api_instance.transfer_to_bank_inquiry_status(transfer_to_bank_inquiry_status_request)
        print("The response of DisbursementApi->transfer_to_bank_inquiry_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->transfer_to_bank_inquiry_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_to_bank_inquiry_status_request** | [**TransferToBankInquiryStatusRequest**](Disbursement/TransferToBankInquiryStatusRequest.md)|  | 

### Return type

[**TransferToBankInquiryStatusResponse**](Disbursement/TransferToBankInquiryStatusResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer to bank inquiry status response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_to_dana**
> transfer_to_dana(transfer_to_dana_request) -> TransferToDanaResponse 

Transfer to DANA

This API is used for merchant to do top up request to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.TransferToDanaRequest import TransferToDanaRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    transfer_to_dana_request = TransferToDanaRequest()

    try:
        api_response = api_instance.transfer_to_dana(transfer_to_dana_request)
        print("The response of DisbursementApi->transfer_to_dana:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->transfer_to_dana: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_to_dana_request** | [**TransferToDanaRequest**](Disbursement/TransferToDanaRequest.md)|  | 

### Return type

[**TransferToDanaResponse**](Disbursement/TransferToDanaResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer to DANA response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_to_dana_inquiry_status**
> transfer_to_dana_inquiry_status(transfer_to_dana_inquiry_status_request) -> TransferToDanaInquiryStatusResponse 

Transfer to DANA Inquiry Status

This API is used for merchant to do inquiry status top up transaction to DANA

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)

* PRIVATE_KEY or PRIVATE_KEY_PATH
* ORIGIN
* X_PARTNER_ID
* ENV
```python
import os
from dana.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana.widget.v1 import DisbursementApi
from dana.widget.v1.models.TransferToDanaInquiryStatusRequest import TransferToDanaInquiryStatusRequest
from dana.api_client import ApiClient
from dana.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = DisbursementApi(api_client)
    transfer_to_dana_inquiry_status_request = TransferToDanaInquiryStatusRequest()

    try:
        api_response = api_instance.transfer_to_dana_inquiry_status(transfer_to_dana_inquiry_status_request)
        print("The response of DisbursementApi->transfer_to_dana_inquiry_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisbursementApi->transfer_to_dana_inquiry_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_to_dana_inquiry_status_request** | [**TransferToDanaInquiryStatusRequest**](Disbursement/TransferToDanaInquiryStatusRequest.md)|  | 

### Return type

[**TransferToDanaInquiryStatusResponse**](Disbursement/TransferToDanaInquiryStatusResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer to DANA inquiry status response |  * Content-Type - Content type, value always application/json <br>  * X-TIMESTAMP - Transaction date time, in format YYYY-MM-DDTHH:mm:ss+07:00. Time must be in GMT+7 (Jakarta time) <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

