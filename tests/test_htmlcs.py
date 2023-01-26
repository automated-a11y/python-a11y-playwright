import os
from pathlib import Path

from playwright.sync_api import Page

from automateda11y.pw.htmlcsrunner import HtmlCsRunner
from automateda11y.pw.settings import Settings


def root_dir():
    return Path(__file__).parent.parent.__str__()


def test_accessibility_htmlcs(page: Page):
    Settings.report_dir = root_dir() + '/reports'
    page.goto("file://"+root_dir()+"/tests/test.html")
    data = HtmlCsRunner(page).set_standard().set_page_title("Page Title").set_ignore_code([]).execute()
    assert data.errors == 5
