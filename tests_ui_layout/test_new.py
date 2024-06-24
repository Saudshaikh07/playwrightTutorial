import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.parametrize("email, password", [("standard_user", "secret_sauce"),
                                             ("problem_user", "secret_sauce"),
                                             ("performance_glitch_user", "secret_sauce")])
def test_sauce_demo_new(page, email, password):
    page.goto("https://www.saucedemo.com/v1/")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user performance_g").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(email)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()
    all_price = page.get_by_text("$").all()

    for price in all_price:
        if '$29.99' in price.text_content():
            print('This is the price for backpack')

    assert page.locator("text=Products").is_visible()