# python3

import asyncio
from playwright.async_api import async_playwright, expect
import pytest

@pytest.mark.asyncio # Mark to run with pytest required with asyncio
async def test_login_succesful():
    async with async_playwright() as playwright:
        # Launch chromium instance non-headless to display the test workflow
        browser = await playwright.chromium.launch(headless=False, slow_mo=300) # remove headless=False for CI/CD
        
        # Open new page from a newly crated context to avoid sharing cookies and cache
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to login website
        await page.goto("http://the-internet.herokuapp.com/login")

        # Fill in username and password, and click the submit button
        await page.get_by_label("username").fill("tomsmith")
        await page.get_by_label("password").fill("SuperSecretPassword!")
        await page.get_by_role("button").click()

        # Locate flash message that appears after login
        flash_message = page.locator("#flash")

        # Assert if the flash message contains succesful test within 5 seconds
        await expect(flash_message).to_contain_text("You logged into a secure area!", timeout=5000)

        await browser.close()

# Uncomment the following line to run the test manually outside pytest
#asyncio.run(test_login_succesful())
