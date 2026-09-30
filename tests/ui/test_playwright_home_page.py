from playwright.sync_api import Page, expect
from pages.playwright_home_page import PlaywrightHomePage


def test_playwright_homepage(page:Page):
    homepage = PlaywrightHomePage(page)
    homepage.open()
    homepage.click_get_started()
    
    expect(page.
           get_by_role("heading",name = "installation")).to_be_visible()
