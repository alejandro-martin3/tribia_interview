# QA Automation Engineer Technical Case

Summary of Fixes and Optimizations:
- Used async with async_playwright() as indicated in playwright's documentation, this ensures automatically stopping playwright when the script completes, therefore also removed the "await playwright.stop()" statement.
- (Optional) headless=False state with an appropiate slow_mo value shows the full test worflow which is useful for debugging but must be removed for CI/CD.
- (Also optional) creating a new context ensures isolation of cookies and cache.
- Locators for both text fields and submit button used discouraged format "page.fill(), page.click()". Fixed to modern format "page.locator.fill(), page.locator.click()".
- Corrected the text fields labels from #user/#pass to #username/#password.
- Instead of using a static timeout (wait_for_timeout(5000)), implemented an actual assertion with expect while maintaining the same timeout.
