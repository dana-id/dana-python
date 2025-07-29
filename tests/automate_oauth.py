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

import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse, parse_qs, unquote
import json

# Configuration
PIN = '123321'  # Replace with your test PIN
oauth_url = 'https://m.sandbox.dana.id/n/ipg/oauth?partnerId=2025021714245533502768&scopes=CASHIER,AGREEMENT_PAY,QUERY_BALANCE,DEFAULT_BASIC_PROFILE,MINI_DANA&externalId=b3b7e164-a295-4461-8475-8db546f0d509&state=02c92610-aa7c-42b0-bf26-23bb06e4d475&channelId=2025021714245533502768&redirectUrl=https://google.com&timestamp=2025-05-20T22:27:01+00:00&seamlessData=%7B%22mobile%22%3A%220811742234%22%7D&seamlessSign=IN8MCZZMge6C0SOQG4otmP9WE5yTll0%2F6OwgmUV0cfFi1e9Hj8PAWuD1ZanQ9MZcrKH1nwJEKnYTtqtQ3AdpLa24E%2B2W3%2BNJD8nh7FLicjPFQuDEIAdE%2ByEqTfpU5Z8%2B1tdB%2BW3HN4p6ko%2BiSXu28XHZOnxxXbfMZzQ0qwpwhTp76xSi2tH5eU7ksp37G9sjCB3eyFXBR8bWr7NCjDzFL5cxVlTuEZCmLieDLYh%2FiGClPfWj%2F7tnzzppyiPJsG7PjWkuM25%2B%2BwHBcb7DUA1yVllq30lxUpKeogZ3AuY%2Be9%2FeRHrhz6d%2BBFnzowI3Fk2ZA64BR9E8TSpNHyzWKCNc1A%3D%3D&isSnapBI=true'

def extract_mobile_from_url(url):
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        seamless_data = params.get('seamlessData', [None])[0]
        if seamless_data:
            decoded = unquote(seamless_data)
            json_data = json.loads(decoded)
            return json_data.get('mobile', '0811742234')
    except Exception as e:
        print(f'Error extracting mobile number: {e}')
    return '0811742234'

