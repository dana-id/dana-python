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

