from playwright.sync_api import Page, expect


def test_valid_login(page: Page, playwright) -> None:
    page.goto("https://www.saucedemo.com/")
    playwright.selectors.set_test_id_attribute("data-test")  # Configure the custom test ID attribute
    page.locator("[data-test=\"username\"]").click()
    page.get_by_placeholder("Username").fill("standard_user")  # Locate the username field by placeholder
    page.get_by_test_id("password").click()  # Locate the password field by test ID
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()  # Locate and click the login button by role
    expect(page.get_by_text("Products", exact=True)).to_be_visible()  # Verify that the Products text is visible
