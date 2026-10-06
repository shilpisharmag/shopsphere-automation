import pytest
from pages.saucedemo_page import SauceDemoPage

@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login("standard_user","secret_sauce")
    login_page.verify_login_success()

@pytest.mark.ui
def test_invalid_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login("wrong user","wrong password")
    login_page.verify_login_error()

@pytest.mark.ui
def test_locked_user_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login("locked_out_user","secret_sauce")
    login_page.verify_login_error()