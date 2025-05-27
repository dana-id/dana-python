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

import base64
import hashlib
import json

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from dana.payment_gateway.v1.models.finish_notify_request import FinishNotifyRequest

class WebhookParser:
    """
    Verifies incoming webhook signatures and parse webhook request into FinishNotifyRequest object
    """
    def __init__(self, gateway_public_key_pem: str):
        self.public_key = serialization.load_pem_public_key(
            gateway_public_key_pem.encode("utf-8")
        )

    @staticmethod
    def _minify_json(json_str: str) -> str:
        # Remove whitespace and sort keys
        obj = json.loads(json_str)
        return json.dumps(obj, separators=(",", ":"))

    @staticmethod
    def _sha256_lower_hex(data: str) -> str:
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    def _construct_string_to_verify(
        self,
        http_method: str,
        relative_path_url: str,
        body: str,
        x_timestamp: str
    ) -> str:
        minified_body = self._minify_json(body)
        body_hash = self._sha256_lower_hex(minified_body)
        return f"{http_method}:{relative_path_url}:{body_hash}:{x_timestamp}"

    def parse_webhook(
        self,
        http_method: str,
        relative_path_url: str,
        headers: dict,
        body: str
    ) -> FinishNotifyRequest:
        x_signature = headers.get("X-SIGNATURE")
        x_timestamp = headers.get("X-TIMESTAMP")
        
        if not x_signature or not x_timestamp:
            raise ValueError("Missing X-SIGNATURE or X-TIMESTAMP header.")

        string_to_verify = self._construct_string_to_verify(
            http_method=http_method,
            relative_path_url=relative_path_url,
            body=body,
            x_timestamp=x_timestamp
        )
        signature_bytes = base64.b64decode(x_signature)
       
        try:
            self.public_key.verify(
                signature_bytes,
                string_to_verify.encode('utf-8'),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except InvalidSignature:
            raise ValueError("Signature verification failed.")

        try:
            payload_dict = json.loads(body)
            return FinishNotifyRequest.from_dict(payload_dict)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in request body.")
        except Exception as e:
            raise ValueError(f"Failed to parse body into FinishNotifyRequest: {e}")