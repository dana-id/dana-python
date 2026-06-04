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
import re

from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from dana.webhook.finish_notify_request import FinishNotifyRequest

# Sandbox gateway public key used for webhook signature verification when DANA_ENV/ENV is sandbox.
SANDBOX_WEBHOOK_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnaKVGRbin4Wh4KN35OPh
ytJBjYTz7QZKSZjmHfiHxFmulfT87rta+IvGJ0rCBgg+1EtKk1hX8G5gPGJs1htJ
5jHa3/jCk9l+luzjnuT9UVlwJahvzmFw+IoDoM7hIPjsLtnIe04SgYo0tZBpEmkQ
vUGhmHPqYnUGSSMIpDLJDvbyr8gtwluja1SbRphgDCoYVXq+uUJ5HzPS049aaxTS
nfXh/qXuDoB9EzCrgppLDS2ubmk21+dr7WaO/3RFjnwx5ouv6w+iC1XOJKar3CTk
X6JV1OSST1C9sbPGzMHZ8AGB51BM0mok7davD/5irUk+f0C25OgzkwtxAt80dkDo
/QIDAQAB
-----END PUBLIC KEY-----"""


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
        env = (os.getenv("DANA_ENV") or os.getenv("ENV") or "").strip().lower()
        if env == "sandbox" or env == "":
            key_input_content = SANDBOX_WEBHOOK_PUBLIC_KEY
        elif public_key_path:
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
    def _is_json_minified(json_str: str) -> bool:
        """
        Performs a quick heuristic check to see if JSON is already minified
        """
        indicators = [": ", ", ", "{ ", "[ ", "\n", "\t", "\r"]
        
        for indicator in indicators:
            if indicator in json_str:
                return False
        
        return True


    @staticmethod
    def _minify_json(json_str: str) -> tuple[str, Exception]:
        """
        Compacts a JSON string by removing unnecessary whitespace
        """
        try:
            obj = json.loads(json_str)
            minified = json.dumps(obj, separators=(",", ":"))
            return minified, None
        except json.JSONDecodeError as e:
            return "", Exception(f"MinifyJSON: failed to unmarshal JSON: {e}")
        except Exception as e:
            return "", Exception(f"MinifyJSON: failed to marshal JSON for minification: {e}")

    @staticmethod
    def _has_triple_escaped_json_string_field(json_str: str) -> bool:
        return '":"{\\\\\\"' in json_str

    @staticmethod
    def _process_over_escaped_minified_json(json_str: str) -> str:
        normalized = json_str.replace('\\\\"', '"')
        return WebhookParser._process_nested_json_fields(normalized)

    @staticmethod
    def _process_nested_json_fields(json_str: str) -> str:
        normalized_str = json_str.replace('\\\\"', '\\"')

        def replace_func(match):
            field_name = match.group(1)
            json_value = match.group(2)
            escaped_value = json_value.replace('"', '\\"')
            return f'"{field_name}":"{escaped_value}"'

        return re.sub(r'"(\w+)":"(\{.*?\})"', replace_func, normalized_str)

    @staticmethod
    def _ensure_minified_json(json_str: str) -> tuple[str, Exception]:
        """
        Ensures JSON string is minified
        Returns tuple of (minified_json, error)
        """
        try:
            if WebhookParser._is_json_minified(json_str) and not WebhookParser._has_triple_escaped_json_string_field(json_str):
                return json_str, None

            if WebhookParser._is_json_minified(json_str):
                return WebhookParser._process_over_escaped_minified_json(json_str), None

            normalized_str = json_str.replace('\\\\"', '\\"')
            processed_str = WebhookParser._process_nested_json_fields(normalized_str)

            if WebhookParser._is_json_minified(processed_str):
                return processed_str, None

            return WebhookParser._minify_json(processed_str)

        except json.JSONDecodeError as e:
            return "", Exception(f"EnsureMinifiedJSON: failed to unmarshal JSON: {e}")
        except Exception as e:
            return "", Exception(f"EnsureMinifiedJSON: failed to marshal JSON for minification: {e}")

    @staticmethod
    def _is_valid_json(json_str: str) -> bool:
        try:
            json.loads(json_str)
            return True
        except json.JSONDecodeError:
            return False

    @staticmethod
    def _collapse_triple_backslash_quotes(s: str) -> str:
        if '\\\\\\"' not in s:
            return s
        return s.replace('\\\\\\"', '\\"')

    @staticmethod
    def _collapse_double_backslash_quotes(s: str) -> str:
        if '\\\\"' not in s:
            return s
        return s.replace('\\\\"', '"')

    @staticmethod
    def _remove_colon_space_before_quoted_value(s: str) -> str:
        if ': \\"' not in s:
            return s
        return s.replace(': \\"', ':\\"')

    @staticmethod
    def _normalize_over_escaped_quotes(s: str) -> str:
        if '\\\\"' in s:
            return s.replace('\\\\"', '\\"')
        return s

    @staticmethod
    def _body_forms_for_signature(request_body: str) -> list[str]:
        seen: set[str] = set()
        forms: list[str] = []

        def add(form: str) -> None:
            if form and form not in seen:
                seen.add(form)
                forms.append(form)

        collapsed = WebhookParser._collapse_triple_backslash_quotes(request_body)
        if collapsed != request_body and WebhookParser._is_valid_json(collapsed):
            add(collapsed)

        collapsed_spaced = WebhookParser._remove_colon_space_before_quoted_value(collapsed)
        if collapsed_spaced != request_body and WebhookParser._is_valid_json(collapsed_spaced):
            add(collapsed_spaced)

        collapsed = WebhookParser._collapse_double_backslash_quotes(request_body)
        if collapsed != request_body and WebhookParser._is_valid_json(collapsed):
            add(collapsed)

        spaced = WebhookParser._remove_colon_space_before_quoted_value(request_body)
        if spaced != request_body and WebhookParser._is_valid_json(spaced):
            add(spaced)

        collapsed = WebhookParser._collapse_triple_backslash_quotes(spaced)
        if collapsed != request_body and WebhookParser._is_valid_json(collapsed):
            add(collapsed)

        if WebhookParser._is_valid_json(request_body):
            add(request_body)

        normalized = WebhookParser._normalize_over_escaped_quotes(request_body)
        if normalized != request_body and WebhookParser._is_json_minified(normalized) and WebhookParser._is_valid_json(normalized):
            add(normalized)

        nested_processed = WebhookParser._process_nested_json_fields(request_body)
        if nested_processed != request_body:
            add(nested_processed)

        minified, err = WebhookParser._ensure_minified_json(request_body)
        if err:
            if not forms:
                raise ValueError("failed to prepare any signature body form") from err
        else:
            add(minified)

        if not forms:
            raise ValueError("failed to prepare any signature body form")
        return forms

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
        path = relative_path_url if relative_path_url.startswith("/") else f"/{relative_path_url}"
        body_hash = self._sha256_lower_hex(body)
        return f"{http_method.upper()}:{path}:{body_hash}:{x_timestamp}"

    def _verify_signature(
        self,
        http_method: str,
        relative_path_url: str,
        body: str,
        x_timestamp: str,
        x_signature: str,
    ) -> None:
        body_forms = self._body_forms_for_signature(body)
        signature_bytes = base64.b64decode(x_signature)

        for body_form in body_forms:
            string_to_verify = self._construct_string_to_verify(
                http_method, relative_path_url, body_form, x_timestamp
            )
            try:
                self.public_key.verify(
                    signature_bytes,
                    string_to_verify.encode("utf-8"),
                    padding.PKCS1v15(),
                    hashes.SHA256(),
                )
                return
            except InvalidSignature:
                continue

        raise ValueError("Signature verification failed.")

    def parse_webhook(
        self,
        http_method: str,
        relative_path_url: str,
        headers: dict,
        body: str
    ) -> FinishNotifyRequest:
        x_signature = headers.get("X-SIGNATURE") or headers.get("X-Signature") or headers.get("X-signature") or headers.get("x-signature")
        x_timestamp = headers.get("X-TIMESTAMP") or headers.get("X-Timestamp") or headers.get("X-timestamp") or headers.get("x-timestamp")
        
        if not x_signature or not x_timestamp:
            raise ValueError("Missing X-SIGNATURE or X-TIMESTAMP header.")

        self._verify_signature(http_method, relative_path_url, body, x_timestamp, x_signature)

        # Try multiple body transformations for parsing in order of likelihood:
        # 1. Collapsed triple-backslash form (handles over-escaped \\\" → \")
        # 2. Process nested JSON fields (handles bare-quote inner JSON like "field":"{...}")
        # 3. ensureMinifiedJson fallback for pretty-printed bodies
        payload_dict = None
        for candidate in [
            self._collapse_triple_backslash_quotes(body),
            self._process_nested_json_fields(body),
        ]:
            try:
                payload_dict = json.loads(candidate)
                break
            except json.JSONDecodeError:
                continue

        if payload_dict is None:
            processed_body, err = self._ensure_minified_json(body)
            if err:
                raise ValueError(f"Failed to process JSON body: {err}")
            try:
                payload_dict = json.loads(processed_body)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON in request body.")

        try:
            return FinishNotifyRequest.from_dict(payload_dict)
        except Exception as e:
            raise ValueError(f"Failed to parse body into FinishNotifyRequest: {e}")