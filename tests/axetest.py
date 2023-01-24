from playwright.sync_api import sync_playwright
from automateda11y.axerunner import AxeRunner

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.hotukdeals.com/hot")
    data = AxeRunner(page).execute()
    print(data.browser)
    print(page.title())
    browser.close()
