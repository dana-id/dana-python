# # Copyright 2025 PT Espay Debit Indonesia Koe
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# import time
# from dana.disbursement.v1.api import DisbursementApi
# from dana.disbursement.v1.models import (
#     DanaAccountInquiryRequest,
#     TransferToDanaRequest,
#     TransferToDanaInquiryStatusRequest,
#     BankAccountInquiryRequest,
#     TransferToBankRequest,
#     TransferToBankInquiryStatusRequest
# )
# from dana.rest import ApiException

# from tests.fixtures.api_client import api_instance_disbursement
# from tests.fixtures.disbursement import (
#     account_inquiry_request,
#     customer_top_up_request,
#     customer_top_up_inquiry_status_request,
#     bank_account_inquiry_request,
#     transfer_to_bank_request,
#     transfer_to_bank_inquiry_status_request
# )


# class TestDisbursementApi:
#     """Test class for Disbursement API endpoints"""
    
#     def test_dana_account_inquiry_success(self, api_instance_disbursement: DisbursementApi, account_inquiry_request: DanaAccountInquiryRequest):
#         """Should give success response and validate DANA account inquiry functionality"""
        
#         # Act
#         api_response = api_instance_disbursement.account_inquiry(account_inquiry_request)
#         print(api_response, "api_responses")
#         # Assert - Check response structure and required fields
#         assert api_response is not None
#         assert hasattr(api_response, 'response_code')
#         assert hasattr(api_response, 'response_message')
#         assert hasattr(api_response, 'customer_name')
#         assert hasattr(api_response, 'min_amount')
#         assert hasattr(api_response, 'max_amount')
#         assert hasattr(api_response, 'amount')
#         assert hasattr(api_response, 'fee_amount')
        
#         # Assert - Check expected success response
#         # Note: Actual response codes may vary based on environment and test data
#         assert api_response.response_code is not None, "Response code should not be empty"
#         assert api_response.response_message is not None, "Response message should not be empty"
#         assert api_response.customer_name is not None, "Customer name should not be empty"
        
#         # Assert - Check Money objects are properly structured
#         assert hasattr(api_response.min_amount, 'value')
#         assert hasattr(api_response.min_amount, 'currency')
#         assert hasattr(api_response.max_amount, 'value')
#         assert hasattr(api_response.max_amount, 'currency')
#         assert hasattr(api_response.amount, 'value')
#         assert hasattr(api_response.amount, 'currency')
#         assert hasattr(api_response.fee_amount, 'value')
#         assert hasattr(api_response.fee_amount, 'currency')
        
#         # Assert - Check currency consistency
#         assert api_response.amount.currency == api_response.fee_amount.currency, "Amount and fee currency should match"

#     def test_bank_account_inquiry_success(self, api_instance_disbursement: DisbursementApi, bank_account_inquiry_request: BankAccountInquiryRequest):
#         """Should give success response and validate bank account inquiry functionality"""
        
#         # Act
#         api_response = api_instance_disbursement.bank_account_inquiry(bank_account_inquiry_request)
        
#         # Assert - Check response structure and required fields
#         assert api_response is not None
#         assert hasattr(api_response, 'response_code')
#         assert hasattr(api_response, 'response_message')
#         assert hasattr(api_response, 'beneficiary_account_number')
#         assert hasattr(api_response, 'beneficiary_account_name')
#         assert hasattr(api_response, 'amount')
        
#         # Assert - Check expected success response
#         assert api_response.response_code is not None, "Response code should not be empty"
#         assert api_response.response_message is not None, "Response message should not be empty"
#         assert api_response.beneficiary_account_number is not None, "Beneficiary account number should not be empty"
#         assert api_response.beneficiary_account_name is not None, "Beneficiary account name should not be empty"
        
#         # Assert - Check account details match request
#         assert api_response.beneficiary_account_number == bank_account_inquiry_request.beneficiary_account_number, "Account number should match request"
        
#         # Assert - Check Money object structure
#         assert hasattr(api_response.amount, 'value')
#         assert hasattr(api_response.amount, 'currency')
#         assert api_response.amount.value == bank_account_inquiry_request.amount.value, "Amount should match request"
#         assert api_response.amount.currency == bank_account_inquiry_request.amount.currency, "Currency should match request"
        
#         # Assert - Check additional info contains fee amount
#         if hasattr(api_response, 'additional_info') and api_response.additional_info:
#             assert 'fee_amount' in api_response.additional_info or hasattr(api_response.additional_info, 'fee_amount'), "Fee amount should be present in additional info"

#     def test_transfer_to_bank_success(self, api_instance_disbursement: DisbursementApi, transfer_to_bank_request: TransferToBankRequest):
#         """Should give success response and validate transfer to bank functionality"""
        
#         # Act
#         api_response = api_instance_disbursement.transfer_to_bank(transfer_to_bank_request)
        
#         # Assert - Check response structure and required fields
#         assert api_response is not None
#         assert hasattr(api_response, 'response_code')
#         assert hasattr(api_response, 'response_message')
#         assert hasattr(api_response, 'reference_number')
        
