# Copyright 2026 PT Espay Debit Indonesia Koe
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

import json

import pytest
from types import SimpleNamespace

from dana.disbursement.v1.custom_validation import enrich_disbursement_error
from dana.disbursement.v1.models import (
    Money,
    TransferToDanaRequest,
    TransferToDanaRequestAdditionalInfo,
)
from dana.exceptions import ForbiddenException, ServiceException


@pytest.fixture(autouse=True)
def sandbox_env(monkeypatch):
    monkeypatch.setenv('DANA_ENV', 'sandbox')


def _transfer_to_dana_request() -> TransferToDanaRequest:
    return TransferToDanaRequest(
        partner_reference_no='ref-1',
        amount=Money(value='21000000.00', currency='IDR'),
        fee_amount=Money(value='1.00', currency='IDR'),
        additional_info=TransferToDanaRequestAdditionalInfo(
            fund_type='AGENT_TOPUP_FOR_USER_SETTLE',
        ),
    )


def test_enrich_disbursement_error_appends_hint_on_reason_and_data():
    request = _transfer_to_dana_request()
    body = json.dumps({
        'responseCode': '4033802',
        'responseMessage': 'Exceed maximum limit amount',
        'partnerReferenceNo': 'ref-1',
    })
    exc = ForbiddenException(status=403, reason='Forbidden', body=body, data=json.loads(body))

    enriched = enrich_disbursement_error(request, exc)

    assert enriched.reason.startswith('403:')
    assert '21000000 after topup' in enriched.reason
    assert enriched.data['responseMessage'] != 'Exceed maximum limit amount'
    assert '21000000 after topup' in enriched.data['responseMessage']


def test_enrich_disbursement_error_leaves_reason_when_no_hint():
    request = _transfer_to_dana_request()
    body = json.dumps({
        'responseCode': '4033814',
        'responseMessage': 'Insufficient Fund',
        'partnerReferenceNo': 'ref-2',
    })
    exc = ForbiddenException(status=403, reason='Forbidden', body=body, data=json.loads(body))

    enriched = enrich_disbursement_error(request, exc)

    assert enriched.reason == 'Forbidden'
    assert enriched.data['responseMessage'] == 'Insufficient Fund'


def test_enrich_disbursement_error_bank_transfer_general_error():
    class BankAccountInquiryRequest:
        pass

    request = BankAccountInquiryRequest()
    body = json.dumps({
        'responseCode': '5004201',
        'responseMessage': 'General Error',
        'partnerReferenceNo': 'ref-bank',
    })
    exc = ServiceException(status=500, reason='Internal Server Error', body=body, data=json.loads(body))

    enriched = enrich_disbursement_error(request, exc)

    assert enriched.reason.startswith('500:')
    assert '2460888509' in enriched.data['responseMessage']
    assert '014' in enriched.data['responseMessage']


def test_enrich_disbursement_error_transfer_to_bank_exceed_amount():
    class TransferToBankRequest:
        pass

    request = TransferToBankRequest()
    body = json.dumps({
        'responseCode': '4034302',
        'responseMessage': 'Exceed limit per transaction',
        'partnerReferenceNo': 'ref-tb',
    })
    exc = ForbiddenException(status=403, reason='Forbidden', body=body, data=json.loads(body))

    enriched = enrich_disbursement_error(request, exc)

    assert '20000000' in enriched.data['responseMessage']


def test_enrich_disbursement_error_skips_outside_sandbox(monkeypatch):
    monkeypatch.setenv('DANA_ENV', 'production')
    request = _transfer_to_dana_request()
    body = json.dumps({
        'responseCode': '4033802',
        'responseMessage': 'Exceed maximum limit amount',
        'partnerReferenceNo': 'ref-1',
    })
    exc = ForbiddenException(status=403, reason='Forbidden', body=body, data=json.loads(body))

    enriched = enrich_disbursement_error(request, exc)

    assert enriched is exc
    assert enriched.reason == 'Forbidden'
