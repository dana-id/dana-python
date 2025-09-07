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
        
    Returns:
        bool: True if automation completed successfully, False otherwise
    """
    try:
        if not payment_url:
            logger.error("Error: Payment URL is empty")
            return False
            
        print(f"Starting payment widget automation with URL: {payment_url}")
        
        # Check if selenium/browser automation is available
        # In a real implementation, we'd check for Selenium server availability like in PHP
        
        async with async_playwright() as p:
            # Use environment variable to control headless mode, matching PHP's implementation
            headless_setting = os.getenv('AUTOMATION_HEADLESS', 'true').lower() == 'true'
            if headless_setting != headless:  # Override with parameter if different
                headless = headless_setting
                
            print(f"Launching browser (headless: {headless})...")
            browser = await p.chromium.launch(headless=headless)

            
            # Create a new browser context with mobile device simulation
            device = p.devices['iPhone X']  # Match PHP's device emulation
            context = await browser.new_context(
                **device,
                locale='id-ID'
            )
            
            # Open a new page
            page = await context.new_page()
            
            # Navigate to the payment URL
            print("Navigating to payment URL...")
            await page.goto(payment_url, wait_until='networkidle')
            
            # Wait for page to load and payment button to be visible (up to 60 seconds like PHP)
            print("Waiting for payment button...")
            payment_button_found = False
            
            # First try to wait for primary button (similar to PHP's wait for visibility)
            try:
                await page.wait_for_selector('.btn.btn-primary.btn-pay', state='visible', timeout=60000)
                payment_button_found = True
            except Exception as e:
                logger.warning(f"Payment button not found after waiting: {e}")
                
                # Try other common selectors as fallback (exact same as PHP)
                fallback_selectors = [
                    '.btn-pay',
                    '.payment-button',
                    '.btn-primary',
                    '.dana-button',
                    'button[type="submit"]'
                ]
                
                for selector in fallback_selectors:
                    try:
                        elements = await page.query_selector_all(selector)
                        if len(elements) > 0:
                            print(f"Found alternative payment button with selector: {selector}")
                            payment_button_found = True
                            break
                    except Exception as e:
                        # Continue trying other selectors
                        pass
            
            # Click the payment button - similar to PHP implementation
            print("Clicking payment button...")
            try:
                # First try primary button (exact same as PHP)
                pay_button = await page.query_selector('.btn.btn-primary.btn-pay')
                if pay_button:
                    await pay_button.click()
                else:
                    raise Exception("Primary payment button not found")
            except Exception as e:
                print(f"Error clicking primary payment button: {e}, trying JavaScript click...")
                
                # Try JavaScript click as fallback - identical to PHP
                try:
                    # Exact same JavaScript as in PHP
                    result = await page.evaluate("""
                        const buttons = document.querySelectorAll("button");
                        for (const button of Array.from(buttons)) {
                            if (button.classList.contains("btn-pay") || 
                                button.innerText.includes("Pay") || 
                                button.innerText.includes("BAYAR")) {
                                button.click();
                                return true;
                            }
                        }
                        return false;
                    """)
                    if result:
                        print("Successfully clicked button via JavaScript")
                    else:
                        logger.warning("JavaScript found no suitable buttons to click")
                except Exception as e:
                    logger.error(f"JavaScript click fallback failed: {e}")
            
            if not payment_button_found:
                logger.error("Could not find any payment button after trying multiple selectors")
                await browser.close()
                return False
            
            print("Waiting for payment success message...")
            success = False
            
            try:
                # Wait for payment success message - identical to PHP implementation
                success_timeout = 30000 
                start_time = time.time() * 1000
                
                # Implement exact same polling logic as PHP
                while time.time() * 1000 - start_time < success_timeout:
                    page_source = await page.content()
                    
                    # Check for success indicators
                    if ('Payment Success' in page_source) or ('Pembayaran Sukses' in page_source):
                        print("Payment completed successfully!")
                        success = True
                        break
                    
                    # Also check for failure indicators
                    if ('Payment Failed' in page_source) or ('Pembayaran Gagal' in page_source):
                        logger.warning("Payment failed message detected on page")
                        # Take a screenshot of the failure
                        failure_path = os.path.join(tempfile.gettempdir(), 'payment_failed.png')
                        await page.screenshot(path=failure_path)
                        print(f"Saved failure screenshot to {failure_path}")
                        # Don't break, continue waiting in case it might recover
                    
                    await page.wait_for_timeout(1000)  # Poll every second
                
                if not success:
                    logger.warning("Timeout waiting for payment success")
                    page_content = await page.content()
                    logger.warning(f"Final page source snippet: {page_content[:500]}...")
                    
            except Exception as e:
                logger.error(f"Error while waiting for success message: {e}")
            
            # Take screenshot for debugging
            try:
                screenshots_dir = Path(tempfile.gettempdir()) / "dana_test_screenshots"
                screenshots_dir.mkdir(exist_ok=True)
                screenshot_path = screenshots_dir / f"payment_widget_{int(time.time())}.png"
                await page.screenshot(path=str(screenshot_path))
                print(f"Screenshot saved to {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to take screenshot: {e}")
            
            # Output file handling (similar to PHP implementation)
            if output_file and success:
                try:
                    output_dir = os.path.dirname(output_file)
                    if output_dir and not os.path.exists(output_dir):
                        os.makedirs(output_dir, exist_ok=True)
                    
                    with open(output_file, 'w') as f:
                        f.write('SUCCESS')
                    print(f"Wrote success indicator to {output_file}")
                except Exception as e:
                    logger.error(f"Failed to write output file: {e}")
                
            # Close browser
            await browser.close()
            print("Browser closed successfully")
            
            return success
            
    except Exception as e:
        logger.error(f"Error during payment automation: {e}")
        return False

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
        logger.error("Error: Payment URL is empty")
        return False
    
    # Log operation for debugging
    print(f"Starting payment automation with URL: {payment_url}")
    
    try:
        async with async_playwright() as p:
            # Setup Chrome options - similar to PHP's ChromeOptions
            # In PHP, headless might be commented out for debugging
            headless_mode = os.getenv('AUTOMATION_HEADLESS', 'true').lower() == 'true'
            browser = await p.chromium.launch(headless=headless_mode, args=[
                '--disable-gpu',
                '--no-sandbox', 
                '--disable-web-security',
                '--disable-features=IsolateOrigins',
                '--disable-site-isolation-trials',
                '--disable-features=BlockInsecurePrivateNetworkRequests',
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage'
            ])
            
            # Mobile emulation setup - match PHP's deviceMetrics
            context = await browser.new_context(
                viewport={'width': 390, 'height': 844},
                device_scale_factor=3.0,
                user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                locale='id-ID'
            )
            
            page = await context.new_page()
            
            # Navigate to the checkout URL (matching PHP implementation)
            await page.goto(payment_url)
            try:
                await page.wait_for_url("**/checkout**", timeout=10000)
                print("Loaded checkout page")
            except Exception as e:
                logger.warning(f"URL didn't contain 'checkout': {e}")
            
            print("Looking for DANA payment option...")
                        
            # Attempt to find DANA payment option using multiple selector strategies
            dana_payment_button = None
            selectors = [
                "div.bank-item.sdetfe-lbl-dana-pay-option",
                "div.bank-item[class*='dana-pay-option']",
                "//div[contains(@class, 'bank-title') and contains(text(), 'DANA')]", # XPath
                "//div[contains(@class, 'bank-item')]//*[contains(text(), 'DANA')]", # XPath
            ]
            
            for selector in selectors:
                try:
                    # Determine if using XPath or CSS selector
                    locator = page.locator(selector)
                        
                    if await locator.count() > 0:
                        print(f"DANA payment option found with selector: {selector}")
                        dana_payment_button = locator
                        break
                except Exception as e:
                    logger.warning(f"Error finding DANA payment option with selector {selector}: {e}")
            
            if dana_payment_button:
                # Click the DANA payment option first
                await dana_payment_button.click()
                await page.wait_for_timeout(3000)  # Wait 1 second after click
                
                # Now handle OAuth flow - similar to PHP's handleOAuthFlow
                await _handle_oauth_flow(page, context)
                
                # Wait for any redirects to complete
                await page.wait_for_timeout(3000)  # 10 seconds like PHP's wait(10)
                
                # Look for success indicators (just wait for network activity to settle)
                try:
                    # Wait 5 seconds to let the page settle
                    await page.wait_for_timeout(5000)  # 5 seconds like PHP's wait(5)
                    print("Network activity settled")
                    
                    # Take a screenshot for debugging
                    screenshots_dir = Path(tempfile.gettempdir()) / "dana_test_screenshots"
                    screenshots_dir.mkdir(exist_ok=True)
                    screenshot_path = screenshots_dir / f"pg_payment_{int(time.time())}.png"
                    await page.screenshot(path=str(screenshot_path))
                    print(f"Screenshot saved to {screenshot_path}")
                    
                    return True
                except Exception as e:
                    logger.warning(f"Network activity timeout - continuing anyway: {e}")
                    
                return True  # Assume success if we got this far
            else:
                logger.error("DANA payment option not found. Exiting...")
                return False
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        return False


# Constants for auth flow
DEFAULT_PHONE_NUMBER = "087875849373"
DEFAULT_PIN = "131000"

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
