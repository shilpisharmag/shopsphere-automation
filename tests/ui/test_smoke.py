from playwright.sync_api import Page, expect

def test_playwright_homepage(page:Page):
    page.goto("https://playwright.dev/")
    expect(page.
           get_by_role("link",name = "Playwright logo Playwright")).to_be_visible()
    
    expect(page.
           get_by_role("link",name="Get started")).to_be_visible()
