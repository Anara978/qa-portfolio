from playwright.sync_api import Page

def test_playwright_setup(page: Page):
    page.goto("https://www.google.com")
    assert page.title() == "Google"
