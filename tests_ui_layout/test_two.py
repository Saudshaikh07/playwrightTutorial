import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture
def test_flipkart(set_up):
    page = set_up
    page.goto("https://www.flipkart.com/")
    # page.goto("https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_1f1bff70-a25b-4acb-8682-f74505e59873_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J")
    # page.wait_for_load_state("networkidle")
    # product_value = page.locator('xpath=//*[@id="container"]/div/div[3]/div[3]/div[2]/div[14]/div/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/div[3]/div/div[1]').text_content()
    # print(product_value)

    # ---------------------