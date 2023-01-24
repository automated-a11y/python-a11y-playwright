from playwright.sync_api import sync_playwright
from automateda11y.htmlcsrunner import HtmlCsRunner

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    data = HtmlCsRunner(page).execute()
    print(data.notices)
    print(page.title())
    browser.close()
