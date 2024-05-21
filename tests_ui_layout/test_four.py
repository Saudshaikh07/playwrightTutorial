from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_elements import HomePage
import pytest


@pytest.mark.integration
def test_about_us_section(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    page.get_by_role("button", name="Shop Now").click()
    print("Test Passed")


@pytest.mark.regression
def test_about_us_section_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    assert page.is_visible("text=faketext")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    page.get_by_role("button", name="Shop Now").click()
    print("Test Passed")

    # ---------------------
    context.close()
    browser.close()
