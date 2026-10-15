import pytest
from pages.saucedemo_product import ProductPage
from pages.saucedemo_cart import CartPage

@pytest.mark.integeration
def test_api_ui_smoke(api_client,authenticated_page):
    #Part1 : API validation

    api_response = api_client.get("posts/1")
    assert api_response.status_code == 200

    api_data = api_response.json()
    assert api_data["body"] != ""
    assert api_data["id"] == 1
    assert api_data["userId"] == 1
    assert api_data["title"] != ""

    assert isinstance(api_data["body"],str)

    #Part2 : UI validation

    productpage = ProductPage(authenticated_page)
    cartpage = CartPage(authenticated_page)
    productpage.verify_product_page()
    productpage.add_first_product()
    productpage.open_cart()
    cartpage.verify_backpack_added()
    cartpage.verify_backpack_count(1)

@pytest.mark.integeration
def test_api_ui_smoke2(integeration_setup):
    api_client = integeration_setup["api_client"]
    page = integeration_setup["page"]

    res = api_client.get("posts/1")
    assert res.status_code == 200
    
    api_data = res.json()
    assert api_data["body"] != ""
    assert api_data["id"] == 1
    assert api_data["userId"] == 1
    assert api_data["title"] != ""
    
    assert isinstance(api_data["body"],str)

    productpage = ProductPage(page)
    cartpage = CartPage(page)
    productpage.verify_product_page()
    productpage.add_first_product()
    productpage.open_cart()
    cartpage.verify_backpack_added()
    cartpage.verify_backpack_count(1)