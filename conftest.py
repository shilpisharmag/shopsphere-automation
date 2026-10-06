import pytest
from pages.saucedemo_page import SauceDemoPage
from data.users import STANDARD_USER

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