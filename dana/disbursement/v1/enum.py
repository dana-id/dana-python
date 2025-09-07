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
class ChargeTarget(str, Enum):
    DIVISION = "DIVISION"
    MERCHANT = "MERCHANT"

class LatestTransactionStatus(str, Enum):
    N00 = "00"
    N01 = "01"
    N02 = "02"
    N03 = "03"
    N04 = "04"
    N05 = "05"
    N06 = "06"
    N07 = "07"

