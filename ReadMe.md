## Accessibility Automation for Web Apps with Python and [Playwright](https://playwright.dev/).

### This project uses [HTML CodeSniffer](https://squizlabs.github.io/HTML_CodeSniffer/) and [Deque Axe](https://www.deque.com/)

**HTML CodeSniffer** : checks HTML source code and detects any Accessibility violations. Comes with standards that cover
the three (A, AA & AAA) conformance levels of the W3C's Web Content Accessibility Guidelines (WCAG) 2.1 and the U.S.
Section 508 legislation.

**Deque Axe** : World’s leading digital accessibility toolkit. Powerful and accurate accessibility toolkit can get you
to 80% issue coverage, or more, during development.

[![Python badge](https://img.shields.io/badge/python-3.10-green.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/python-a11y-playwright.svg)](https://badge.fury.io/py/python-a11y-playwright)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/52674c845fa54bc5afafd9b4ce960503)](https://www.codacy.com/gh/automated-a11y/python-a11y-playwright/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=automated-a11y/python-a11y-playwright&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/52674c845fa54bc5afafd9b4ce960503)](https://www.codacy.com/gh/automated-a11y/python-a11y-playwright/dashboard?utm_source=github.com&utm_medium=referral&utm_content=automated-a11y/python-a11y-playwright&utm_campaign=Badge_Coverage)
[![License badge](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Contributer badge](https://img.shields.io/github/contributors/automated-a11y/java-a11y-playwright.svg)](https://github.com/automated-a11y/java-a11y-playwright/graphs/contributors)

### Features

1. Simple & Easy to use
2. No need of prior knowledge on Accessibility
3. Works with Python [Playwright](https://playwright.dev/)
4. Rich Reporting
5. Open source

### Installation

For maven based project add the below dependency

```
pip install python-a11y-playwright
```
### Getting Started

#### Using HTML CodeSniffer

Below is the example usage using HTML CodeSniffer.

```python
from pathlib import Path

from automateda11y.pw.settings import Settings
from playwright.sync_api import sync_playwright
from automateda11y.pw.htmlcsrunner import HtmlCsRunner


def json_reports_dir():
    return Path(__file__).parent.parent.__str__()


with sync_playwright() as p:
    Settings.report_dir = json_reports_dir() + '/reports'
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    data = HtmlCsRunner(page).execute()
    browser.close()
```

#### Using Deque Axe

Below is the example usage using Deque Axe.

```python
from pathlib import Path

from automateda11y.pw.settings import Settings
from playwright.sync_api import sync_playwright
from automateda11y.pw.axerunner import AxeRunner


def json_reports_dir():
    return Path(__file__).parent.parent.__str__()


with sync_playwright() as p:
    Settings.report_dir = json_reports_dir() + '/reports'
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    data = AxeRunner(page).execute()
    browser.close()
```

