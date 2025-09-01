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

import os
import datetime

from dana.disbursement.v1.models.dana_account_inquiry_request import DanaAccountInquiryRequest
from dana.disbursement.v1.models.dana_account_inquiry_request_additional_info import DanaAccountInquiryRequestAdditionalInfo
from dana.disbursement.v1.models.transfer_to_dana_request import TransferToDanaRequest
from dana.disbursement.v1.models.transfer_to_dana_request_additional_info import TransferToDanaRequestAdditionalInfo
from dana.disbursement.v1.models.transfer_to_dana_inquiry_status_request import TransferToDanaInquiryStatusRequest
from dana.disbursement.v1.models.bank_account_inquiry_request import BankAccountInquiryRequest
from dana.disbursement.v1.models.bank_account_inquiry_request_additional_info import BankAccountInquiryRequestAdditionalInfo
from dana.disbursement.v1.models.transfer_to_bank_request import TransferToBankRequest
from dana.disbursement.v1.models.transfer_to_bank_request_additional_info import TransferToBankRequestAdditionalInfo
from dana.disbursement.v1.models.transfer_to_bank_inquiry_status_request import TransferToBankInquiryStatusRequest
from dana.disbursement.v1.models.money import Money

def get_dynamic_dana_account_inquiry_request():
    """Get a dynamic DANA account inquiry request with unique reference number."""
    
    additional_info = DanaAccountInquiryRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE"
    )
    
    request = DanaAccountInquiryRequest(
        partner_reference_no=f"ACCINQ-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        additional_info=additional_info
    )
    
    return request


def get_dana_account_inquiry_request_with_access_token():
    """Get a DANA account inquiry request with access token."""
    
    additional_info = DanaAccountInquiryRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE",
        access_token="test_access_token_123456"
    )
    
    request = DanaAccountInquiryRequest(
        partner_reference_no=f"ACCINQ-TOKEN-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        additional_info=additional_info
    )
    
    return request


def get_dana_account_inquiry_request_with_customer_id():
    """Get a DANA account inquiry request with customer ID."""
    
    additional_info = DanaAccountInquiryRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE",
        customer_id="test_customer_123"
    )
    
    request = DanaAccountInquiryRequest(
        partner_reference_no=f"ACCINQ-CUSTID-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="620000000000",  # Default phone number format when using customer_id
        amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        additional_info=additional_info
    )
    
    return request


