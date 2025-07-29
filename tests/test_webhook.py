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

import json
import os
from dana.webhook.finish_notify_request import FinishNotifyRequest
from dana.webhook import WebhookParser
from dana.utils.snap_header import SnapHeader
# Import fixtures directly from their modules to avoid circular imports
from tests.fixtures.api_client import api_instance_payment_gateway
from tests.fixtures.payment_gateway import webhook_key_pair

class TestWebhookParser:
    def test_webhook_signature_and_parsing_success(self):
        public_key, private_key = os.getenv("WEBHOOK_PUBLIC_KEY"), os.getenv("WEBHOOK_PRIVATE_KEY")
        parser = WebhookParser(public_key=public_key)
        webhook_http_method = "POST"
        webhook_relative_url = "/v1.0/debit/notify"
        webhook_body_dict = {
            "originalPartnerReferenceNo": "TESTPN20240101001",
            "originalReferenceNo": "TESTREF20240101001",
            "merchantId": "TESTMERCH001",
            "subMerchantId": "TESTSUBMERCH001",
            "amount": {"value": "15000.00", "currency": "IDR"},
            "latestTransactionStatus": "00",
            "transactionStatusDesc": "Success",
            "createdTime": "2024-01-01T10:00:00+07:00",
            "finishedTime": "2024-01-01T10:00:05+07:00"
        }
        webhook_body_str = json.dumps(webhook_body_dict, separators=(",", ":"))
        # Generate signature headers with SnapHeader
        generated_headers = SnapHeader.get_snap_generated_auth(
            method=webhook_http_method,
            resource_path=webhook_relative_url,
            body=webhook_body_str,
            private_key=private_key
        )
        headers = {
            "X-TIMESTAMP": generated_headers["X-TIMESTAMP"]["value"],
            "X-SIGNATURE": generated_headers["X-SIGNATURE"]["value"]
        }
        result = parser.parse_webhook(
            http_method=webhook_http_method,
            relative_path_url=webhook_relative_url,
            headers=headers,
            body=webhook_body_str
        )
        assert isinstance(result, FinishNotifyRequest)
        assert result.to_dict() == webhook_body_dict
