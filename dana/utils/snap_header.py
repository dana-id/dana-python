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
from hashlib import sha256
import uuid
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

        elif scenario == "apply_ott":
            return list(set(filtered_auth).union(SnapHeader.SnapApplyOTTRuntimeHeaders))
        
        else:
            return list(set(filtered_auth).union(SnapHeader.SnapRuntimeHeaders))

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
        
        def get_usable_private_key(private_key: str, private_key_path: str) -> str:

            if private_key_path:
                with open(private_key_path, 'rb') as pem_in:
                    pemlines = pem_in.read()
                    private_key = load_pem_private_key(pemlines, None, default_backend())
                    return private_key
            elif private_key:
                private_key = private_key.replace("\\n", "\n")
                return private_key
            else:
                raise ValueError("Provide one of private_key or private_key_path")

        private_key = get_usable_private_key(private_key=private_key,
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
        elif scenario == "apply_ott":
            external_id = str(uuid.uuid4())
            body_dict: dict = json.loads(body)
            return {
                X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
                X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
                X_EXTERNALID: generateApiKeyAuthSetting(key=X_EXTERNALID, value=external_id),
                X_IP_ADDRESS: generateApiKeyAuthSetting(key=X_IP_ADDRESS, value=body_dict.get('end_user_ip_address', '')),
                X_DEVICE_ID: generateApiKeyAuthSetting(key=X_DEVICE_ID, value=body_dict.get('device_id', '')),
                X_LATITUDE: generateApiKeyAuthSetting(key=X_LATITUDE, value=body_dict.get('latitude', '')),
                X_LONGITUDE: generateApiKeyAuthSetting(key=X_LONGITUDE, value=body_dict.get('longitude', '')),
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
