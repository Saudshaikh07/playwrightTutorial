from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_elements import HomePage
import pytest


@pytest.mark.integration
@pytest.fixture
def test_about_us_section(set_up):
    page = set_up
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    page.get_by_role("button", name="Shop Now").click()
    print("Test Passed")


@pytest.mark.regression
@pytest.fixture
def test_about_us_section_2(set_up):
    page = set_up
    assert not page.is_visible("text=faketext")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    page.get_by_role("button", name="Shop Now").click()
    print("Test Passed")

    # ---------------------
