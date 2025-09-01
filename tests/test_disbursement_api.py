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

import time
from dana.disbursement.v1.api import DisbursementApi
from dana.disbursement.v1.models import (
    DanaAccountInquiryRequest,
    DanaAccountInquiryResponse,
    TransferToDanaRequest,
    TransferToDanaResponse,
    TransferToDanaInquiryStatusRequest,
    TransferToDanaInquiryStatusResponse,
    BankAccountInquiryRequest,
    BankAccountInquiryResponse,
    TransferToBankRequest,
    TransferToBankResponse,
    TransferToBankInquiryStatusRequest,
    TransferToBankInquiryStatusResponse
)
from dana.rest import ApiException

from tests.fixtures.api_client import api_instance_disbursement
from tests.fixtures.disbursement import (
    get_dynamic_dana_account_inquiry_request,
    get_dynamic_bank_account_inquiry_request,
    get_dynamic_transfer_to_bank_request,
    get_dynamic_transfer_to_dana_request,
    get_transfer_to_bank_inquiry_status_request,
    get_transfer_to_dana_inquiry_status_request
)


class TestDisbursementApi:
    """Test class for Disbursement API endpoints"""
    
    def test_dana_account_inquiry_success(self, api_instance_disbursement: DisbursementApi):
        """Should give success response and validate DANA account inquiry functionality"""
        
        # Arrange
        request = get_dynamic_dana_account_inquiry_request()
        
        # Act
        api_response = api_instance_disbursement.dana_account_inquiry(request)
        
        # Assert - Check response structure and required fields
        assert isinstance(api_response, DanaAccountInquiryResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        assert api_response.customer_name is not None, 'Customer name should not be empty'
        
        # Assert - Check Money objects are properly structured
        assert api_response.min_amount is not None, 'Min amount should not be null'
        assert api_response.max_amount is not None, 'Max amount should not be null'
        assert api_response.amount is not None, 'Amount should not be null'
        assert api_response.fee_amount is not None, 'Fee amount should not be null'
        
        assert api_response.min_amount.value is not None, 'Min amount value should not be null'
        assert api_response.min_amount.currency is not None, 'Min amount currency should not be null'
        assert api_response.max_amount.value is not None, 'Max amount value should not be null'
        assert api_response.max_amount.currency is not None, 'Max amount currency should not be null'
        assert api_response.amount.value is not None, 'Amount value should not be null'
        assert api_response.amount.currency is not None, 'Amount currency should not be null'
        assert api_response.fee_amount.value is not None, 'Fee amount value should not be null'
        assert api_response.fee_amount.currency is not None, 'Fee amount currency should not be null'
        
        # Assert - Check currency consistency
        assert api_response.amount.currency == api_response.fee_amount.currency, 'Amount and fee currency should match'

    def test_bank_account_inquiry_success(self, api_instance_disbursement: DisbursementApi):
        """Should give success response and validate bank account inquiry functionality"""
        
        # Arrange
        request = get_dynamic_bank_account_inquiry_request()
        
        # Act
        api_response = api_instance_disbursement.bank_account_inquiry(request)
        
        # Assert - Check response structure and required fields
        assert isinstance(api_response, BankAccountInquiryResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        assert api_response.beneficiary_account_number is not None, 'Beneficiary account number should not be empty'
        assert api_response.beneficiary_account_name is not None, 'Beneficiary account name should not be empty'
        assert api_response.amount is not None, 'Amount should not be null'
        
        # Assert - Check account details match request
        assert api_response.beneficiary_account_number == request.beneficiary_account_number, 'Account number should match request'
        
        # Assert - Check Money object structure
        assert api_response.amount.value is not None, 'Amount value should not be null'
        assert api_response.amount.currency is not None, 'Amount currency should not be null'
        assert api_response.amount.value == request.amount.value, 'Amount should match request'
        assert api_response.amount.currency == request.amount.currency, 'Currency should match request'
        
        # Assert - Check additional info if present
        if hasattr(api_response, 'additional_info') and api_response.additional_info is not None:
            assert api_response.additional_info is not None, 'Additional info should be present'

    def test_transfer_to_bank_success(self, api_instance_disbursement: DisbursementApi):
        """Should give success response and validate transfer to bank functionality"""
        
        # Arrange
        request = get_dynamic_transfer_to_bank_request()
        
        # Act
        api_response = api_instance_disbursement.transfer_to_bank(request)
        
        # Assert - Check response structure and required fields
        assert isinstance(api_response, TransferToBankResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        
        # Assert - Check partner reference number matches if present
        if hasattr(api_response, 'partner_reference_no') and api_response.partner_reference_no is not None:
            assert api_response.partner_reference_no == request.partner_reference_no, 'Partner reference number should match request'

    def test_transfer_to_bank_inquiry_status_success(self, api_instance_disbursement: DisbursementApi):
        """Should give success response and validate transfer to bank inquiry status functionality"""
        
        # Arrange - First perform a transfer to bank to get a valid reference
        transfer_request = get_dynamic_transfer_to_bank_request()
        transfer_response = api_instance_disbursement.transfer_to_bank(transfer_request)
        
        # Create inquiry status request using the transfer response
        partner_ref_no = transfer_response.partner_reference_no or transfer_request.partner_reference_no
        inquiry_request = get_transfer_to_bank_inquiry_status_request(partner_ref_no)
        
        # Act
        api_response = api_instance_disbursement.transfer_to_bank_inquiry_status(inquiry_request)
        
        # Assert - Check response structure and required fields
        assert isinstance(api_response, TransferToBankInquiryStatusResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        assert api_response.service_code is not None, 'Service code should not be empty'
        assert api_response.latest_transaction_status is not None, 'Latest transaction status should not be empty'
        
        # Assert - Check service code matches request
        assert api_response.service_code == inquiry_request.service_code, 'Service code should match request'
        
        # Assert - Check original reference numbers if present
        if hasattr(api_response, 'original_partner_reference_no') and api_response.original_partner_reference_no is not None:
            assert api_response.original_partner_reference_no == inquiry_request.original_partner_reference_no, 'Original partner reference number should match request'
        
        # Assert - Check transaction status is valid
        valid_statuses = ['00', '01', '02', '03', '04', '05', '06', '07']
        assert api_response.latest_transaction_status in valid_statuses, f'Latest transaction status should be one of {valid_statuses}'

    def test_transfer_to_dana_success(self, api_instance_disbursement: DisbursementApi):
        """Should successfully perform transfer to DANA operation"""
        
        # Arrange
        request = get_dynamic_transfer_to_dana_request()
        
        # Act
        api_response = api_instance_disbursement.transfer_to_dana(request)
        
        # Assert
        assert isinstance(api_response, TransferToDanaResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        assert api_response.partner_reference_no is not None, 'Partner reference number should not be empty'
        assert api_response.amount is not None, 'Amount should not be null'
        
        # Assert - Check partner reference number matches request
        assert api_response.partner_reference_no == request.partner_reference_no, 'Partner reference number should match request'
        
    def test_transfer_to_dana_inquiry_status_success(self, api_instance_disbursement: DisbursementApi):
        """Should successfully inquire transfer to DANA status"""
        
        # Arrange - First perform a transfer to DANA to get a valid reference
        transfer_request = get_dynamic_transfer_to_dana_request()
        transfer_response = api_instance_disbursement.transfer_to_dana(transfer_request)
        
        # Create inquiry status request using the transfer response
        inquiry_request = get_transfer_to_dana_inquiry_status_request(
            transfer_response.partner_reference_no
        )
        
        # Wait a bit before checking status
        time.sleep(2)
        
        # Act
        api_response = api_instance_disbursement.transfer_to_dana_inquiry_status(inquiry_request)
        
        # Assert
        assert isinstance(api_response, TransferToDanaInquiryStatusResponse)
        assert api_response.response_code is not None, 'Response code should not be empty'
        assert api_response.response_message is not None, 'Response message should not be empty'
        assert api_response.original_partner_reference_no is not None, 'Original partner reference number should not be empty'
        assert api_response.service_code is not None, 'Service code should not be empty'
        assert api_response.amount is not None, 'Amount should not be null'
        assert api_response.latest_transaction_status is not None, 'Latest transaction status should not be empty'
        # Python test may check for transaction_status_desc if available
        if hasattr(api_response, 'transaction_status_desc'):
            assert api_response.transaction_status_desc is not None, 'Transaction status description should not be empty'
        
        # Assert - Check fields match request
        assert api_response.original_partner_reference_no == inquiry_request.original_partner_reference_no, 'Original partner reference number should match request'
        assert api_response.service_code == inquiry_request.service_code, 'Service code should match request'
        
        # Assert - Check transaction status is valid
        valid_statuses = ['00', '01', '02', '03', '04', '05', '06', '07']
        assert api_response.latest_transaction_status in valid_statuses, 'Latest transaction status should be valid'
        
  
        