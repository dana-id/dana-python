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
import re
from playwright.async_api import async_playwright
from urllib.parse import urlparse, parse_qs, unquote
import json

# Configuration
PIN = '181818'
DEFAULT_PHONE_NUMBER = '083811223355'


def extract_mobile_from_url(url):
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        seamless_data = params.get('seamlessData', [None])[0]
        if seamless_data:
            decoded = unquote(seamless_data)
            json_data = json.loads(decoded)
            return json_data.get('mobile', DEFAULT_PHONE_NUMBER)
    except Exception as e:
        print(f'Error extracting mobile number: {e}')
    return DEFAULT_PHONE_NUMBER


def normalize_mobile_number(mobile):
    """Strip non-digits; if starts with 62 convert to 0-prefixed local form."""
    digits = re.sub(r'\D', '', mobile)
    if not digits:
        return DEFAULT_PHONE_NUMBER
    if digits.startswith('62'):
        return '0' + digits[2:]
    return digits


async def automate_oauth(oauth_url, phone_number=None, pin=None, show_log=False):
    """
    Automates the OAuth login flow using Playwright.
    Matches the logic in the Go widget_oauth_automation.go implementation.
    """
    def log(msg):
        if show_log:
            print(msg)

    raw_phone = phone_number or extract_mobile_from_url(oauth_url)
    mobile_number = normalize_mobile_number(raw_phone)
    used_pin = pin or PIN

    log(f'Starting OAuth automation with phone: {mobile_number}')

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            '--disable-web-security',
            '--disable-features=IsolateOrigins',
            '--disable-site-isolation-trials',
            '--disable-blink-features=AutomationControlled',
            '--no-sandbox',
            '--disable-dev-shm-usage',
        ])

        context = await browser.new_context(
            **p.devices['iPhone 13'],
            locale='id-ID',
            geolocation={'longitude': 106.8456, 'latitude': -6.2088},
            permissions=['geolocation']
        )
        context.set_default_timeout(60000)
        page = await context.new_page()

        # When DANA navigates to a link.dana.id deep link the browser commits to
        # chrome-error://. DANA's JS is then gone and can never fall back to ipgLogin.
        # Going back immediately restores the inputphone page so DANA's fallback
        # timer (~15 s) can complete and route to ipgLogin where the PIN field appears.
        async def on_frame_navigated(frame):
            if frame == page.main_frame and frame.url.startswith('chrome-error://'):
                log('Detected chrome-error (link.dana.id deep-link failure) — going back to restore DANA page')
                await asyncio.sleep(0.3)
                try:
                    await page.go_back(wait_until='domcontentloaded', timeout=8000)
                    log('Successfully restored page after chrome-error')
                except Exception as e:
                    log(f'GoBack from chrome-error failed: {e}')

        page.on('framenavigated', on_frame_navigated)

        await page.goto(oauth_url, wait_until='domcontentloaded', timeout=60000)
        log('Page loaded, waiting for scripts to initialize...')
        await page.wait_for_timeout(2000)

        pin_selector = '.txt-input-pin-field, input[maxlength="6"][inputmode="numeric"], input[type="password"]'

        # Check if seamlessData caused DANA to auto-navigate past the phone page
        is_pin_visible = await page.locator(pin_selector).first.is_visible()

        if not is_pin_visible:
            # DANA pre-fills the phone field from seamlessData. Calling fill() clears+rewrites
            # the field which disrupts React state and causes seamlessSign validation to fail,
            # leading to a redirect to setting-more. Only fill if the field is actually empty.
            phone_selectors = [
                'input.txt-input-phone-number-field',
                "input[type='tel']",
                "input[placeholder='12312345678']",
                "input[maxlength='13']",
                "input[maxlength='15']",
            ]
            phone_filled = False
            for sel in phone_selectors:
                loc = page.locator(sel).first
                if await loc.is_visible():
                    current_val = await loc.input_value()
                    if current_val:
                        log(f'Phone field already pre-filled by DANA: {current_val} (skipping fill)')
                        phone_filled = True
                    else:
                        try:
                            await loc.fill(mobile_number)
                            log(f'Phone filled using selector: {sel} with value: {mobile_number}')
                            phone_filled = True
                        except Exception as e:
                            log(f'Error filling {sel}: {e}')
                    break

            if not phone_filled:
                # Fallback: click label and type via keyboard (only if field is empty)
                label = page.locator('label.new-clearable-input.form-ipg-phonenumber').first
                if await label.is_visible():
                    try:
                        await label.click()
                        await page.keyboard.type(mobile_number)
                        log('Phone filled via label click + keyboard type')
                        phone_filled = True
                    except Exception as e:
                        log(f'Error with label fallback: {e}')

            if not phone_filled:
                log('Warning: could not determine phone field state')

            # Wait for input to register in React state
            await page.wait_for_timeout(1000)

            # Click LANJUTKAN — try by role+name first (most specific), then CSS selectors
            submitted = False
            for text in ['LANJUTKAN', 'Lanjutkan', 'Next', 'Continue']:
                loc = page.get_by_role('button', name=text, exact=True).first
                if await loc.is_visible():
                    try:
                        await loc.click()
                        log(f'Submit clicked via role+name: {text}')
                        submitted = True
                        break
                    except Exception:
                        pass

            if not submitted:
                for sel in ["button[type='submit']", 'button.btn-primary', 'button.next-button', '.btn-continue', '.btn-submit']:
                    loc = page.locator(sel).first
                    if await loc.is_visible():
                        try:
                            await loc.click()
                            log(f'Submit clicked via selector: {sel}')
                            submitted = True
                            break
                        except Exception:
                            pass

            if not submitted:
                log('Warning: could not click LANJUTKAN button')

            # Wait for page to settle after submit
            await page.wait_for_timeout(3000)

            # Click continue button if shown on intermediate consent screen
            continue_loc = page.locator('button.btn-continue.fs-unmask.btn.btn-primary').first
            if await continue_loc.is_visible():
                await continue_loc.click()
                await page.wait_for_timeout(1000)

            # Wait for PIN field to appear (15 s)
            try:
                await page.wait_for_selector(pin_selector, state='attached', timeout=15000)
            except Exception:
                log('Timeout waiting for PIN field after phone submit')

        # Enter PIN using native Playwright keyboard input
        pin_filled = False
        pin_loc = page.locator(pin_selector).first
        if await pin_loc.is_visible():
            try:
                await pin_loc.click()
                await page.keyboard.type(used_pin)
                log('PIN entered via keyboard type')
                pin_filled = True
            except Exception as e:
                log(f'Error entering PIN via click+type: {e}')

        if not pin_filled:
            try:
                el = await page.wait_for_selector(pin_selector, state='visible', timeout=10000)
                await el.click()
                await page.keyboard.type(used_pin)
                log('PIN entered via wait_for_selector + keyboard type')
                pin_filled = True
            except Exception as e:
                log(f'Error entering PIN via wait_for_selector: {e}')

        if not pin_filled:
            log('Warning: could not enter PIN — PIN field not visible')
            await browser.close()
            return None

        # Listen for redirect URL containing the authorization code (30 s timeout)
        auth_code = None
        navigation_event = asyncio.Event()

        def extract_auth_code_from_url(url):
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            return params.get('authCode', [None])[0]

        async def on_redirect_navigated(frame):
            nonlocal auth_code
            if frame == page.main_frame:
                code = extract_auth_code_from_url(frame.url)
                if code:
                    auth_code = code
                    log(f'Auth code found in redirect URL: {auth_code}')
                    navigation_event.set()

        page.on('framenavigated', on_redirect_navigated)

        # Check immediately in case PIN submit already redirected
        code = extract_auth_code_from_url(page.url)
        if code:
            auth_code = code
            navigation_event.set()

        try:
            await asyncio.wait_for(navigation_event.wait(), timeout=30)
        except asyncio.TimeoutError:
            log('Timeout waiting for redirect')

        if not auth_code:
            auth_code = extract_auth_code_from_url(page.url)

        await browser.close()
        log('Browser closed')

    if auth_code:
        log(f'OAuth flow completed successfully, auth code: {auth_code}')
    else:
        log('Could not capture authorization code')

    return auth_code


def get_auth_code(oauth_url, phone_number=None, pin=None):
    """
    Wrapper function to get an authorization code synchronously.
    This is the main entry point for other test files to use.
    """
    try:
        return asyncio.run(automate_oauth(oauth_url=oauth_url, phone_number=phone_number, pin=pin, show_log=True))
    except Exception as e:
        print(f'Error during OAuth automation: {e}')
        return None


if __name__ == '__main__':
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else None
    code = get_auth_code(url)
    print(f'Auth code: {code}')
