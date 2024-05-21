import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.smoke
def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Login")).to_be_hidden()

    assert page.is_visible("text=Dashboard")  # Dashboard page
    print("Test Passed!!!")
    # ---------------------
    context.close()
    browser.close()