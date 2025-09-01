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

import os
import uuid
import json
import base64
import hashlib
import urllib.parse
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, List, Union
from dana.widget.v1.models import WidgetPaymentResponse, ApplyOTTResponse
from dana.utils.snap_header import SnapHeader

# For cryptography operations
try:
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.serialization import load_pem_private_key
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

# Import enum values - assuming these are defined in the generated code
try:
    from dana.widget.v1.enum import Mode, TerminalType
except ImportError:
    # If enums aren't available, define Mode as a simple class
    class Mode:
        API = "API"
        DEEPLINK = "DEEPLINK"
    
    class TerminalType:
        WEB = "WEB"


class Util:
    """
    Utility class for the Dana Widget API.
    """
    

    
    @staticmethod
    def generate_oauth_url(data, private_key: Optional[str] = None, private_key_path: Optional[str] = None) -> str:
        """
        Generate OAuth URL for testing
        
        Args:
            data: OAuth URL data object
            private_key: Optional private key content
            private_key_path: Optional path to private key file
            
        Returns:
            str: The generated OAuth URL
        """
        # Use environment variable or default to sandbox
        env = os.environ.get('DANA_ENV') or os.environ.get('ENV') or 'sandbox'
        
        # Get mode or default to API
        mode = getattr(data, 'mode', None) or Mode.API
        
        # Set base URL based on environment and mode
        if mode == Mode.DEEPLINK:
            base_url = 'https://m.sandbox.dana.id/n/link/binding' if env == 'sandbox' else 'https://link.dana.id/bindSnap'
        elif mode == Mode.API:
            base_url = 'https://m.sandbox.dana.id/n/ipg/oauth' if env == 'sandbox' else 'https://m.dana.id/n/ipg/oauth'
        
        # Get partner ID from environment
        partner_id = os.environ.get('X_PARTNER_ID')
        if not partner_id:
            raise RuntimeError('X_PARTNER_ID is not defined')
        
        # Use provided state or generate a new UUID
        state = getattr(data, 'state', None)
        if not state:
            state = str(uuid.uuid4())
        
        # Generate channel ID
        channel_id = os.environ.get('X_PARTNER_ID')
        
        # Get scopes based on environment
        if hasattr(data, 'scopes') and data.scopes:
            scopes = data.scopes
        else:
            if env.lower() != 'production':
                scopes = 'CASHIER,AGREEMENT_PAY,QUERY_BALANCE,DEFAULT_BASIC_PROFILE,MINI_DANA'
            else:
                scopes = 'CASHIER'
        
        # Use provided external ID or generate a UUID
        external_id = getattr(data, 'external_id', None)
        if not external_id:
            external_id = str(uuid.uuid4())
            
        # Get merchant ID
        merchant_id = getattr(data, 'merchant_id', None)
        
        # Generate timestamp in Jakarta time (UTC+7) with RFC3339 format
        try:
            # Python's timezone handling is different from PHP
            now = datetime.now(timezone(timedelta(hours=7)))
            timestamp = now.strftime('%Y-%m-%dT%H:%M:%S%z')
            # Format timezone correctly with a colon
            timestamp = timestamp[:-2] + ':' + timestamp[-2:]
        except Exception:
            # Fallback if timezone calculation fails
            now = datetime.now(timezone.utc)
            now += timedelta(hours=7)  # Add 7 hours for UTC+7
            timestamp = now.strftime('%Y-%m-%dT%H:%M:%S+07:00')
        
        # Build URL with required parameters
        if mode == Mode.DEEPLINK:
            request_id = str(uuid.uuid4())
            url_params = {
                'partnerId': partner_id,
                'scopes': scopes,
                'terminalType': TerminalType.WEB,
                'externalId': external_id,
                'requestId': request_id,
                'redirectUrl': data.redirect_url if hasattr(data, 'redirect_url') else None,
                'state': state,
            }
        elif mode == Mode.API:
            url_params = {
                'partnerId': partner_id,
                'scopes': scopes,
                'externalId': external_id,
                'channelId': channel_id,
                'redirectUrl': data.redirect_url if hasattr(data, 'redirect_url') else None,
                'timestamp': timestamp,
                'state': state,
                'isSnapBI': 'true'
            }
        
        # Add merchant ID if provided
        if merchant_id and mode == Mode.API:
            url_params['merchantId'] = merchant_id
        
        # Add subMerchantId if provided
        if hasattr(data, 'sub_merchant_id') and data.sub_merchant_id and mode == Mode.API:
            url_params['subMerchantId'] = data.sub_merchant_id
        
        # Add lang if provided
        if hasattr(data, 'lang') and data.lang and mode == Mode.API:
            url_params['lang'] = data.lang
        
        # Add allowRegistration if provided
        if hasattr(data, 'allow_registration') and data.allow_registration is not None and mode == Mode.API:
            url_params['allowRegistration'] = 'true' if data.allow_registration else 'false'
        
        # Handle seamless data if provided
        seamless_data = getattr(data, 'seamless_data', None)
        if seamless_data:
            # Convert object to dict if necessary
            if not isinstance(seamless_data, dict):
                try:
                    seamless_data = vars(seamless_data)
                except TypeError:
                    seamless_data = json.loads(json.dumps(seamless_data))
            
            # Ensure seamless_data is a dict and convert mobileNumber to mobile if needed
            if isinstance(seamless_data, dict):
                if 'mobileNumber' in seamless_data:
                    seamless_data['mobile'] = seamless_data['mobileNumber']
                    del seamless_data['mobileNumber']
                
                if mode == Mode.DEEPLINK:
                    seamless_data['externalUid'] = getattr(data, 'external_id', '')
                    seamless_data['reqTime'] = timestamp
                    seamless_data['verifiedTime'] = "0"
                    seamless_data['reqMsgId'] = request_id
                
                seamless_data_json = json.dumps(seamless_data)
                url_params['seamlessData'] = seamless_data_json
                
                url_params['seamlessSign'] = Util.generate_seamless_sign(seamless_data, private_key, private_key_path)
        
        # Remove None values
        url_params = {k: v for k, v in url_params.items() if v is not None}
        
        # Build the final URL
        return base_url + '?' + urllib.parse.urlencode(url_params)
    
    @staticmethod
    def generate_seamless_sign(seamless_data: Dict[str, Any], private_key: Optional[str] = None, private_key_path: Optional[str] = None) -> str:
        """
        Generate seamless sign for OAuth URL
        
        Args:
            seamless_data: The seamless data to sign
            private_key: Optional private key content
            private_key_path: Optional path to private key file
            
        Returns:
            str: The generated signature
        """
        try:
            # Get properly formatted private key using SnapHeader utility method
            usable_private_key = SnapHeader.get_usable_private_key(private_key, private_key_path)
            data_to_sign = json.dumps(seamless_data).encode()
            
            # Use cryptography library if available
            if CRYPTOGRAPHY_AVAILABLE:
                # Load the private key
                key = load_pem_private_key(usable_private_key.encode(), password=None)
                
                # Sign the data
                signature = key.sign(
                    data_to_sign,
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )
                
                # Return base64 encoded signature
                return base64.b64encode(signature).decode()
            else:
                # Fallback to a simple hash for testing
                return hashlib.sha256(data_to_sign + str(int(datetime.now().timestamp())).encode()).hexdigest()
                
        except Exception as e:
            # For testing purposes, generate a mock signature if key is not available
            return hashlib.sha256((json.dumps(seamless_data) + str(int(datetime.now().timestamp()))).encode()).hexdigest()
    
    @staticmethod
    def generate_complete_payment_url(widget_payment_response: WidgetPaymentResponse = None, apply_ott_response: ApplyOTTResponse = None) -> str:
        """
        Combines the webRedirectUrl from WidgetPaymentResponse with the OTT token from ApplyOTTResponse
        
        Args:
            widget_payment_response: The widget payment response
            apply_ott_response: The apply OTT response
            
        Returns:
            str: The generated payment URL or empty string if inputs are invalid
        """
        if widget_payment_response is None or apply_ott_response is None:
            return ''
        
        web_redirect_url = getattr(widget_payment_response, 'web_redirect_url', None)
        if not web_redirect_url:
            return ''
        
        user_resources = getattr(apply_ott_response, 'user_resources', None)
        if not user_resources or len(user_resources) == 0:
            return web_redirect_url
        
        ott_value = getattr(user_resources[0], 'value', None) if user_resources else None
        if not ott_value:
            return web_redirect_url
        
        return web_redirect_url + '&ott=' + ott_value
