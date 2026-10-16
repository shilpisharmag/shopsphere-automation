import pytest
from pages.saucedemo_page import SauceDemoPage
from data.users import STANDARD_USER
from pathlib import Path
from config.settings import BASE_URL
from api.api_client import APIClient
from config.settings import API_URL
from config.settings import SHOPSPHERE_API_URL
from config.settings import STANDARD_USERNAME,STANDARD_PASSWORD

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
        STANDARD_USERNAME,
        STANDARD_PASSWORD,
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

@pytest.fixture
def api_client():
    return APIClient(
        base_url=API_URL,
        headers={
            "Accept":"application/json"
        })
@pytest.fixture
def shopsphere_api_client():
    return APIClient(
        base_url=SHOPSPHERE_API_URL,
        headers={
            "Accept":"application/json"
        })

@pytest.fixture
def validated_post(api_client):
    response = api_client.get(f"posts/1")
    assert response.status_code == 200
    post = response.json()

    assert post["id"] == 1
    assert isinstance(post["title"], str)
    assert post["title"].strip() != ""
    assert isinstance(post["body"], str)
    assert post["body"].strip() != ""

    return post

@pytest.fixture
def integeration_setup(api_client,authenticated_page):
    return {
        "api_client": api_client,
        "page": authenticated_page
    }

@pytest.fixture
def validated_multi_post(api_client,request):
    post_id = request.param
    response = api_client.get(f"posts/{post_id}")
    post = response.json()
    assert post["id"] == post_id
    assert isinstance(post["title"], str)
    assert post["title"].strip() != ""
    assert isinstance(post["body"], str)
    assert post["body"].strip() != ""

    return post  