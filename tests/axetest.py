from pathlib import Path

from playwright.sync_api import sync_playwright
from automateda11y.pw.axerunner import AxeRunner
from automateda11y.pw.settings import Settings


def root_dir():
    return Path(__file__).parent.parent.__str__()


with sync_playwright() as p:
    Settings.report_dir = root_dir() + '/reports'
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.hotukdeals.com/hot")
    data = AxeRunner(page).execute()
    print(data.browser)
    print(page.title())
    browser.close()