def get_bank_account_inquiry_request():
    """Get a bank account inquiry request."""
    
    additional_info = BankAccountInquiryRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE",
        beneficiary_bank_code="014"
    )
    
    request = BankAccountInquiryRequest(
        partner_reference_no=f"BANKINQ-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        beneficiary_account_number="2460888509",
        amount=Money(value="50000.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request


def get_bank_account_inquiry_request_with_account_name():
    """Get a bank account inquiry request with beneficiary account name."""
    
    additional_info = BankAccountInquiryRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE",
        beneficiary_bank_code="014",
        beneficiary_account_name="Test Account Holder"
    )
    
    request = BankAccountInquiryRequest(
        partner_reference_no=f"BANKINQ-NAME-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        beneficiary_account_number="2460888509",
        amount=Money(value="1.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request


def get_transfer_to_bank_request():
    """Get a transfer to bank request."""
    
    additional_info = TransferToBankRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE"
    )
    
    request = TransferToBankRequest(
        partner_reference_no=f"TRANSFER-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        beneficiary_account_number="2460888509",
        beneficiary_bank_code="014",
        amount=Money(value="50000.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request


def get_transfer_to_bank_request_with_notification():
    """Get a transfer to bank request with notification enabled."""
    
    additional_info = TransferToBankRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE",
        need_notify=True,
        beneficiary_account_name="Test Account Holder"
    )
    
    request = TransferToBankRequest(
        partner_reference_no=f"TRANSFER-NOTIFY-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        beneficiary_account_number="2460888509",
        beneficiary_bank_code="014",
        amount=Money(value="1.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request


def get_transfer_to_bank_inquiry_status_request(original_reference_no=None):
    """Get a transfer to bank inquiry status request with reference to original transaction."""
    
    request = TransferToBankInquiryStatusRequest(
        partner_reference_no=f"BANKST-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        original_partner_reference_no=original_reference_no or "BANKTRX-20230101000001",
        service_code="00"
    )
    
    return request


def get_transfer_to_bank_inquiry_status_request_with_references(original_reference_no=None):
    """Get a transfer to bank inquiry status request with all reference numbers."""
    
    request = TransferToBankInquiryStatusRequest(
        partner_reference_no=f"BANKST-REF-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        original_partner_reference_no=original_reference_no or "BANKTRX-20230101000001",
        original_reference_no="DANA123456789",
        original_external_id="EXT123456789",
        service_code="52"
    )
    
    return request


def get_customer_top_up_request():
    """Get a transfer to DANA request."""
    
    additional_info = TransferToDanaRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE",
    )
    
    request = TransferToDanaRequest(
        partner_reference_no=f"TOPUP-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        amount=Money(value="1.00", currency="IDR"),
        fee_amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        additional_info=additional_info
    )
    
    return request


def get_customer_top_up_request_with_division():
    """Get a transfer to DANA request with division charge target."""
    
    additional_info = TransferToDanaRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE",
        external_division_id="DIV123456",
        charge_target="DIVISION",
        account_type="DANA_WALLET"
    )
    
    request = TransferToDanaRequest(
        partner_reference_no=f"TOPUP-DIV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        amount=Money(value="1.00", currency="IDR"),
        fee_amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        notes="Test transfer to DANA with division",
        additional_info=additional_info
    )
    
    return request


def get_transfer_to_dana_inquiry_status_request(original_reference_no=None):
    """Get a transfer to DANA inquiry status request with reference to original transaction."""
    
    request = TransferToDanaInquiryStatusRequest(
        partner_reference_no=f"TOPUPST-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        original_partner_reference_no=original_reference_no or "TOPUP-20230101000001",
        service_code="38"
    )
    
    return request


# Keeping this function for backward compatibility
def get_customer_top_up_inquiry_status_request(original_reference_no=None):
    """Get a transfer to DANA inquiry status request (alias for get_transfer_to_dana_inquiry_status_request)."""
    return get_transfer_to_dana_inquiry_status_request(original_reference_no)


def get_customer_top_up_inquiry_status_request_with_reference(original_reference_no=None):
    """Get a transfer to DANA inquiry status request with DANA reference."""
    
    request = TransferToDanaInquiryStatusRequest(
        partner_reference_no=f"TOPUPST-REF-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        original_partner_reference_no=original_reference_no or "TOPUP-20230101000001",
        original_reference_no="DANA123456789",
        service_code="53"
    )
    
    return request


def get_dynamic_transfer_to_bank_request():
    """Get a dynamic transfer to bank request with unique reference number."""
    
    additional_info = TransferToBankRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE"
    )
    
    request = TransferToBankRequest(
        partner_reference_no=f"TRANSFER-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="6287875849373",
        beneficiary_account_number="2460888509",
        beneficiary_bank_code="014",
        amount=Money(value="50000.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request
    

def get_dynamic_transfer_to_dana_request():
    """Get a dynamic transfer to DANA request with unique reference number."""
    
    additional_info = TransferToDanaRequestAdditionalInfo(
        fund_type="AGENT_TOPUP_FOR_USER_SETTLE",
    )
    
    request = TransferToDanaRequest(
        partner_reference_no=f"TOPUP-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        amount=Money(value="1.00", currency="IDR"),
        fee_amount=Money(value="1.00", currency="IDR"),
        transaction_date=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00'),
        additional_info=additional_info
    )
    
    return request


# Keeping this function for backward compatibility
def get_dynamic_customer_top_up_request():
    """Get a dynamic transfer to DANA request with unique reference number (alias for get_dynamic_transfer_to_dana_request)."""
    return get_dynamic_transfer_to_dana_request()


def get_dynamic_bank_account_inquiry_request():
    """Get a dynamic bank account inquiry request with unique reference number."""
    
    additional_info = BankAccountInquiryRequestAdditionalInfo(
        fund_type="MERCHANT_WITHDRAW_FOR_CORPORATE",
        beneficiary_bank_code="014"
    )
    
    request = BankAccountInquiryRequest(
        partner_reference_no=f"BANKINQ-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        customer_number="62811742234",
        beneficiary_account_number="2460888509",
        amount=Money(value="50000.00", currency="IDR"),
        additional_info=additional_info
    )
    
    return request