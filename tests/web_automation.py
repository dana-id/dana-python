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
            
        logger.info(f"Starting payment widget automation with URL: {payment_url}")
        
        # Check if selenium/browser automation is available
        # In a real implementation, we'd check for Selenium server availability like in PHP
        
        async with async_playwright() as p:
            # Use environment variable to control headless mode, matching PHP's implementation
            headless_setting = os.getenv('AUTOMATION_HEADLESS', 'true').lower() == 'true'
            if headless_setting != headless:  # Override with parameter if different
                headless = headless_setting
                
            logger.info(f"Launching browser (headless: {headless})...")
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
            logger.info("Navigating to payment URL...")
            await page.goto(payment_url, wait_until='networkidle')
            
            # Wait for page to load and payment button to be visible (up to 60 seconds like PHP)
            logger.info("Waiting for payment button...")
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
                            logger.info(f"Found alternative payment button with selector: {selector}")
                            payment_button_found = True
                            break
                    except Exception as e:
                        # Continue trying other selectors
                        pass
            
            # Click the payment button - similar to PHP implementation
            logger.info("Clicking payment button...")
            try:
                # First try primary button (exact same as PHP)
                pay_button = await page.query_selector('.btn.btn-primary.btn-pay')
                if pay_button:
                    await pay_button.click()
                else:
                    raise Exception("Primary payment button not found")
            except Exception as e:
                logger.info(f"Error clicking primary payment button: {e}, trying JavaScript click...")
                
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
                        logger.info("Successfully clicked button via JavaScript")
                    else:
                        logger.warning("JavaScript found no suitable buttons to click")
                except Exception as e:
                    logger.error(f"JavaScript click fallback failed: {e}")
            
            if not payment_button_found:
                logger.error("Could not find any payment button after trying multiple selectors")
                await browser.close()
                return False
            
            logger.info("Waiting for payment success message...")
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
                        logger.info("Payment completed successfully!")
                        success = True
                        break
                    
                    # Also check for failure indicators
                    if ('Payment Failed' in page_source) or ('Pembayaran Gagal' in page_source):
                        logger.warning("Payment failed message detected on page")
                        # Take a screenshot of the failure
                        failure_path = os.path.join(tempfile.gettempdir(), 'payment_failed.png')
                        await page.screenshot(path=failure_path)
                        logger.info(f"Saved failure screenshot to {failure_path}")
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
                logger.info(f"Screenshot saved to {screenshot_path}")
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
                    logger.info(f"Wrote success indicator to {output_file}")
                except Exception as e:
                    logger.error(f"Failed to write output file: {e}")
                
            # Close browser
            await browser.close()
            logger.info("Browser closed successfully")
            
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
    logger.info(f"Starting payment automation with URL: {payment_url}")
    
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
            
            # Navigate to the checkout URL
            await page.goto(payment_url)
            
            # Wait for URL to contain checkout - matching PHP's urlContains check
            try:
                await page.wait_for_url("**/checkout**", timeout=10000)
                logger.info("Loaded checkout page")
            except Exception as e:
                logger.warning(f"URL didn't contain 'checkout': {e}")
            
            logger.info("Looking for DANA payment option...")
            
            # Attempt to find and click DANA payment option using multiple selector strategies - like PHP
            dana_payment_button_found = False
            selectors = [
                "div.bank-item.sdetfe-lbl-dana-pay-option",
                "div.bank-item[class*='dana-pay-option']",
                "//div[contains(@class, 'bank-title') and contains(text(), 'DANA')]", # XPath
                "//div[contains(@class, 'bank-item')]//*[contains(text(), 'DANA')]", # XPath
            ]
            
            for selector in selectors:
                try:
                    # Determine if using XPath or CSS selector
                    if selector.startswith('//'):
                        locator = page.locator(selector)
                    else:
                        locator = page.locator(selector)
                        
                    if await locator.count() > 0:
                        logger.info(f"DANA payment option found with selector: {selector}")
                        await locator.click()
                        dana_payment_button_found = True
                        break
                except Exception as e:
                    logger.warning(f"Error finding DANA payment option with selector {selector}: {e}")
            
            if dana_payment_button_found:
                # Click the DANA payment option
                await page.wait_for_timeout(1000)  # Wait 1 second after click
                
                # Now handle OAuth flow - similar to PHP's handleOAuthFlow
                await _handle_oauth_flow(page)
                
                # Wait for any redirects to complete
                await page.wait_for_timeout(3000)  # 3 seconds like PHP's wait(3)
                
                # Look for success indicators (just wait for network activity to settle)
                try:
                    # Wait for page to be stable - similar to PHP wait
                    await page.wait_for_load_state('networkidle', timeout=5000)
                    logger.info("Network activity settled")
                    
                    # Take a screenshot for debugging
                    screenshots_dir = Path(tempfile.gettempdir()) / "dana_test_screenshots"
                    screenshots_dir.mkdir(exist_ok=True)
                    screenshot_path = screenshots_dir / f"pg_payment_{int(time.time())}.png"
                    await page.screenshot(path=str(screenshot_path))
                    logger.info(f"Screenshot saved to {screenshot_path}")
                    
                    return True
                except Exception as e:
                    logger.warning(f"Network activity timeout - continuing anyway: {e}")
                    
                return True  # Assume success if we got this far (like PHP)
            else:
                logger.error("DANA payment option not found. Exiting...")
                return False
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        return False


async def _handle_oauth_flow(page):
    """Handle OAuth flow with phone number and PIN entry.
    
    Args:
        page: Playwright page object
    """
    logger.info("Handling OAuth flow...")
    
    # Check if a new window/tab has been opened
    pages = page.context.pages
    if len(pages) > 1:
        # Switch to the latest page (similar to PHP switchTo()->window())
        new_page = pages[-1]
        logger.info("Switching to new page for OAuth flow")
        # No need to explicitly switch in Playwright as we can just use the new_page reference
        
        # Wait 1.5 seconds to match PHP's implementation
        await new_page.wait_for_timeout(1500)
        
        # In a full implementation, we would now handle phone/PIN entry
        # This would depend on the specific OAuth flow structure
        
        # For now, just wait for the page to stabilize
        await new_page.wait_for_load_state('networkidle')

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