#         # Assert - Check expected success response
#         assert api_response.response_code is not None, "Response code should not be empty"
#         assert api_response.response_message is not None, "Response message should not be empty"
#         assert api_response.reference_number is not None, "Reference number should not be empty"
        
#         # Assert - Check partner reference number matches if present
#         if hasattr(api_response, 'partner_reference_no') and api_response.partner_reference_no:
#             assert api_response.partner_reference_no == transfer_to_bank_request.partner_reference_no, "Partner reference number should match request"
        
#         # Assert - Check transaction date format if present
#         assert hasattr(api_response, 'transaction_date')

#     def test_transfer_to_bank_inquiry_status_success(self, api_instance_disbursement: DisbursementApi, transfer_to_bank_inquiry_status_request: TransferToBankInquiryStatusRequest, transfer_to_bank_request: TransferToBankRequest):
#         """Should give success response and validate transfer to bank inquiry status functionality"""
        
#         api_response_transfer = api_instance_disbursement.transfer_to_bank(transfer_to_bank_request)
#         transfer_to_bank_inquiry_status_request.original_partner_reference_no = api_response_transfer.partner_reference_no
#         api_response = api_instance_disbursement.transfer_to_bank_inquiry_status(transfer_to_bank_inquiry_status_request)
        
#         # Assert - Check response structure and required fields
#         assert api_response is not None
#         assert hasattr(api_response, 'response_code')
#         assert hasattr(api_response, 'response_message')
#         assert hasattr(api_response, 'service_code')
#         assert hasattr(api_response, 'latest_transaction_status')
        
#         # Assert - Check expected success response
#         assert api_response.response_code is not None, "Response code should not be empty"
#         assert api_response.response_message is not None, "Response message should not be empty"
#         assert api_response.service_code is not None, "Service code should not be empty"
#         assert api_response.latest_transaction_status is not None, "Latest transaction status should not be empty"
        
#         # Assert - Check service code matches request
#         assert api_response.service_code == transfer_to_bank_inquiry_status_request.service_code, "Service code should match request"
        
#         # Assert - Check original reference numbers if present
#         if hasattr(api_response, 'original_partner_reference_no') and api_response.original_partner_reference_no:
#             assert api_response.original_partner_reference_no == transfer_to_bank_inquiry_status_request.original_partner_reference_no, "Original partner reference number should match request"
        
#         # Assert - Check transaction status is valid
#         valid_statuses = ["00", "01", "02", "03", "04", "05", "06", "07"]
#         assert api_response.latest_transaction_status in valid_statuses, f"Latest transaction status should be one of {valid_statuses}"

#     def test_transfer_to_dana_success(self, api_instance_disbursement: DisbursementApi, customer_top_up_request: TransferToDanaRequest):
#         """Should successfully perform transfer to DANA operation"""
        
#         # Act
#         api_response = api_instance_disbursement.customer_top_up(customer_top_up_request)
        
#         # Assert
#         assert api_response is not None
#         assert hasattr(api_response, 'response_code')
#         assert hasattr(api_response, 'response_message')
#         assert hasattr(api_response, 'partner_reference_no')
#         assert hasattr(api_response, 'amount')
        
#         assert api_response.response_code is not None
#         assert api_response.response_message is not None
#         assert api_response.partner_reference_no == customer_top_up_request.partner_reference_no
        
#     # def test_transfer_to_dana_inquiry_status_success(self, api_instance_disbursement: DisbursementApi, customer_top_up_inquiry_status_request: TransferToDanaInquiryStatusRequest, customer_top_up_request: TransferToDanaRequest):
#     #     """Should successfully inquire transfer to DANA status"""
        

#     #     # Act
#     #     api_response_topup = api_instance_disbursement.customer_top_up(customer_top_up_request)
        
#     #     # Update the inquiry status request with the actual partner reference number from transfer to DANA
#     #     customer_top_up_inquiry_status_request.original_partner_reference_no = customer_top_up_request.partner_reference_no
#     #     time.sleep(5)
#     #     api_response = api_instance_disbursement.customer_top_up_inquiry_status(customer_top_up_inquiry_status_request)
        
#     #     # Assert
#     #     assert api_response is not None
#     #     assert hasattr(api_response, 'response_code')
#     #     assert hasattr(api_response, 'response_message')
#     #     assert hasattr(api_response, 'original_partner_reference_no')
#     #     assert hasattr(api_response, 'service_code')
#     #     assert hasattr(api_response, 'amount')
#     #     assert hasattr(api_response, 'latest_transaction_status')
#     #     assert hasattr(api_response, 'transaction_status_desc')
        
#     #     assert api_response.response_code is not None
#     #     assert api_response.response_message is not None
#     #     assert api_response.original_partner_reference_no == customer_top_up_request.partner_reference_no
#     #     assert api_response.service_code == customer_top_up_inquiry_status_request.service_code
        
  
        