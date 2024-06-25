import os

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD

@pytest.mark.parametrize("email, password", [("standard_user", "secret_sauce"),
                                             ("problem_user", "secret_sauce")])
def test_sauce_demo(set_up, email, password):
    page = set_up
    page.goto("https://www.saucedemo.com/v1/")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user performance_g").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(email)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(PASSWORD)
    page.get_by_role("button", name="LOGIN").click()
    all_price = page.get_by_text("$").all()

    for price in all_price:
        if '$29.99' in price.text_content():
            print('This is the price for backpack')

    # Difference between assert and expect
    # value = page.get_by_text("© 2020 Sauce Labs. All Rights").is_hidden()
    # value = expect(page.locator("text=© 2020 Sauce Labs. All Rights")).to_be_visible()

    # #Waits
    # page.wait_for_load_state()
    # assert page.is_visible('//*[@id="inventory_filter_container"]/div')

    # ---------------------
