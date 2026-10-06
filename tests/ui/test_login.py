import pytest
from pages.saucedemo_page import SauceDemoPage
from data.users import (
    STANDARD_USER,
    INVALID_USER,
    LOCKED_USER
)

@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )
    login_page.verify_login_success()

@pytest.mark.ui
def test_invalid_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login(INVALID_USER["username"],INVALID_USER["password"])
    login_page.verify_login_error()

@pytest.mark.ui
def test_locked_user_login(page):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login(LOCKED_USER["username"],LOCKED_USER["password"])
    login_page.verify_login_error()


@pytest.mark.ui
@pytest.mark.parametrize("username,password",
                         [("wrong_user","wrong_password"),
                          ("invalid_user","invalid_password"),
                          ("","")])
def test_invalids_login(page,username,password):
    login_page = SauceDemoPage(page)
    login_page.open_sauce_webpage()
    login_page.do_login(username,password)
    login_page.verify_login_error()