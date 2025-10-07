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
PIN = '131000'  # Replace with your test PIN

def extract_mobile_from_url(url):
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        seamless_data = params.get('seamlessData', [None])[0]
        if seamless_data:
            decoded = unquote(seamless_data)
            json_data = json.loads(decoded)
            return json_data.get('mobile', '087875849373')
    except Exception as e:
        print(f'Error extracting mobile number: {e}')
    return '087875849373'

async def automate_oauth(oauth_url, phone_number=None, pin=None, show_log=False):
    """
    Automates the OAuth login flow using Playwright in a headless browser, simulating a mobile device.
    This function navigates to the OAuth URL, enters the provided or extracted phone number, submits it,
    waits for the PIN input screen, enters the provided or default PIN, and attempts to extract the
    authorization code from the redirect URL or page content.
    Args:
        oauth_url (str): The OAuth URL to navigate to.
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
        
        # First try the specific selector used in PHP implementation
        phone_entered = False
        try:
            log('Trying to find label.new-clearable-input.form-ipg-phonenumber...')
            phone_label = await page.query_selector('label.new-clearable-input.form-ipg-phonenumber')
            if phone_label:
                log('Phone label found, clicking it...')
                await phone_label.click()
                await page.keyboard.type(mobile_number)
                log(f'Phone number {mobile_number} entered via label.new-clearable-input.form-ipg-phonenumber click')
                phone_entered = True
            else:
                log('Phone label not found, trying alternative methods')
        except Exception as e:
            log(f'Error during specific phone selector handling: {str(e)}')

        # Fall back to the generic approach if the specific selector didn't work
        if not phone_entered:
            log('Using general input detection as fallback')
            log('Looking for phone input field...')
            result = await page.evaluate("""
            (mobile) => {
                // Try the generic approach matching PHP implementation exactly
                const inputs = document.querySelectorAll('input');
                for (const input of Array.from(inputs)) {
                    if (input.type === 'tel' || 
                        input.placeholder === '12312345678' || 
                        input.maxLength === 13 ||
                        input.className.includes('phone-number')) {
                        input.value = mobile;
                        input.dispatchEvent(new Event('input', { bubbles: true }));
                        return { filled: true, message: 'Found and filled mobile number input' };
                    }
                }
                return { filled: false, message: 'No suitable mobile number input found' };
            }
            """, mobile_number)
            
            # Process result with error handling like in PHP
            if result and result.get('filled', False):
                log(f"Phone input filled: {result.get('message')}")
            else:
                log(f"Warning: {result.get('message', 'Unknown error')}")
                
            # If JS approach failed, try clicking on input with type=tel as a fallback
            if not result or not result.get('filled', False):
                log('Trying alternative approach - clicking on tel input directly')
                try:
                    tel_input = await page.query_selector('input[type="tel"]')
                    if tel_input:
                        await tel_input.click()
                        await page.keyboard.type(mobile_number)
                        log('Mobile number entered via direct tel input click')
                except Exception as e:
                    log(f'Error with fallback approach: {str(e)}')
            

        # Wait a bit for the input to take effect
        await page.wait_for_timeout(1000)
        log('Looking for submit button...')
        submit_button_result = await page.evaluate("""
        () => {
            const buttons = document.querySelectorAll('button');
            for (const button of Array.from(buttons)) {
                if (button.type === 'submit' || 
                    button.innerText.includes('Next') || 
                    button.innerText.includes('Continue') ||
                    button.innerText.includes('Submit') ||
                    button.innerText.includes('Lanjutkan')) {
                    button.click();
                    return { clicked: true, message: 'Found and clicked button via JS evaluation' };
                }
            }
            return { clicked: false, message: 'No suitable submit button found' };
        }
        """)
        
        # Process result with error handling like in PHP
        if submit_button_result and submit_button_result.get('clicked', False):
            log(f"Submit button clicked: {submit_button_result.get('message')}")
        else:
            log(f"Warning: {submit_button_result.get('message', 'Unknown error')}")
            # Try alternative approach for finding buttons
            log('Trying alternative approach for finding submit button...')
            try:
                # Try to find any button that looks like a submit button
                for selector in ['button[type="submit"]', 'button.btn-primary', 'button.next-button', '.btn-continue', '.btn-submit']:
                    button = await page.query_selector(selector)
                    if button:
                        log(f'Found button with selector: {selector}')
                        await button.click()
                        log('Alternative button click successful')
                        break
            except Exception as e:
                log(f'Error with alternative button approach: {str(e)}')
        log('Waiting for PIN input screen...')
        # First wait for page to load completely
        try:
            await page.wait_for_load_state('networkidle')
            await page.wait_for_timeout(1000)  # Extra wait to ensure JS has executed
        except Exception as e:
            log(f"Error waiting for page to load: {e}")
            
        # Take a screenshot for debugging
        try:
            screenshot_path = Path('dana_oauth_before_pin_detection.png')
            await page.screenshot(path=str(screenshot_path))
            log(f"Before PIN detection screenshot saved to {screenshot_path}")
        except Exception as e:
            log(f"Failed to take screenshot: {str(e)}")
            
        # Attempt to log all inputs on the page for debugging
        try:
            input_details = await page.evaluate("""
            () => {
                const inputs = document.querySelectorAll('input');
                return Array.from(inputs).map(input => ({
                    id: input.id || 'no-id',
                    type: input.type,
                    maxLength: input.maxLength,
                    className: input.className,
                    placeholder: input.placeholder || 'no-placeholder'
                }));
            }
            """)
            log(f"DEBUG - Found {len(input_details)} input fields: {input_details}")
        except Exception as e:
            log(f"Error logging input fields: {e}")
            
        # If we need to click a continue button to get to PIN screen, do it now
        try:
            continue_clicked = await page.evaluate("""
            () => {
                const buttons = document.querySelectorAll('button');
                for (const button of buttons) {
                    const text = button.innerText.toLowerCase().trim();
                    if ((text.includes('continue') || text.includes('lanjut')) && 
                        (button.className.includes('btn-continue') || button.className.includes('btn-primary'))) {
                        console.log('Found continue button to click:', button.innerText);
                        button.click();
                        return true;
                    }
                }
                return false;
            }
            """)
            if continue_clicked:
                log('Clicked continue button to proceed to PIN screen')
                await page.wait_for_timeout(1000)  # Wait for PIN screen to appear
        except Exception as e:
            log(f"Error clicking continue button: {e}")
            
        # Sleep a bit before PIN input attempt to make sure page is stable
        await page.wait_for_timeout(2000)
        
        # Try to capture screenshot just before PIN input
        try:
            screenshot_path = Path('dana_oauth_pin_attempt.png')
            await page.screenshot(path=str(screenshot_path))
            log(f"PIN attempt screenshot saved to {screenshot_path}")
        except Exception as e:
            log(f"Failed to take screenshot: {str(e)}")
        
        # Log visible inputs in the console for debugging
        log('DEBUG - All input fields found:')
        try:
            input_log = await page.evaluate("""
            () => {
                const inputs = document.querySelectorAll('input');
                const details = [];
                for (let i = 0; i < inputs.length; i++) {
                    const input = inputs[i];
                    details.push({type: input.type, maxLength: input.maxLength, id: input.id, className: input.className});
                }
                return JSON.stringify(details);
            }
            """)
            log(f"Input fields: {input_log}")
        except Exception as e:
            log(f"Error getting input details: {e}")
        
        # Enter PIN using JavaScript exactly like PHP implementation - EXACT MATCH
        log('Looking for PIN input fields...')
        
        # Use the EXACT same JavaScript as PHP, with minimal changes for Python syntax
        # First try direct page.fill with a selector - can be more reliable than JS evaluation
        try:
            log("Trying direct Playwright fill first...")
            fill_result = False
            # Try specific PIN input selector
            try:
                await page.fill(".txt-input-pin-field", used_pin)
                log("Filled PIN directly with Playwright .txt-input-pin-field selector")
                fill_result = True
            except Exception as e:
                log(f"Could not fill .txt-input-pin-field: {e}")
                # Try maxlength=6 selector
                try:
                    await page.fill("input[maxLength='6']", used_pin)
                    log("Filled PIN directly with Playwright maxLength=6 selector")
                    fill_result = True
                except Exception as e:
                    log(f"Could not fill input[maxLength='6']: {e}")
        except Exception as e:
            log(f"Direct fill attempts failed: {e}")
            
        # Now try more aggressive JavaScript approach exactly like PHP
        pin_input_result = await page.evaluate("""
        (pin) => {
            // Helper function to trigger all possible events to ensure the value is registered
            function triggerAllEvents(element) {
                // Focus first
                element.focus();
                
                // Try both assignment methods
                element.value = pin;
                if (element.hasAttribute('value')) {
                    element.setAttribute('value', pin);
                }
                
                // Create events with proper properties for maximum compatibility
                const inputEvent = new Event('input', { bubbles: true, cancelable: true });
                const changeEvent = new Event('change', { bubbles: true, cancelable: true });
                const keyupEvent = new Event('keyup', { bubbles: true, cancelable: true });
                
                // Dispatch all events
                element.dispatchEvent(inputEvent);
                element.dispatchEvent(changeEvent);
                element.dispatchEvent(keyupEvent);
                
                // Blur at the end
                element.blur();
            }
            
            // First check for the specific PIN input field
            const specificPinInput = document.querySelector(".txt-input-pin-field");
            if (specificPinInput) {
                console.log("Found specific PIN input field: .txt-input-pin-field");
                triggerAllEvents(specificPinInput);
                
                // Verify the value was set
                console.log("PIN field value after set:", specificPinInput.value);
                return { success: true, method: "specific", message: "Found specific PIN input field: .txt-input-pin-field" };
            }
            
            const inputs = document.querySelectorAll("input");
            console.log("Total inputs found:", inputs.length);
            
            // Try for single PIN input with maxLength=6
            const singlePinInput = Array.from(inputs).find(input => 
                input.maxLength === 6 && 
                (input.type === "text" || input.type === "tel" || input.type === "number" || input.inputMode === "numeric")
            );
            
            if (singlePinInput) {
                console.log("Found single PIN input with maxLength=6:", singlePinInput.type);
                triggerAllEvents(singlePinInput);
                
                // Verify the value was set
                console.log("PIN field value after set:", singlePinInput.value);
                return { success: true, method: "single", message: "Found single PIN input field with maxLength=6" };
            }
            
            // Try multi-character PIN inputs
            const pinInputs = Array.from(inputs).filter(input => 
                input.maxLength === 1 || 
                input.type === "password" || 
                input.className.includes("pin")
            );
            
            console.log("Pin inputs found with criteria (maxLength=1, type=password, or class contains 'pin'):", pinInputs.length);
            
            if (pinInputs.length >= pin.length) {
                console.log("Using multiple PIN inputs");
                for (let i = 0; i < pin.length; i++) {
                    const input = pinInputs[i];
                    // Set value directly
                    input.value = pin.charAt(i);
                    if (input.hasAttribute('value')) {
                        input.setAttribute('value', pin.charAt(i));
                    }
                    
                    // Dispatch events
                    input.dispatchEvent(new Event("input", { bubbles: true }));
                    input.dispatchEvent(new Event("change", { bubbles: true }));
                }
                return { success: true, method: "multi", message: `Found ${pinInputs.length} PIN inputs via JS` };
            }
            
            // Last resort - try ANY input
            if (inputs.length > 0) {
                console.log("Last resort: trying any input field");
                const input = inputs[0];
                triggerAllEvents(input);
                return { success: true, method: "any", message: "Tried with first available input as last resort" };
            }
            
            console.log("No suitable PIN input fields found");
            return { success: false, method: "none", message: "Could not find any suitable PIN input field" };
        }
        """, used_pin)
        
        # Process result with error handling exactly like in PHP
        if pin_input_result and pin_input_result.get('success', False):
            log(f"PIN input successful: {pin_input_result.get('message')} (method: {pin_input_result.get('method')})")
        else:
            log(f"Warning: {pin_input_result.get('message', 'Unknown error')}")
            
            # Try fallback direct keyboard entry if all else fails
            log("Attempting fallback PIN entry method with keyboard...")
            try:
                await page.keyboard.type(used_pin, {'delay': 200})
                await page.keyboard.press('Enter')
                log("Typed PIN using direct keyboard input as fallback")
            except Exception as ke:
                log(f"Keyboard fallback also failed: {ke}")
                
        # Try to find and click a confirm button after PIN entry - exactly matching PHP
        log('Looking for confirm button after PIN entry...')
        button_clicked = await page.evaluate("""
        () => {
            const allButtons = document.querySelectorAll("button");
            let continueButton, backButton;
            allButtons.forEach((button) => {
              const buttonText = button.innerText.trim().toLowerCase();
              if (buttonText.includes("lanjut") || 
                  buttonText.includes("continue") || 
                  buttonText.includes("submit") || 
                  buttonText.includes("confirm") || 
                  buttonText.includes("next") || 
                  button.className.includes("btn-continue") || 
                  button.className.includes("btn-submit") || 
                  button.className.includes("btn-confirm")) {
                continueButton = button;
              }
            });
            if (continueButton) {
              continueButton.click();
              return { clicked: true, message: "Found continue button, clicked it: " + continueButton.innerText };
            }
            return { clicked: false, message: "No confirm/continue button found" };
        }
        """)
        
        if button_clicked and button_clicked.get('clicked', False):
            log(f"Confirm button clicked: {button_clicked.get('message')}")
        # Notice no else case here to match PHP exactly
        
        # Wait a moment after clicking confirm button
        await page.wait_for_timeout(1500)  # 1.5 seconds like in PHP implementation
        
        # Take a screenshot after button click to help with debugging
        try:
            screenshot_path = Path('dana_oauth_after_confirm.png')
            await page.screenshot(path=str(screenshot_path))
            log(f"After-confirm screenshot saved to {screenshot_path}")
        except Exception as e:
            log(f"Failed to take screenshot: {str(e)}")
            
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
            return params.get('authCode', [None])[0]

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

def get_auth_code(oauth_url, phone_number=None, pin=None):
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
        return asyncio.run(automate_oauth(oauth_url=oauth_url, phone_number=phone_number, pin=pin, show_log=True))
    except Exception as e:
        print(f"Error during OAuth automation: {e}")
        return None

if __name__ == '__main__':
    code = get_auth_code()
    print(f'Auth code: {code}')
