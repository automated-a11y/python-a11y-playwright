from pathlib import Path

from playwright.sync_api import Page

from automateda11y.pw.axerunner import AxeRunner
from automateda11y.pw.settings import Settings


def root_dir():
    return Path(__file__).parent.parent.__str__()


def test_accessibility_axe(page: Page):
    Settings.report_dir = root_dir() + '/reports'
    page.goto("file://"+root_dir()+"/tests/test.html")
    data = AxeRunner(page).set_page_title("Page Title").execute()
    assert len(data.violations) == 2
