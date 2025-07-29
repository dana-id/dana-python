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
import os

from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from dana.webhook.finish_notify_request import FinishNotifyRequest

class WebhookParser:
    """
    Verifies incoming webhook signatures and parse webhook request into FinishNotifyRequest object
    """
    def __init__(self, public_key: str = None, public_key_path: str = None):
        """
        Initializes the WebhookParser.
        Args:
            public_key (str, optional): The public key as a string. Defaults to None.
            public_key_path (str, optional): Path to the public key PEM file. Defaults to None.
                                          If provided, this will be prioritized over public_key.
        Raises:
            ValueError: If neither public_key nor public_key_path is provided,
                        if the key file cannot be read, or if the key format is invalid.
        """
        key_input_content = ""
        if public_key_path:
            try:
                key_input_content = Path(public_key_path).read_text().strip()
            except Exception as e:
                raise ValueError(f"Failed to read key from file path '{public_key_path}': {e}")
        elif public_key:
            key_input_content = public_key.strip()
        else:
            raise ValueError("Either 'public_key' or 'public_key_path' must be provided.")

        if not key_input_content:
             raise ValueError("Key content is empty.")

        normalized_key_pem = self._normalize_pem_key(key_input_content)
        try:
            self.public_key = serialization.load_pem_public_key(
                normalized_key_pem.encode("utf-8")
            )
        except Exception as e:
            # Catch specific exceptions from cryptography if possible, or re-raise with context
            raise ValueError(f"Failed to load public key: {e}. Processed key: \n{normalized_key_pem}")

    def _normalize_pem_key(self, key_content: str) -> str:
        """
        Normalizes various key input formats (already read from file or string) to a standard PEM string.
        Args:
            key_content (str): The raw key content string.
        Returns:
            str: The normalized PEM formatted key string.
        """        
        if "\\n" in key_content and "-----BEGIN" in key_content and "-----END" in key_content:
            key_content = key_content.replace("\\n", "\n")
        
        has_begin_marker = "-----BEGIN" in key_content
        has_end_marker = "-----END" in key_content

        if has_begin_marker and has_end_marker:
            return key_content
        elif not has_begin_marker and not has_end_marker:
            base64_key_data = key_content.replace("\n", "").strip()
            if not base64_key_data:
                raise ValueError("Key content is empty after removing newlines and markers.")
            
            key_type_header = "PUBLIC KEY"
            
            pem_lines = [f"-----BEGIN {key_type_header}-----"]
            for i in range(0, len(base64_key_data), 64):
                pem_lines.append(base64_key_data[i:i+64])
            pem_lines.append(f"-----END {key_type_header}-----")
            return "\n".join(pem_lines)
        else:
            raise ValueError(
                "Invalid key format: Key has incomplete PEM markers or an unrecognized structure. "
                "Ensure the key is a valid file path, a full PEM string (multi-line or env-style with \\n), "
                "or a base64 key data string (with or without newlines, without PEM markers)."
            )

    @staticmethod
    def _minify_json(json_str: str) -> str:
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