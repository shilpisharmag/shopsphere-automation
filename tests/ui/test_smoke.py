from playwright.sync_api import Page, expect

# Scenario: Verify the Playwright homepage loads with the logo and Get started link visible.
def test_playwright_homepage(page:Page):
    page.goto("https://playwright.dev/")
    expect(page.
           get_by_role("link",name = "Playwright logo Playwright")).to_be_visible()
    
    expect(page.
           get_by_role("link",name="Get started")).to_be_visible()
