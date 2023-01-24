## Accessibility Automation for Web Apps with Python and [Playwright](https://playwright.dev/).

### This project uses [HTML CodeSniffer](https://squizlabs.github.io/HTML_CodeSniffer/) and [Deque Axe](https://www.deque.com/)

**HTML CodeSniffer** : checks HTML source code and detects any Accessibility violations. Comes with standards that cover
the three (A, AA & AAA) conformance levels of the W3C's Web Content Accessibility Guidelines (WCAG) 2.1 and the U.S.
Section 508 legislation.

**Deque Axe** : World’s leading digital accessibility toolkit. Powerful and accurate accessibility toolkit can get you
to 80% issue coverage, or more, during development.

### Features

1. Simple & Easy to use
2. No need of prior knowledge on Accessibility
3. Works with Python [Playwright](https://playwright.dev/)
4. Rich Reporting
5. Open source

### Installation

For maven based project add the below dependency

```
pip install -i https://test.pypi.org/simple/ python-a11y-playwright
```
### Getting Started

#### Using HTML CodeSniffer

Below is the example usage using HTML CodeSniffer.

```python
from pathlib import Path

from automateda11y.settings import Settings
from playwright.sync_api import sync_playwright
from automateda11y.htmlcsrunner import HtmlCsRunner


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

from automateda11y.settings import Settings
from playwright.sync_api import sync_playwright
from automateda11y.axerunner import AxeRunner


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

