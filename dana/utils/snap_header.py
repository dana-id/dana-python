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
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend
import re
import base64
from hashlib import sha256
import uuid
import os
import json
from typing import Any, List, Mapping
from datetime import datetime, timedelta, timezone

from dana.utils.snap_configuration import APIKeyAuthSetting

X_TIMESTAMP = "X-TIMESTAMP"
X_SIGNATURE = "X-SIGNATURE"
X_EXTERNALID = "X-EXTERNAL-ID"
X_CLIENT_KEY = "X-CLIENT-KEY"
X_PARTNER_ID = "X-PARTNER-ID"
X_IP_ADDRESS = "X-IP-ADDRESS"
X_DEVICE_ID = "X-DEVICE-ID"
X_LATITUDE = "X-LATITUDE"
X_LONGITUDE = "X-LONGITUDE"
CHANNEL_ID = "CHANNEL-ID"
AUTHORIZATION_CUSTOMER = "Authorization-Customer"

class SnapHeader:
    SnapRuntimeHeaders: List[str] = [
        X_TIMESTAMP, X_SIGNATURE, 
        X_EXTERNALID, CHANNEL_ID
    ]
    SnapApplyTokenRuntimeHeaders: List[str] = [
        X_TIMESTAMP, X_SIGNATURE, 
        X_CLIENT_KEY, CHANNEL_ID
    ]
    SnapApplyOTTRuntimeHeaders: List[str] = [
        AUTHORIZATION_CUSTOMER, X_TIMESTAMP, X_SIGNATURE, 
        X_PARTNER_ID, X_EXTERNALID, X_IP_ADDRESS, 
        X_DEVICE_ID, X_LATITUDE, X_LONGITUDE, CHANNEL_ID
    ]
    SnapUnbindingAccountRuntimeHeaders: List[str] = [
        AUTHORIZATION_CUSTOMER, X_TIMESTAMP, X_SIGNATURE, 
        X_PARTNER_ID, X_EXTERNALID, X_IP_ADDRESS, 
        X_DEVICE_ID, X_LATITUDE, X_LONGITUDE, CHANNEL_ID
    ]
    SnapBalanceInquiryRuntimeHeaders: List[str] = [
        AUTHORIZATION_CUSTOMER, X_TIMESTAMP, X_SIGNATURE, 
        X_PARTNER_ID, X_EXTERNALID, X_DEVICE_ID, CHANNEL_ID
    ]

    @staticmethod
    def merge_with_snap_runtime_headers(auth_from_users: List[str], scenario: str="") -> List[str]:
        """
        Remove any items containing 'private' or 'env' and merge with Snap runtime headers.
        """
        # Filter out auth items containing 'private' or 'env'
        filtered_auth = [
            auth for auth in auth_from_users
            if 'private' not in auth.lower() and 'env' not in auth.lower()
        ]

        if scenario == "apply_token":
            # Remove X-PARTNER-ID as it's replaced by X-CLIENT-KEY in apply_token scenario
            filtered_auth = [
                auth for auth in filtered_auth 
                if auth != X_PARTNER_ID  # Explicitly exclude X-PARTNER-ID
            ]
            return list(set(filtered_auth).union(SnapHeader.SnapApplyTokenRuntimeHeaders))

        elif scenario == "apply_ott" or scenario == "unbinding_account":
            return list(set(filtered_auth).union(SnapHeader.SnapApplyOTTRuntimeHeaders))
        
        elif scenario == "balance_inquiry":
            return list(set(filtered_auth).union(SnapHeader.SnapBalanceInquiryRuntimeHeaders))
        
        else:
            return list(set(filtered_auth).union(SnapHeader.SnapRuntimeHeaders))

    @staticmethod
    def convert_to_pem(key: str, key_type: str) -> str:
        """
        Convert a key to PEM format
        
        Args:
            key: The key as a string
            key_type: Type of key ("PRIVATE" or "PUBLIC")
            
        Returns:
            The key in PEM format
        """
        # Determine if this is an RSA key or generic private key format
        possible_headers = [
            f"-----BEGIN {key_type} KEY-----",
            f"-----BEGIN RSA {key_type} KEY-----"
        ]
        possible_footers = [
            f"-----END {key_type} KEY-----",
            f"-----END RSA {key_type} KEY-----"
        ]
        
        delimiter = "\n"
        header_found = None
        footer_found = None
        
        # Clean up the key first
        key = key.strip()
        
        # Replace escaped newlines with actual newlines
        key = key.replace('\\n', "\n")
        
        # Check if key already has headers/footers
        for index, header in enumerate(possible_headers):
            if header in key and possible_footers[index] in key:
                header_found = header
                footer_found = possible_footers[index]
                break
        
        # If headers/footers found, extract and clean the body
        if header_found is not None and footer_found is not None:
            # Extract body between header and footer
            parts = key.split(header_found, 1)
            parts = parts[1].split(footer_found, 1)
            body = parts[0].strip()
            
            # Keep the original format but ensure proper line breaks
            body = re.sub(r'\s+', '', body)  # Remove all whitespace
            # Format with proper line breaks - chunk into 64-character lines
            formatted_body = ''
            for i in range(0, len(body), 64):
                formatted_body += body[i:i+64] + delimiter
            
            return header_found + delimiter + formatted_body + footer_found
        
        # For keys without headers/footers - try both RSA and standard formats
        # Remove all whitespace
        clean_key = re.sub(r'\s+', '', key)
        # Format with proper line breaks
        formatted_body = ''
        for i in range(0, len(clean_key), 64):
            formatted_body += clean_key[i:i+64] + delimiter
        
        # First attempt standard key format
        standard_header = f"-----BEGIN {key_type} KEY-----"
        standard_footer = f"-----END {key_type} KEY-----"
        formatted_key = standard_header + delimiter + formatted_body + standard_footer
        
        # Try to validate the key using cryptography library
        try:
            # For private keys
            if key_type == "PRIVATE":
                load_pem_private_key(formatted_key.encode(), password=None, backend=default_backend())
                return formatted_key
            # For public keys
            elif key_type == "PUBLIC":
                load_pem_public_key(formatted_key.encode(), backend=default_backend())
                return formatted_key
        except Exception:
            # If standard format fails, try RSA format
            pass
            
        # Try RSA format
        rsa_header = f"-----BEGIN RSA {key_type} KEY-----"
        rsa_footer = f"-----END RSA {key_type} KEY-----"
        rsa_formatted_key = rsa_header + delimiter + formatted_body + rsa_footer
        
        return rsa_formatted_key

    @staticmethod
    def get_usable_private_key(private_key: str = None, private_key_path: str = None) -> str:
        """
        Get usable private key from either file path or string content
        
        Args:
            private_key: Optional private key content as string
            private_key_path: Optional path to private key file
            
        Returns:
            str: Properly formatted private key as PEM
            
        Raises:
            ValueError: If neither private_key nor private_key_path is provided or valid
        """
        # If private_key_path is provided and exists, it takes precedence over private_key
        if private_key_path and os.path.exists(private_key_path):
            with open(private_key_path, 'rb') as pem_in:
                pemlines = pem_in.read()
                key = pemlines.decode('utf-8')
                return SnapHeader.convert_to_pem(key, "PRIVATE")
        
        # Handle direct private key string
        if private_key:
            # Replace escaped newlines with actual newlines
            key = private_key.replace("\\n", "\n")
            return SnapHeader.convert_to_pem(key, "PRIVATE")
            
        # Throw exception if neither key is provided
        raise ValueError("Provide one of private_key or private_key_path")
    
    @staticmethod
    def get_snap_generated_auth(
        method: str,
        resource_path: str, 
        body: str, 
        private_key: str = None, 
        private_key_path: str = None,
        scenario: str = "",
        client_key: str = None,
    ) -> Mapping[str, APIKeyAuthSetting]:
        
        def generateApiKeyAuthSetting(key: str, value: Any) -> APIKeyAuthSetting:
            return {
                'in': 'header',
                'key': key,
                'type': 'api_key',
                'value': value
            }


        # Use the class method to get the usable private key
        private_key = SnapHeader.get_usable_private_key(private_key=private_key,
                                                      private_key_path=private_key_path)

        jakarta_time = datetime.now(timezone.utc) + timedelta(hours=7)
        timestamp = jakarta_time.strftime('%Y-%m-%dT%H:%M:%S+07:00')

        hashed_payload = sha256(body.encode('utf-8')).hexdigest()

        private_key_obj = serialization.load_pem_private_key(
            private_key.encode(),
            password=None,
        )

        if scenario == "apply_token" and not client_key:
            raise ValueError("X_PARTNER_ID is required for apply_token scenario")
        elif scenario == "apply_token":
            data = f'{client_key}|{timestamp}'
        else:
            data = f'{method}:{resource_path}:{hashed_payload}:{timestamp}'
        
        signature = private_key_obj.sign(
            data.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        encoded_signature = base64.b64encode(signature).decode()

        if scenario == "apply_token":
            return {
                X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
                X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
                X_CLIENT_KEY: generateApiKeyAuthSetting(key=X_CLIENT_KEY, value=client_key),
                CHANNEL_ID: generateApiKeyAuthSetting(key=CHANNEL_ID, value='95221')
            }
        elif scenario == "apply_ott" or scenario == "unbinding_account":
            external_id = str(uuid.uuid4())
            body_dict: dict = json.loads(body)

            return {
                AUTHORIZATION_CUSTOMER: generateApiKeyAuthSetting(key=AUTHORIZATION_CUSTOMER, value=f"Bearer {body_dict.get('additionalInfo', {}).get('accessToken', '')}"),
                X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
                X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
                X_EXTERNALID: generateApiKeyAuthSetting(key=X_EXTERNALID, value=external_id),
                X_IP_ADDRESS: generateApiKeyAuthSetting(key=X_IP_ADDRESS, value=body_dict.get('additionalInfo', {}).get('endUserIpAddress', '')),
                X_DEVICE_ID: generateApiKeyAuthSetting(key=X_DEVICE_ID, value=body_dict.get('additionalInfo', {}).get('deviceId', '')),
                X_LATITUDE: generateApiKeyAuthSetting(key=X_LATITUDE, value=body_dict.get('additionalInfo', {}).get('latitude', '')),
                X_LONGITUDE: generateApiKeyAuthSetting(key=X_LONGITUDE, value=body_dict.get('additionalInfo', {}).get('longitude', '')),
                CHANNEL_ID: generateApiKeyAuthSetting(key=CHANNEL_ID, value='95221')
            }
        elif scenario == "balance_inquiry":
            external_id = str(uuid.uuid4())
            body_dict: dict = json.loads(body)
            return {
                AUTHORIZATION_CUSTOMER: generateApiKeyAuthSetting(key=AUTHORIZATION_CUSTOMER, value=f"Bearer {body_dict.get('additionalInfo', {}).get('accessToken', '')}"),
                X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
                X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
                X_EXTERNALID: generateApiKeyAuthSetting(key=X_EXTERNALID, value=external_id),
                X_DEVICE_ID: generateApiKeyAuthSetting(key=X_DEVICE_ID, value=body_dict.get('additionalInfo', {}).get('deviceId', '')),
                CHANNEL_ID: generateApiKeyAuthSetting(key=CHANNEL_ID, value='95221')
            }
        else:
            external_id = str(uuid.uuid4())
            return {
                X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
                X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
                X_EXTERNALID: generateApiKeyAuthSetting(key=X_EXTERNALID, value=external_id),
                CHANNEL_ID: generateApiKeyAuthSetting(key=CHANNEL_ID, value='95221')
            }
