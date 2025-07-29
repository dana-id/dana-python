# Copyright 2025 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum

class LatestTransactionStatus(str, Enum):
    00 = "00"
    01 = "01"
    02 = "02"
    03 = "03"
    04 = "04"
    05 = "05"
    06 = "06"
    07 = "07"

class LatestTransactionStatus(str, Enum):
    00 = "00"
    01 = "01"
    02 = "02"
    03 = "03"
    04 = "04"
    05 = "05"
    06 = "06"
    07 = "07"

class SourcePlatform(str, Enum):
    IPG = "IPG"

class TerminalType(str, Enum):
    APP = "APP"
    WEB = "WEB"
    WAP = "WAP"
    SYSTEM = "SYSTEM"

class OrderTerminalType(str, Enum):
    APP = "APP"
    WEB = "WEB"
    WAP = "WAP"
    SYSTEM = "SYSTEM"

class PayMethod(str, Enum):
    BALANCE = "BALANCE"
    COUPON = "COUPON"
    NET_BANKING = "NET_BANKING"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    VIRTUAL_ACCOUNT = "VIRTUAL_ACCOUNT"
    OTC = "OTC"
    DIRECT_DEBIT_CREDIT_CARD = "DIRECT_DEBIT_CREDIT_CARD"
    DIRECT_DEBIT_DEBIT_CARD = "DIRECT_DEBIT_DEBIT_CARD"
    ONLINE_CREDIT = "ONLINE_CREDIT"
    LOAN_CREDIT = "LOAN_CREDIT"
    NETWORK_PAY = "NETWORK_PAY"

class PayMethod(str, Enum):
    BALANCE = "BALANCE"
    COUPON = "COUPON"
    NET_BANKING = "NET_BANKING"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    VIRTUAL_ACCOUNT = "VIRTUAL_ACCOUNT"
    OTC = "OTC"
    DIRECT_DEBIT_CREDIT_CARD = "DIRECT_DEBIT_CREDIT_CARD"
    DIRECT_DEBIT_DEBIT_CARD = "DIRECT_DEBIT_DEBIT_CARD"
    ONLINE_CREDIT = "ONLINE_CREDIT"
    LOAN_CREDIT = "LOAN_CREDIT"

class PayOption(str, Enum):
    NETWORK_PAY_PG_SPAY = "NETWORK_PAY_PG_SPAY"
    NETWORK_PAY_PG_OVO = "NETWORK_PAY_PG_OVO"
    NETWORK_PAY_PG_GOPAY = "NETWORK_PAY_PG_GOPAY"
    NETWORK_PAY_PG_LINKAJA = "NETWORK_PAY_PG_LINKAJA"
    NETWORK_PAY_PG_CARD = "NETWORK_PAY_PG_CARD"
    VIRTUAL_ACCOUNT_BCA = "VIRTUAL_ACCOUNT_BCA"
    VIRTUAL_ACCOUNT_BNI = "VIRTUAL_ACCOUNT_BNI"
    VIRTUAL_ACCOUNT_MANDIRI = "VIRTUAL_ACCOUNT_MANDIRI"
    VIRTUAL_ACCOUNT_BRI = "VIRTUAL_ACCOUNT_BRI"
    VIRTUAL_ACCOUNT_BTPN = "VIRTUAL_ACCOUNT_BTPN"
    VIRTUAL_ACCOUNT_CIMB = "VIRTUAL_ACCOUNT_CIMB"
    VIRTUAL_ACCOUNT_PERMATA = "VIRTUAL_ACCOUNT_PERMATA"

class Type(str, Enum):
    PAY_RETURN = "PAY_RETURN"
    NOTIFICATION = "NOTIFICATION"

class ActorType(str, Enum):
    USER = "USER"
    MERCHANT = "MERCHANT"
    MERCHANT_OPERATOR = "MERCHANT_OPERATOR"
    BACK_OFFICE = "BACK_OFFICE"
    SYSTEM = "SYSTEM"
