from playwright.sync_api import sync_playwright

print("Playwright automation started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle")

    print("If CAPTCHA appears, please solve it manually...")
    page.wait_for_timeout(15000)  # Manual CAPTCHA window

    page.fill("textarea[name='q']", "India vs New Zealand match status")
    page.keyboard.press("Enter")

    page.wait_for_load_state("networkidle")

    page.locator("h3").first.click()
    page.wait_for_timeout(5000)

    print("Page title:", page.title())

    browser.close()

print("Playwright automation completed")
