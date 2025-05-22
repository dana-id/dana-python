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
from urllib import parse

def encode(dict: dict) -> str:
    return parse.quote(json.dumps(dict, separators=(',', ':')))

def sign(dict: dict, private_key: str) -> str:
    """
    Signs a dictionary with SHA256withRSA, Base64 encodes the signature, and URL encodes the result.
    
    Args:
        dict: The dictionary to be signed
        private_key: The private key in PEM format for signing
    
    Returns:
        URL-encoded Base64 string of the signature
    """
    import base64
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend
    
    # Convert the dictionary to a JSON string
    json_str = json.dumps(dict, separators=(',', ':'))
    
    # Load the private key
    key = serialization.load_pem_private_key(
        private_key.encode('utf-8'),
        password=None,
        backend=default_backend()
    )
    
    # Sign the data with SHA256withRSA
    signature = key.sign(
        json_str.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    # Base64 encode the signature
    base64_encoded = base64.b64encode(signature).decode('utf-8')
    
    # URL encode the Base64 encoded string
    url_encoded = parse.quote(base64_encoded)
    
    return url_encoded