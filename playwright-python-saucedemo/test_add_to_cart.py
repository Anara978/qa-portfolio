from playwright.sync_api import Page, expect


def test_add_backpack_to_cart(page: Page) -> None:  # Define a test function that uses a browser page
    page.goto("https://www.saucedemo.com/")  # Open the Sauce Demo website
    page.locator("[data-test=\"username\"]").click()  # Locate and click the username field
    page.locator("[data-test=\"username\"]").fill("standard_user")  # Enter the username
    page.locator("[data-test=\"password\"]").click()  # Click the password field
    page.locator("[data-test=\"password\"]").fill("secret_sauce")  # Enter the correct password
    page.locator("[data-test=\"login-button\"]").click()  # Click the login button
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()  # Add the backpack to the cart
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")  # Verify that the cart contains one item
    page.locator("[data-test=\"shopping-cart-link\"]").click()  # Open the shopping cart
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")  # Verify that the backpack is in the cart