async def automate_oauth(phone_number=None, pin=None, show_log=False):
    """
    Automates the OAuth login flow using Playwright in a headless browser, simulating a mobile device.
    This function navigates to the OAuth URL, enters the provided or extracted phone number, submits it,
    waits for the PIN input screen, enters the provided or default PIN, and attempts to extract the
    authorization code from the redirect URL or page content.
    Args:
        phone_number (str, optional): The phone number to use for login. If not provided, attempts to extract from the OAuth URL.
        pin (str, optional): The PIN code to use for authentication. If not provided, uses the default PIN.
        show_log (bool, optional): If True, prints detailed log messages during the automation process.
    Returns:
        str or None: The extracted authorization code if found, otherwise None.
    Notes:
        - Requires Playwright and asyncio.
        - Simulates an iPhone 12 device with Indonesian locale and Jakarta geolocation.
        - Handles various input field and button selectors to maximize compatibility with different OAuth UIs.
        - Waits for redirects and listens for URL changes to capture the authorization code.
        - Closes the browser context after completion.
    """
    def log(msg):
        if show_log:
            print(msg)
    log('Starting OAuth automation...')
    # Use provided phone_number or extract from URL or fallback
    mobile_number = phone_number or extract_mobile_from_url(oauth_url)
    log(f'Extracted mobile number from URL or param: {mobile_number}')
    used_pin = pin or PIN
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=0, args=[
            '--disable-web-security',
            '--disable-features=IsolateOrigins',
            '--disable-site-isolation-trials',
            '--disable-features=BlockInsecurePrivateNetworkRequests',
            '--disable-blink-features=AutomationControlled',
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
        ])
        context = await browser.new_context(
            **p.devices['iPhone 12'],
            locale='id-ID',
            geolocation={'longitude': 106.8456, 'latitude': -6.2088},
            permissions=['geolocation']
        )
        page = await context.new_page()
        # Only print browser console messages that are not warnings
        def handle_console(msg):
            if msg.type != 'warning' and show_log:
                print(f'Browser console: {msg.text}')
        page.on('console', handle_console)
        page.on('pageerror', lambda err: log(f'Browser page error: {err.message}'))
        log('Opening OAuth URL...')
        await page.goto(oauth_url, wait_until='domcontentloaded', timeout=60000)
        log('Page loaded, waiting for scripts to initialize...')
        # Reduce wait time for initialization
        await page.wait_for_timeout(1000)
        log('Done waiting for initialization')
        log('Trying to find the phone input field...')
        await page.evaluate("""
        (mobile) => {
            const inputs = document.querySelectorAll('input');
            for (const input of inputs) {
                if (input.type === 'tel' || 
                    input.placeholder === '12312345678' || 
                    input.maxLength === 13 ||
                    input.className.includes('phone-number')) {
                    input.value = mobile;
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    return true;
                }
            }
            return false;
        }
        """, mobile_number)
        log('Looking for the submit button...')
        await page.evaluate("""
        () => {
            const buttons = document.querySelectorAll('button');
            for (const button of buttons) {
                if (button.type === 'submit' || 
                    button.innerText.includes('Next') || 
                    button.innerText.includes('Continue') ||
                    button.innerText.includes('Submit') ||
                    button.innerText.includes('Lanjutkan')) {
                    button.click();
                    return true;
                }
            }
            return false;
        }
        """)
        log('Waiting for PIN input screen...')
        # Use selector-based wait for PIN input instead of fixed timeout
        try:
            await page.wait_for_selector('.txt-input-pin-field, input[maxlength="6"], input[type="password"]', timeout=3000)
        except Exception:
            pass
        need_to_continue = await page.evaluate("""
        () => {
            const continueBtn = document.querySelector('button.btn-continue.fs-unmask.btn.btn-primary');
            if (continueBtn) {
                continueBtn.click();
                return true;
            }
            return false;
        }
        """)
        if need_to_continue:
            log('Clicked another continue button - waiting for PIN input to appear')
            await page.wait_for_timeout(500)
        success = await page.evaluate("""
        (pinCode) => {
            const specificPinInput = document.querySelector('.txt-input-pin-field');
            if (specificPinInput) {
                specificPinInput.value = pinCode;
                specificPinInput.dispatchEvent(new Event('input', { bubbles: true }));
                specificPinInput.dispatchEvent(new Event('change', { bubbles: true }));
                return true;
            }
            const inputs = document.querySelectorAll('input');
            const singlePinInput = Array.from(inputs).find(input => 
                input.maxLength === 6 && 
                (input.type === 'text' || input.type === 'tel' || input.type === 'number' || input.inputMode === 'numeric')
            );
            if (singlePinInput) {
                singlePinInput.value = pinCode;
                singlePinInput.dispatchEvent(new Event('input', { bubbles: true }));
                singlePinInput.dispatchEvent(new Event('change', { bubbles: true }));
                return true;
            }
            const pinInputs = Array.from(inputs).filter(input => 
                input.maxLength === 1 || 
                input.type === 'password' || 
                input.className.includes('pin')
            );
            if (pinInputs.length >= pinCode.length) {
                for (let i = 0; i < pinCode.length; i++) {
                    pinInputs[i].value = pinCode.charAt(i);
                    pinInputs[i].dispatchEvent(new Event('input', { bubbles: true }));
                    pinInputs[i].dispatchEvent(new Event('change', { bubbles: true }));
                }
                return true;
            }
            return false;
        }
        """, used_pin)
        if success:
            log('Successfully entered PIN via JavaScript')
        else:
            log('Failed to enter PIN, no suitable input field found')
        async def try_to_find_and_click_confirm_button():
            try:
                button_clicked = await page.evaluate("""
                () => {
                    const allButtons = document.querySelectorAll('button');
                    let continueButton = null;
                    let backButton = null;
                    allButtons.forEach((button) => {
                        const buttonText = button.innerText.trim().toLowerCase();
                        if (buttonText.includes('lanjut') || 
                            buttonText.includes('continue') || 
                            buttonText.includes('submit') || 
                            buttonText.includes('confirm') || 
                            buttonText.includes('next') ||
                            button.className.includes('btn-continue') ||
                            button.className.includes('btn-submit') ||
                            button.className.includes('btn-confirm')) {
                            continueButton = button;
                        }
                        if (buttonText.includes('kembali') || 
                            buttonText.includes('back') || 
                            button.className.includes('btn-back')) {
                            backButton = button;
                        }
                    });
                    if (continueButton) {
                        continueButton.click();
                        return true;
                    }
                    return false;
                }
                """)
                if button_clicked:
                    await page.wait_for_timeout(500)
                    return True
            except Exception as e:
                if show_log:
                    print(f'Error with PIN confirm button: {e}')
            return False
        button_clicked = await try_to_find_and_click_confirm_button()
        if button_clicked:
            log('Confirm button was clicked, waiting for action to complete...')
            await page.wait_for_timeout(500)
        log('Watching for redirects and URL changes...')
        auth_code = None
        navigation_event = asyncio.Event()
        
        def extract_auth_code_from_url(url):
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            return params.get('auth_code', [None])[0]

        async def check_url_for_auth_code():
            nonlocal auth_code
            url = page.url
            code = extract_auth_code_from_url(url)
            if code:
                auth_code = code
                log(f'\n✅ SUCCESS! Auth code found in current URL: {auth_code}')
                navigation_event.set()

        async def on_frame_navigated(frame):
            nonlocal auth_code
            if frame == page.main_frame:
                url = frame.url
                code = extract_auth_code_from_url(url)
                if code:
                    auth_code = code
                    log(f'\n✅ SUCCESS! Auth code found in redirect URL: {auth_code}')
                    navigation_event.set()

        page.on('framenavigated', on_frame_navigated)
        page.on('load', lambda _: asyncio.create_task(check_url_for_auth_code()))

        # Also check immediately after actions
        await check_url_for_auth_code()
        try:
            await asyncio.wait_for(navigation_event.wait(), timeout=15)
        except asyncio.TimeoutError:
            log('\n⚠️ Timeout waiting for redirect')
        if not auth_code:
            content = await page.content()
            import re
            match = re.search(r'auth[_-]?code["\'>: ]+([a-zA-Z0-9_-]+)', content, re.IGNORECASE)
            if match:
                auth_code = match.group(1)
                log(f'Found auth code reference in page content: {auth_code}')
        await browser.close()
        log('Browser closed')
    return auth_code

def get_auth_code(phone_number=None, pin=None):
    """
    Wrapper function to get an authorization code synchronously.
    This is the main entry point for other test files to use.
    
    Args:
        phone_number (str, optional): Phone number to use for login
        pin (str, optional): PIN code to use for authentication
        
    Returns:
        str or None: Authorization code if found, None otherwise
    """    
    # If no override, use the automation
    try:
        return asyncio.run(automate_oauth(phone_number=phone_number, pin=pin, show_log=True))
    except Exception as e:
        print(f"Error during OAuth automation: {e}")
        return None

if __name__ == '__main__':
    code = get_auth_code()
    print(f'Auth code: {code}')
