from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
import base64
from hashlib import sha256
import uuid
from typing import Any, List, Mapping
from datetime import datetime, timedelta, timezone

from dana_python.utils.snap_configuration import APIKeyAuthSetting

X_TIMESTAMP = "X-TIMESTAMP"
X_SIGNATURE = "X-SIGNATURE"
X_EXTERNALID = "X-EXTERNAL-ID"

class SnapHeader:
    SnapRuntimeHeaders: List[str] = [X_TIMESTAMP, X_SIGNATURE, X_EXTERNALID]

    @staticmethod
    def merge_with_snap_runtime_headers(auth_from_users: List[str]) -> List[str]:
        """
        Remove any items containing 'private' or 'env' and merge with Snap runtime headers.
        """
        filtered_auth = [
            auth for auth in auth_from_users
            if 'private' not in auth.lower() and 'env' not in auth.lower()
        ]

        return list(set(filtered_auth).union(SnapHeader.SnapRuntimeHeaders))


    @staticmethod
    def get_snap_generated_auth(
        method: str,
        resource_path: str, 
        body: str, 
        private_key: str = None, 
        private_key_path: str = None,
    ) -> Mapping[str, APIKeyAuthSetting]:
        
        def generateApiKeyAuthSetting(key: str, value: Any) -> APIKeyAuthSetting:
            return {
                'in': 'header',
                'key': key,
                'type': 'api_key',
                'value': value
            }
        
        def get_usable_private_key(private_key: str, private_key_path: str) -> str:

            if private_key and private_key_path:
                raise ValueError("Provide one of private_key or private_key_path, not both")
            elif private_key:
                private_key = private_key.replace("\\n", "\n")
                return private_key
            elif private_key_path:
                with open(private_key_path, 'rb') as pem_in:
                    pemlines = pem_in.read()
                    private_key = load_pem_private_key(pemlines, None, default_backend())
                    return private_key
            else:
                raise ValueError("Provide on of private_key or private_key_path")
        
        if not isinstance(body, str):
            body = str(body)

        private_key = get_usable_private_key(private_key=private_key,
                                             private_key_path=private_key_path)

        jakarta_time = datetime.now(timezone.utc) + timedelta(hours=7)
        timestamp = jakarta_time.strftime('%Y-%m-%dT%H:%M:%S+07:00')

        hashed_payload = sha256(body.encode('utf-8')).hexdigest()

        data = f'{method}:{resource_path}:{hashed_payload}:{timestamp}'
        
        private_key_obj = serialization.load_pem_private_key(
            private_key.encode(),
            password=None,
        )

        signature = private_key_obj.sign(
            data.encode('utf-8'),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        encoded_signature = base64.b64encode(signature).decode()

        external_id = str(uuid.uuid4())

        return {
            X_TIMESTAMP: generateApiKeyAuthSetting(key=X_TIMESTAMP, value=timestamp),
            X_SIGNATURE: generateApiKeyAuthSetting(key=X_SIGNATURE, value=encoded_signature),
            X_EXTERNALID: generateApiKeyAuthSetting(key=X_EXTERNALID, value=external_id),
        }
