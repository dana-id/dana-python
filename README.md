# dana_python
SDK for DANA API (https://dashboard.dana.id/api-docs) 

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import dana_python.payment_gateway.payment_gateway
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dana_python.payment_gateway.payment_gateway
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then go to documentation per API you wanna use:

## Documentation for API Endpoints

API | Description
------------- | -------------
[**PaymentGatewayApi**](docs/payment_gateway/PaymentGatewayApi.md) | API for doing operations in DANA Payment Gateway (Gapura)

