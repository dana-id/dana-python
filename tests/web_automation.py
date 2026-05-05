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

from ast import Return
import os
import time
import asyncio
import tempfile
from pathlib import Path
from playwright.async_api import async_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def _automate_payment_widget(payment_url: str, headless: bool = True, output_file: str = None) -> bool:
    """
    Automates the payment flow using Playwright in a headless browser.

    Args:
        payment_url: The URL to the payment widget with OTT token
        output_file: Optional path to write 'SUCCESS' on completion

    Returns:
        bool: True if automation completed successfully, False otherwise
    """
    if not payment_url:
        logger.error("Error: Payment URL is empty")
        return False

    print(f"Starting payment widget automation with URL: {payment_url}")

    headless = os.getenv('AUTOMATION_HEADLESS', 'true').lower() == 'true'

    browser = None
    success = False
    try:
        async with async_playwright() as p:
            launch_args = [
                '--no-sandbox',
                '--disable-web-security',
                '--disable-features=IsolateOrigins',
                '--disable-site-isolation-trials',
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
            ]
            chromium_path = os.getenv('CHROMIUM_PATH')
            if not chromium_path and os.getenv('CI'):
                candidate = '/usr/bin/chromium-browser'
                if os.path.exists(candidate):
                    chromium_path = candidate

            print(f"Launching browser (headless: {headless})...")
            browser = await p.chromium.launch(
                headless=headless,
                args=launch_args,
                **({"executable_path": chromium_path} if chromium_path else {}),
            )

            context = await browser.new_context(
                user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
                viewport={'width': 390, 'height': 844},
            )
            page = await context.new_page()

            print("Navigating to payment URL...")
            await page.goto(payment_url, timeout=60000)

            # Wait for the pay button (up to 60 s)
            print("Waiting for payment button...")
            pay_selector = '.btn.btn-primary.btn-pay'
            try:
                await page.wait_for_selector(pay_selector, state='visible', timeout=60000)
            except Exception:
                # Fallback: look for any visible button that looks like a pay button
                fallback_selectors = [
                    '.btn-pay',
                    '.payment-button',
                    'button[type="submit"]',
                ]
                found_fallback = False
                for sel in fallback_selectors:
                    try:
                        await page.wait_for_selector(sel, state='visible', timeout=5000)
                        pay_selector = sel
                        found_fallback = True
                        print(f"Using fallback payment button selector: {sel}")
                        break
                    except Exception:
                        pass
                if not found_fallback:
                    # Last resort: JS scan
                    clicked = await page.evaluate("""
                        () => {
                            for (const btn of document.querySelectorAll('button')) {
                                if (btn.classList.contains('btn-pay') ||
                                    (btn.innerText || '').match(/bayar|pay/i)) {
                                    btn.click();
                                    return true;
                                }
                            }
                            return false;
                        }
                    """)
                    if clicked:
                        print("Clicked payment button via JavaScript fallback")
                    else:
                        print("Error: Could not find any payment button")
                        raise Exception("Primary payment button not found after all fallbacks")

            # Click the pay button
            print("Clicking payment button...")
            try:
                await page.click(pay_selector)
            except Exception as e:
                print(f"Direct click failed ({e}), trying JS click...")
                await page.evaluate(f"document.querySelector('{pay_selector}')?.click()")

            # Wait for success indicator
            print("Waiting for payment success message...")
            try:
                await page.wait_for_selector(
                    'text="Payment Success"',
                    timeout=120000,
                )
                print("Payment completed successfully!")
                success = True
            except Exception:
                print("Warning: Timeout waiting for payment success indicator")

            # Write output file on success
            if output_file and success:
                try:
                    os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
                    with open(output_file, 'w') as f:
                        f.write('SUCCESS')
                    print(f"Wrote success indicator to {output_file}")
                except Exception as e:
                    logger.error(f"Failed to write output file: {e}")

            await browser.close()
            print("Browser closed successfully")

    except Exception as e:
        print(f"Error during payment widget automation: {e}")
        import traceback
        traceback.print_exc()
        if browser:
            try:
                await browser.close()
            except Exception:
                pass

    return success

