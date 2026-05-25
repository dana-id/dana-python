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
class ShopParentType(str, Enum):
    MERCHANT = "MERCHANT"
    DIVISION = "DIVISION"
    EXTERNAL_DIVISION = "EXTERNAL_DIVISION"

class SizeType(str, Enum):
    UMI = "UMI"
    UKE = "UKE"
    UME = "UME"
    UBE = "UBE"
    URE = "URE"

class Loyalty(str, Enum):
    TRUE = "true"
    FALSE = "false"

class BusinessEntity(str, Enum):
    PT = "pt"
    CV = "cv"
    INDIVIDU = "individu"
    USAHA_DAGANG = "usaha_dagang"
    YAYASAN = "yayasan"
    KOPERASI = "koperasi"

class OwnerIdType(str, Enum):
    KTP = "KTP"
    SIM = "SIM"
    PASSPORT = "PASSPORT"
    SIUP = "SIUP"
    NIB = "NIB"

class ShopOwning(str, Enum):
    DIRECT_OWNED = "DIRECT_OWNED"
    FRANCHISED = "FRANCHISED"

class ShopIdType(str, Enum):
    INNER_ID = "INNER_ID"
    EXTERNAL_ID = "EXTERNAL_ID"

class ParentRoleType(str, Enum):
    MERCHANT = "MERCHANT"
    DIVISION = "DIVISION"
    EXTERNAL_DIVISION = "EXTERNAL_DIVISION"

class DivisionType(str, Enum):
    REGION = "REGION"
    AREA = "AREA"
    BRANCH = "BRANCH"
    OUTLET = "OUTLET"
    STORE = "STORE"
    KIOSK = "KIOSK"
    STALL = "STALL"
    COUNTER = "COUNTER"
    BOOTH = "BOOTH"
    POINT_OF_SALE = "POINT_OF_SALE"
    VENDING_MACHINE = "VENDING_MACHINE"

class GOODSSOLDTYPE(str, Enum):
    DIGITAL = "DIGITAL"
    PHYSICAL = "PHYSICAL"

class USERPROFILING(str, Enum):
    B2B = "B2B"
    B2C = "B2C"

class PgDivisionFlag(str, Enum):
    TRUE = "true"
    FALSE = "false"

class DivisionIdType(str, Enum):
    INNER_ID = "INNER_ID"
    EXTERNAL_ID = "EXTERNAL_ID"

class ResourceType(str, Enum):
    MERCHANT_DEPOSIT_BALANCE = "MERCHANT_DEPOSIT_BALANCE"
    MERCHANT_AVAILABLE_BALANCE = "MERCHANT_AVAILABLE_BALANCE"
    MERCHANT_TOTAL_BALANCE = "MERCHANT_TOTAL_BALANCE"

class Verified(str, Enum):
    TRUE = "true"
    FALSE = "false"

class DocType(str, Enum):
    KTP = "KTP"
    SIM = "SIM"
    SIUP = "SIUP"
    NIB = "NIB"

class ResultStatus(str, Enum):
    S = "S"
    F = "F"
    U = "U"

class ShopBizType(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

class ContactBizType(str, Enum):
    TRANSFER_HIS = "TRANSFER_HIS"
    DIRECT_TRANSFER = "DIRECT_TRANSFER"
    GENERAL_CARD = "GENERAL_CARD"
    DIRECTPAY_CARD = "DIRECTPAY_CARD"
    PAYMENT_CARD = "PAYMENT_CARD"
    CASHOUT_CARD = "CASHOUT_CARD"
    IMPS_ACCOUNT = "IMPS_ACCOUNT"
    INVESTMENT_ACCOUNT = "INVESTMENT_ACCOUNT"

class AssetType(str, Enum):
    CHECKING_ACCOUNT = "CHECKING_ACCOUNT"
    SAVINGS_ACCOUNT = "SAVINGS_ACCOUNT"
    LOAN_ACCOUNT = "LOAN_ACCOUNT"
    IMPS_ACCOUNT = "IMPS_ACCOUNT"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"
    SECURED_CREDIT_CARD = "SECURED_CREDIT_CARD"
    VA_ACCOUNT = "VA_ACCOUNT"
    OTC_ACCOUNT = "OTC_ACCOUNT"
    REFUND_ACCOUNT = "REFUND_ACCOUNT"
    CREDIT_ACCOUNT = "CREDIT_ACCOUNT"
    LOAN = "LOAN"
    MUTUAL_FUNDS_ACCOUNT = "MUTUAL_FUNDS_ACCOUNT"
    INVESTMENT = "INVESTMENT"

class DefaultAsset(str, Enum):
    TRUE = "true"
    FALSE = "false"

class EnableStatus(str, Enum):
    TRUE = "true"
    FALSE = "false"

class DirectDebit(str, Enum):
    TRUE = "true"
    FALSE = "false"

class EnableOnly(str, Enum):
    TRUE = "true"
    FALSE = "false"

class LoginType(str, Enum):
    ROLE = "ROLE"
    MOBILE_NO = "MOBILE_NO"

class ContactAddressType(str, Enum):
    OFFICE_ADD = "OFFICE_ADD"
    REG_ADD = "REG_ADD"
    HOME_ADD = "HOME_ADD"

class Status(str, Enum):
    ENABLE = "ENABLE"
    FROZEN = "FROZEN"
    CLOSE = "CLOSE"

class DebitFreezeStatus(str, Enum):
    ENABLE = "ENABLE"
    FROZEN = "FROZEN"
    CLOSE = "CLOSE"

class CreditFreezeStatus(str, Enum):
    ENABLE = "ENABLE"
    FROZEN = "FROZEN"
    CLOSE = "CLOSE"

class AccountType(str, Enum):
    MERCHANT_SETTLEMENT_ACCOUNT = "MERCHANT_SETTLEMENT_ACCOUNT"
    MERCHANT_PAYABLE_ACCOUNT = "MERCHANT_PAYABLE_ACCOUNT"
    MERCHANT_DEPOSIT_ACCOUNT = "MERCHANT_DEPOSIT_ACCOUNT"

class MerchantType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    CORPORATION = "CORPORATION"
    FINANCIAL_INST = "FINANCIAL_INST"

class MerchantSubType(str, Enum):
    COMPANY_TYPE_22 = "COMPANY_TYPE_22"
    COMPANY_TYPE_31 = "COMPANY_TYPE_31"
    COMPANY_TYPE_41 = "COMPANY_TYPE_41"

class MerchantStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"

