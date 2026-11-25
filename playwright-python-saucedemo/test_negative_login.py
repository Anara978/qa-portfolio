from playwright.sync_api import Page, expect


def test_invalid_password(page: Page) -> None:  # Define a test function that uses a browser page
    page.goto("https://www.saucedemo.com/")  # Open the Sauce Demo website
    page.locator("[data-test=\"username\"]").click()  # Locate and click the username field
    page.locator("[data-test=\"username\"]").fill("error_user")  # Enter the username
    page.locator("[data-test=\"password\"]").click()  # Click the password field
    page.locator("[data-test=\"password\"]").fill("12345")  # Enter an incorrect password
    page.locator("[data-test=\"login-button\"]").click()  # Click the login button
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()  # Verify that the error message is visible
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")  # Verify that the error message contains the expected text