def automate_payment_widget(payment_url: str, headless: bool = True, output_file: str = None) -> bool:
    """Synchronous wrapper for the asynchronous payment widget automation function.
    
    Args:
        payment_url: The URL to the payment widget with OTT token
        headless: Whether to run browser in headless mode
        output_file: Optional file path to write success indicator to
        
    Returns:
        bool: True if automation completed successfully, False otherwise
    """
    # Try to get the event loop, create a new one if it doesn't exist
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    except RuntimeError:
        # No event loop exists
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    # Run the automation in the loop and pass the output_file parameter
    success = loop.run_until_complete(_automate_payment_widget(payment_url, headless, output_file))
    
    return success


async def _automate_payment_payment_gateway(payment_url: str) -> bool:
    """Automates the payment flow for Payment Gateway using Playwright.
    
    Args:
        payment_url: The URL to the payment page
        
    Returns:
        bool: True if automation completed successfully, False otherwise
    """
    if not payment_url:
        print("Error: Payment URL is empty")
        return False

    print(f"Starting payment automation with URL: {payment_url}")

    max_attempts = 2
    for attempt in range(1, max_attempts + 1):
        try:
            async with async_playwright() as p:
                headless_mode = os.getenv('AUTOMATION_HEADLESS', 'true').lower() == 'true'
                chromium_path = os.getenv('CHROMIUM_PATH')
                if not chromium_path and os.getenv('CI'):
                    candidate = '/usr/bin/chromium-browser'
                    if os.path.exists(candidate):
                        chromium_path = candidate

                browser = await p.chromium.launch(
                    headless=headless_mode,
                    slow_mo=100,
                    args=[
                        '--no-sandbox',
                        '--disable-web-security',
                        '--disable-features=IsolateOrigins',
                        '--disable-site-isolation-trials',
                        '--disable-blink-features=AutomationControlled',
                        '--disable-dev-shm-usage',
                    ],
                    **({"executable_path": chromium_path} if chromium_path else {}),
                )

                context = await browser.new_context(
                    viewport={'width': 390, 'height': 844},
                    user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                )

                page = await context.new_page()

                print(f"Navigating to checkout (attempt {attempt})...")
                await page.goto(payment_url, timeout=60000)
                # Use 'load' (not networkidle) to avoid timing out on persistent background requests
                await page.wait_for_load_state('load', timeout=30000)
                await page.wait_for_timeout(2000)  # Extra settle time for JS-rendered content
                print("Loaded checkout page")

                print("Looking for DANA payment option...")

                # Try Playwright CSS selectors first
                dana_locator = None
                bank_item_selectors = [
                    "div.bank-item.sdetfe-lbl-dana-pay-option",
                    "div.bank-item[class*='dana-pay-option']",
                    "div.bank-item:has(div.bank-title:has-text('DANA'))",
                    "div.bank-title:has-text('DANA')",
                    "div.bank-item:has-text('DANA')",
                    "xpath=//div[contains(@class,'bank-title') and contains(text(),'DANA')]",
                    "xpath=//div[contains(@class,'bank-item')]//*[contains(text(),'DANA')]",
                ]
                for sel in bank_item_selectors:
                    try:
                        loc = page.locator(sel).first
                        await loc.wait_for(state='visible', timeout=3000)
                        if await loc.is_visible():
                            print(f"DANA payment option found with selector: {sel}")
                            dana_locator = loc
                            break
                    except Exception:
                        pass

                if dana_locator is not None:
                    await dana_locator.click()
                else:
                    # JavaScript fallback: scan all elements for DANA text and click
                    print("CSS selectors failed, trying JavaScript scan for DANA option...")
                    dana_clicked = await page.evaluate("""
                        () => {
                            const candidates = [
                                ...document.querySelectorAll('[class*="bank-item"]'),
                                ...document.querySelectorAll('[class*="bank-title"]'),
                                ...document.querySelectorAll('[class*="payment-option"]'),
                                ...document.querySelectorAll('[class*="dana"]'),
                                ...document.querySelectorAll('button'),
                                ...document.querySelectorAll('a'),
                            ];
                            // Deduplicate
                            const seen = new Set();
                            const unique = candidates.filter(el => {
                                if (seen.has(el)) return false;
                                seen.add(el);
                                return true;
                            });
                            for (const el of unique) {
                                const text = (el.textContent || '').trim();
                                if (text === 'DANA' || text.startsWith('DANA') ||
                                    el.className.toLowerCase().includes('dana')) {
                                    // Prefer clicking the outermost bank-item ancestor
                                    const bankItem = el.closest('[class*="bank-item"]') || el;
                                    bankItem.click();
                                    return bankItem.className || 'unknown';
                                }
                            }
                            return null;
                        }
                    """)
                    if dana_clicked:
                        print(f"DANA option clicked via JavaScript (element class: {dana_clicked})")
                    else:
                        print("DANA payment option not found by any method. Exiting...")
                        await browser.close()
                        if attempt < max_attempts:
                            print("Retrying...")
                            continue
                        return False

                await page.wait_for_timeout(1000)

                # OAuth flow runs in a new page opened by the click
                await _handle_oauth_flow(page, context)

                await page.wait_for_timeout(5000)

                screenshots_dir = Path(tempfile.gettempdir()) / "dana_test_screenshots"
                screenshots_dir.mkdir(exist_ok=True)
                screenshot_path = screenshots_dir / f"pg_payment_{int(time.time())}.png"
                try:
                    await page.screenshot(path=str(screenshot_path))
                    print(f"Screenshot saved to {screenshot_path}")
                except Exception:
                    pass

                print("Network activity settled")
                await browser.close()
                return True

        except Exception as e:
            print(f"Error during payment gateway automation (attempt {attempt}): {e}")
            import traceback
            traceback.print_exc()
            if attempt >= max_attempts:
                return False

    return False


