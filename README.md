# dana-python
SDK for DANA API (https://dashboard.dana.id/api-docs) 

## Requirements.

Python 3.9.1+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install dana-python
```

(you may need to run `pip` with root permission: `sudo pip install dana-python`)

Then import the package, ex:
```python
import dana.payment_gateway.v1
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then go to documentation per API you wanna use:

## Documentation for API Endpoints

API | Description
------------- | -------------
[**PaymentGatewayApi**](docs/payment_gateway/v1/PaymentGatewayApi.md) | API for doing operations in DANA Payment Gateway (Gapura)
[**WidgetApi**](docs/widget/v1/WidgetApi.md) | API for enabling the user to make payment from merchant’s platform with redirecting to DANA’s platform
[**DisbursementApi**](docs/disbursement/v1/DisbursementApi.md) | API for doing operations in DANA Disbursement
[**MerchantManagementApi**](docs/merchant_management/v1/MerchantManagementApi.md) | API for doing operations in DANA Merchant Management
