# SauceDemo UI Test Automation — Python & Playwright

A hands-on training project from Portnov Computer School, practicing browser automation on the public [SauceDemo](https://www.saucedemo.com/) demo application.

## Test coverage

| File | Purpose |
| --- | --- |
| `test_login.py` | Valid login; verifies the Products text is visible |
| `test_negative_login.py` | Invalid password; verifies error visibility and expected error text |
| `test_add_to_cart.py` | Adds Sauce Labs Backpack, checks cart indicator and verifies product name in cart |
| `test_firstcase.py` | Initial Codegen login exercise; records actions without an explicit assertion |
| `test_setup.py` | Browser setup smoke check against Google |

## Skills practiced

- Playwright Codegen, Python synchronous API and pytest fixtures
- CSS selectors, placeholder, role, text and custom test ID locators
- Positive and negative UI scenarios, assertions, headed and headless execution

SauceDemo uses `data-test` rather than Playwright's default `data-testid`. The login test configures the custom attribute.

## Run locally

From this project directory, with Python installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

To watch a test in the browser:

```bash
python -m pytest test_login.py --headed
```

## Recorded result

November 25, 2026 — original coursework rerun on macOS, Python 3.15.2, pytest 8.3.4, Playwright 1.50.0, Chromium: **5 passed, 0 failed (3.45 seconds)**.

This portfolio copy uses descriptive function names and minor comment/import cleanup; test actions and assertions are preserved. The five passing executions include three functional tests, one recorded login exercise without an assertion, and one setup check. No CI or cross-browser execution is claimed.

Credentials in these tests are public SauceDemo demo credentials, not personal account credentials.