# Constants for auth flow
DEFAULT_PHONE_NUMBER = "083811223355"
DEFAULT_PIN = "181818"

async def _handle_oauth_flow(page, context):
    """Handle OAuth flow with phone number and PIN entry.
    
    Args:
        page: Playwright page object
    """
    print("Handling OAuth flow...")
    
    try:
        # Print information about current page
        print(f"DEBUG: Current page URL before OAuth: {page.url}")
        
        # Access pages as a property, not a method
        pages = context.pages
        print(f"DEBUG: Found {len(pages)} pages in context")
        
        # Print all page URLs
        for i, p in enumerate(pages):
            print(f"DEBUG: Page {i} URL: {p.url}")
            
        # Based on the screenshot, we want page at index 1
        if len(pages) > 1:
            # Explicitly use page 1 (second page) as we can see it has the Dana OAuth page
            new_page = pages[1]
            print(f"DEBUG: Using page 1 (index 1) for OAuth flow with URL: {new_page.url}")
        else:
            # No second page detected, try to continue with current page
            print("WARNING: No second page detected for OAuth flow, continuing with original page")
            return False
        
        await new_page.wait_for_timeout(5000)  # Wait for page to stabilize
        
        # Take screenshots of all pages for debugging
        for i, p in enumerate(pages):
            try:
                await p.screenshot(path=f'debug_page_{i}.png')
                print(f"DEBUG: Captured screenshot of page {i}")
            except Exception as e:
                print(f"ERROR: Could not capture screenshot of page {i}: {e}")
        
        phone_entered = False
    except Exception as e:
        print(f"ERROR in OAuth flow setup: {e}")
        return False
    
    # Take a screenshot of the initial page for debugging
    try:
        await new_page.screenshot(path='01_phone_screen_initial.png')
        print("Initial phone screen screenshot captured")
        
        # Capture HTML content for debugging
        html_content = await new_page.content()
        with open('phone_page_html.txt', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("HTML content captured for debugging")
        
        # Print all input elements for debugging
        input_elements = await new_page.evaluate("""
        () => {
            const inputs = document.querySelectorAll('input');
            return Array.from(inputs).map(input => ({
                type: input.type,
                id: input.id,
                name: input.name,
                class: input.className,
                placeholder: input.placeholder,
                maxLength: input.maxLength,
                pattern: input.pattern,
                isVisible: input.offsetParent !== null
            }));
        }
        """)
        print("All input elements on page:")
        for idx, inp in enumerate(input_elements):
            print(f"Input #{idx+1}:", inp)
    except Exception as e:
        print(f"Error capturing debug info: {e}")
    
    try:
        # Try JavaScript approach targeting the Dana login page elements we can see in the screenshot
        print("Attempting phone number input with JavaScript for Dana OAuth page...")
        phone_result = await new_page.evaluate("""
        (phoneNumber) => {
            // Debug info
            const allInputs = document.querySelectorAll('input');
            console.log('Found', allInputs.length, 'input elements on page');
            
            // First try specific phone input using most common selectors
            const tel_input = document.querySelector('input[type="tel"]');
            if (tel_input) {
                console.log('Found tel input:', tel_input);
                try {
                    tel_input.focus();
                    tel_input.value = phoneNumber;
                    tel_input.dispatchEvent(new Event('input', {bubbles: true}));
                    tel_input.dispatchEvent(new Event('change', {bubbles: true}));
                    return {success: true, message: 'Set value directly on tel input'};
                } catch (e) {
                    console.error('Error setting tel input:', e);
                }
            }
            
            // Try using querySelector to find specific input class from the screenshot
            const txtInputPhone = document.querySelector('input.txt-input-phone-number-field');
            if (txtInputPhone) {
                console.log('Found txt-input-phone-number-field input');
                try {
                    txtInputPhone.focus();
                    txtInputPhone.value = phoneNumber;
                    txtInputPhone.dispatchEvent(new Event('input', {bubbles: true}));
                    txtInputPhone.dispatchEvent(new Event('change', {bubbles: true}));
                    return {success: true, message: 'Set value on txt-input-phone-number-field'};
                } catch (e) {
                    console.error('Error setting txt-input-phone-number-field:', e);
                }
            }
            
            return {success: false, message: 'Failed to set phone input via JavaScript'};
        }
        """, DEFAULT_PHONE_NUMBER)
        
        if phone_result.get('success'):
            print(f"Phone input succeeded via JS: {phone_result.get('message')}")
        else:
            print(f"Phone input failed via JS: {phone_result.get('message')}")
            return False
        
    except Exception as e:
        print(f"Error during phone input handling: {e}")
        # Take screenshot of error state
        try:
            await new_page.screenshot(path='error_state.png')
        except Exception:
            pass
        return False
    
    next_button_selectors = [
        # Standard CSS selectors
        'button.btn-primary',
        'button.btn-next',
        'button.next-btn',
        'button.btn-continue',
        'button.dana-btn-primary',
        'button.submit-button',
        '.btn.btn-primary',
        '.button-submit',
        'button[type="submit"]',
        'form .button',
        '.form-footer button',
        '.footer-button button',
        # XPath selectors for text matching
        '//button[contains(text(),"Next")]',
        '//button[text()="Next"]',
        '//button[contains(text(),"Continue")]',
        '//button[text()="Continue"]',
        '//button[contains(text(),"Lanjut")]',
        '//button[contains(text(),"Lanjutkan")]',
        '//button[contains(text(),"Selanjutnya")]',
        # Additional selectors for common next/continue button patterns
        'button.ant-btn',
        'button.ant-btn-primary'
    ]

    print("Clicking next button...")
    
    next_button_clicked = False
    for selector in next_button_selectors:
        try:
            locator = new_page.locator(selector)
            
            if await locator.count() > 0:
                print(f"Found next button with selector: {selector}")
                first_element = locator.first
                
                # Use direct JavaScript click with selector - this worked in testing
                print(f"Trying JavaScript click with selector: {selector}")
                
                # Use the appropriate JavaScript based on selector type
                if selector.startswith('//'):
                    # XPath selector
                    js_code = f'''
                    () => {{  
                        const elements = document.evaluate("{selector}", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                        if (elements.snapshotLength > 0) {{  
                            const element = elements.snapshotItem(0);
                            element.click();
                            return true;
                        }}
                        return false;
                    }}
                    '''
                else:
                    # CSS selector
                    js_code = f'''
                    () => {{  
                        const element = document.querySelector("{selector}");
                        if (element) {{  
                            element.click();
                            return true;
                        }}
                        return false;
                    }}
                    '''
                
                clicked = await new_page.evaluate(js_code)
                if clicked:
                    print("JavaScript click successful!")
                    next_button_clicked = True
                    break
                else:
                    print("JavaScript click found no elements, trying next selector...")
            else:
                logger.warning(f"Continue button with selector {selector} not found")
        except Exception as e:
            logger.error(f"Error clicking continue button with selector: {selector}, {e}")
            return False
    
    if not next_button_clicked:
        logger.error("Failed to find or click next button!")
        return False
    
    # Wait 1 second after clicking next
    await new_page.wait_for_timeout(1000)
    
    # Enter PIN
    await _enter_pin(new_page)
    
    # Wait 1 second after PIN entry
    await new_page.wait_for_timeout(3000)
    
    # Click Pay button
    await _click_pay_button(new_page)
    
    # Wait 1 second after clicking pay
    await new_page.wait_for_timeout(2000)

async def _enter_pin(page):
    """Enter PIN for DANA payment using JavaScript.
    
    Args:
        page: Playwright page object
    """
    pin_entered = False
    
    try:
        print("Trying JavaScript method for PIN entry")
        
        # Find all input fields within containers - using the same selectors as PHP
        inputs = page.locator('input[type="password"], input[type="tel"], input[pattern="[0-9]*"], input.password-focus')
        input_count = await inputs.count()
        
        if input_count >= 1:
            # If it's a single input for all digits
            if input_count == 1:
                input_selector = 'input[type="password"], input[type="tel"], input[pattern="[0-9]*"], input.password-focus'
                await page.evaluate('''
                (args) => {
                    const input = document.querySelector(args.selector);
                    if (input) {
                        input.value = args.pin;
                        input.dispatchEvent(new Event("input"));
                        input.dispatchEvent(new Event("change"));
                        console.log("PIN entered in single input field");
                    }
                }''', {"selector": input_selector, "pin": DEFAULT_PIN})
                pin_entered = True
            
            # If we have individual inputs for each digit (typical pattern)
            elif input_count >= 6:
                print(f"Found {input_count} PIN input fields, entering digits individually")
                
                # Use JavaScript to populate each input without clicking
                input_selector = 'input[type="password"], input[type="tel"], input[pattern="[0-9]*"], input.password-focus'
                pin_digits = [d for d in DEFAULT_PIN[:6]]
                
                # Use a single JavaScript call to set all digits
                await page.evaluate('''
                (args) => {
                    const inputs = document.querySelectorAll(args.selector);
                    console.log("Found " + inputs.length + " PIN inputs for multiple entry");
                    
                    if (inputs.length >= 6) {
                        for (let i = 0; i < Math.min(6, inputs.length); i++) {
                            inputs[i].value = args.digits[i];
                            inputs[i].dispatchEvent(new Event("input"));
                            inputs[i].dispatchEvent(new Event("change"));
                            console.log("Set PIN digit " + (i+1) + " to " + args.digits[i]);
                            
                            // Small delay between inputs
                            if (i < 5) {
                                // This is a synchronous delay in the browser, not in Python
                                const start = new Date().getTime();
                                while(new Date().getTime() < start + 100) {}
                            }
                        }
                    }
                }''', {"selector": input_selector, "digits": pin_digits})
                
                # Add a small delay after PIN entry
                await page.wait_for_timeout(200)
                    
                pin_entered = True
            
            if pin_entered:
                print("PIN entered successfully via JavaScript")
        else:
            print("Could not find PIN input fields")
            logger.warning("Could not find PIN input fields")
            return False
    except Exception as e:
        print(f"Error using JavaScript method for PIN: {e}")
        return False
    
    await page.wait_for_timeout(2000)
    return pin_entered


async def _click_pay_button(page):
    """Click the pay/confirm button to complete the payment.
    
    Args:
        page: Playwright page object
    """
    print("Attempting to click pay button...")
    
    # Match PHP selectors exactly
    pay_button_selectors = [
        # CSS Selectors
        'button.btn.btn-primary.btn-pay',
        'button.btn-pay',
        'button.payment-button',
        'button.btn-primary',
        'button.dana-button',
        'button.ant-btn',
        'button[type="submit"]',
        # XPath Selectors for text matching
        '//button[contains(text(),"PAY Rp")]',
        '//button[contains(text(),"Bayar Rp")]',
        '//button[contains(text(),"PAY")]',
        '//button[contains(text(),"BAYAR")]',
        '//button[contains(text(),"Pay")]',
        '//button[contains(text(),"Bayar")]',
        '//button[contains(text(),"Confirm")]',
        '//button[contains(text(),"Continue")]'
    ]
    
    pay_button_clicked = False
    for selector in pay_button_selectors:
        print(f"Looking for pay button with selector: {selector}")
        
        try:
            # Determine if using XPath or CSS selector
            locator = page.locator(selector)
            count = await locator.count()
            
            if count > 0:
                print(f"Found pay button with selector: {selector}, attempting to click...")
                
                # Try JavaScript click first to avoid potential interception
                try:
                    # Use the appropriate JavaScript based on selector type
                    if selector.startswith('//'):
                        # XPath selector
                        js_code = f'''
                        () => {{  
                            const elements = document.evaluate("{selector}", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                            if (elements.snapshotLength > 0) {{  
                                const element = elements.snapshotItem(0);
                                element.click();
                                return true;
                            }}
                            return false;
                        }}
                        '''
                    else:
                        # CSS selector
                        js_code = f'''
                        () => {{  
                            const element = document.querySelector("{selector}");
                            if (element) {{  
                                element.click();
                                return true;
                            }}
                            return false;
                        }}
                        '''
                    
                    clicked = await page.evaluate(js_code)
                    if not clicked:
                        # Fall back to regular click if JavaScript click fails
                        await locator.first.click()
                    
                    pay_button_clicked = True
                    await page.wait_for_timeout(1000)  # Wait 1 second like PHP
                    print("Pay button clicked successfully")
                    break
                    
                except Exception as js_click_exception:
                    print(f"JavaScript click failed: {js_click_exception}, trying regular click")
                    # Fall back to regular click if JavaScript click fails
                    try:
                        await locator.first.click()
                        pay_button_clicked = True
                        await page.wait_for_timeout(1000)  # Wait 1 second like PHP
                        print("Pay button clicked successfully using regular click")
                        break
                    except Exception as regular_click_exception:
                        print(f"Regular click also failed: {regular_click_exception}")
            else:
                print(f"No pay button found with selector: {selector}")
        except Exception as e:
            print(f"Error clicking pay button {selector}: {e}")
            logger.warning(f"Error clicking pay button {selector}: {e}")
    
    # Short wait to let UI update - exactly like PHP
    await page.wait_for_timeout(3000)  # 3 seconds wait
    
    if not pay_button_clicked:
        print("Could not find pay button")
        logger.warning("Could not find pay button")
        return False
    
    return True


def automate_payment_payment_gateway(payment_url: str) -> bool:
    """Synchronous wrapper for the asynchronous payment gateway automation function.
    
    Args:
        payment_url: The URL to the payment page
        
    Returns:
        bool: True if automation completed successfully, False otherwise
    """
    # Try to get the event loop, create a new one if it doesn't exist
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    except RuntimeError:
        # No event loop exists
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    # Run the automation in the loop
    return loop.run_until_complete(_automate_payment_payment_gateway(payment_url))
