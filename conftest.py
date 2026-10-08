import pytest
from pages.saucedemo_page import SauceDemoPage
from data.users import STANDARD_USER
from pathlib import Path
from config.settings import BASE_URL

AUTH_FILE= Path("playwright/.auth/user.json")
# AUTH_FILE = (
#     Path(__file__).parent
#     / "playwright"
#     / ".auth"
#     / "user.json"
# )

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "Test@123"
    }

@pytest.fixture
def logged_in_page(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login(
        STANDARD_USER["username"],
        STANDARD_USER["password"],
    )

    login_page.verify_login_success()
    return page

@pytest.fixture
def authenticated_page(browser):
    print(f"\nAuth file: {AUTH_FILE}")
    print(f"\nAuth file exist:{AUTH_FILE.exists()}")

    context = browser.new_context(storage_state = str(AUTH_FILE))
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")

    print(f"DEBUG: landed on {page.url}")   # temporary
    yield page
    context.close()
