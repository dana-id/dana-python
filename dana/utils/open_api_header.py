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

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
import base64
import uuid
import json
from typing import Any, List, Mapping, Optional
from datetime import datetime, timedelta, timezone

from dana.utils.open_api_configuration import APIKeyAuthSetting

# Open API headers
VERSION = "version"
FUNCTION = "function"
CLIENT_ID = "clientId"
REQ_TIME = "reqTime"
REQ_MSG_ID = "reqMsgId"
CLIENT_SECRET = "clientSecret"
RESERVE = "reserve"

class OpenApiHeader:
    OpenApiRuntimeHeaders: List[str] = [
        VERSION, FUNCTION, CLIENT_ID, REQ_TIME, 
        REQ_MSG_ID, CLIENT_SECRET, RESERVE
    ]

    @staticmethod
    def merge_with_open_api_runtime_headers(auth_from_users: List[str]) -> List[str]:
        """
        Remove any items containing 'private' or 'env' and merge with Open API runtime headers.
        """
        # Filter out auth items containing 'private' or 'env'
        filtered_auth = [
            auth for auth in auth_from_users
            if 'private' not in auth.lower() and 'env' not in auth.lower()
        ]

        return list(set(filtered_auth).union(OpenApiHeader.OpenApiRuntimeHeaders))

    @staticmethod
    def generate_open_api_signature(
        body: str,
        private_key: str = None,
        private_key_path: str = None
    ) -> str:
        """
        Generate OPEN_API signature according to the official documentation:
        1. Compose the string to sign: (<HTTP BODY>)
        2. Apply SHA-256 with RSA-2048 encryption using pkcs8 private key
        3. Encode the result to base64
        
        Args:
            body: The HTTP request body as string (contains both request and signature fields)
            private_key: Private key content as string
            private_key_path: Path to private key file
            
        Returns:
            Base64 encoded signature string
        """
        
        # Extract only the request part for signing (excluding signature field)
        body_json = json.loads(body)
        request_data = body_json['request']
        # Generate JSON string with consistent formatting (no spaces, sorted keys)
        request_body = json.dumps(request_data)
        


        def get_usable_private_key(private_key: str, private_key_path: str):
            if private_key_path:
                with open(private_key_path, 'rb') as pem_in:
                    pemlines = pem_in.read()
                    private_key_obj = load_pem_private_key(pemlines, None, default_backend())
                    return private_key_obj
            elif private_key:
                # Handle escaped newlines
                private_key = private_key.replace("\\n", "\n")
                private_key_obj = serialization.load_pem_private_key(
                    private_key.encode(),
                    password=None,
                    backend=default_backend()
                )
                return private_key_obj
            else:
                raise ValueError("Provide one of private_key or private_key_path")

        # Get the private key object
        private_key_obj = get_usable_private_key(private_key=private_key, private_key_path=private_key_path)
        
        # For OPEN_API, sign only the request part (not the full body which includes signature)
        string_to_sign = request_body
        
        # Generate signature using SHA256 with RSA
        signature = private_key_obj.sign(
            string_to_sign.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        # Encode to base64
        encoded_signature = base64.b64encode(signature).decode()
        return encoded_signature

    @staticmethod
    def get_open_api_generated_headers(
        method: str,
        resource_path: str, 
        body: str, 
        client_secret: Optional[str] = None,
        function_name: Optional[str] = None,
        client_id: Optional[str] = None,
        version: str = "2.0",
        private_key: Optional[str] = None,
        private_key_path: Optional[str] = None,
    ) -> Mapping[str, APIKeyAuthSetting]:
        """
        Generate Open API headers following the same pattern as snap_header.py
        """
        def generateOpenApiSetting(key: str, value: Any) -> APIKeyAuthSetting:
            return {
                'in': 'header',
                'key': key,
                'type': 'api_key',
                'value': value
            }
        
        if not client_secret:
            raise ValueError("CLIENT_SECRET is required for Open API authentication")
        
        if not function_name:
            raise ValueError("function_name is required for Open API authentication")
        
        if not client_id:
            raise ValueError("CLIENT_ID is required for Open API authentication")
        
        # Generate timestamp in Jakarta time (GMT+7)
        jakarta_time = datetime.now(timezone.utc) + timedelta(hours=7)
        timestamp = jakarta_time.strftime('%Y-%m-%dT%H:%M:%S+07:00')
        
        # Generate unique request message ID
        req_msg_id = str(uuid.uuid4())
        
        # Return auth settings following snap_header pattern
        return {
            VERSION: generateOpenApiSetting(key=VERSION, value=version),
            FUNCTION: generateOpenApiSetting(key=FUNCTION, value=function_name),
            CLIENT_ID: generateOpenApiSetting(key=CLIENT_ID, value=client_id),
            REQ_TIME: generateOpenApiSetting(key=REQ_TIME, value=timestamp),
            REQ_MSG_ID: generateOpenApiSetting(key=REQ_MSG_ID, value=req_msg_id),
            CLIENT_SECRET: generateOpenApiSetting(key=CLIENT_SECRET, value=client_secret),
            RESERVE: generateOpenApiSetting(key=RESERVE, value="{}")
        }

    @staticmethod
    def get_open_api_generated_auth_with_signature(
        method: str,
        resource_path: str, 
        body: str, 
        client_secret: Optional[str] = None,
        function_name: Optional[str] = None,
        client_id: Optional[str] = None,
        version: str = "2.0",
        private_key: Optional[str] = None,
        private_key_path: Optional[str] = None,
    ) -> tuple[Mapping[str, APIKeyAuthSetting], str]:
        """
        Generate Open API authentication headers and signature.
        
        Returns:
            tuple: (headers_dict, signature_string)
        """
        # Generate headers
        headers = OpenApiHeader.get_open_api_generated_headers(
            method=method,
            resource_path=resource_path,
            body=body,
            client_secret=client_secret,
            function_name=function_name,
            client_id=client_id,
            version=version,
            private_key=private_key,
            private_key_path=private_key_path
        )
        
        # Generate signature if private key is provided
        signature = ""
        if private_key or private_key_path:
            signature = OpenApiHeader.generate_open_api_signature(
                body=body,
                private_key=private_key,
                private_key_path=private_key_path
            )
        
        return headers, signature 