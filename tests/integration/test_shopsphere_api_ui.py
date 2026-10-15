import pytest
from playwright.sync_api import Page
from config.settings import SHOPSPHERE_UI_URL

@pytest.mark.integration
def test_api_products_match_ui(shopsphere_api_client,page:Page):

    # Step1 : Get products from API
    response = shopsphere_api_client.get("products")
    assert response.status_code == 200
    api_products = response.json()

    # Step2: Open the Shopsphere UI
    page.goto(SHOPSPHERE_UI_URL)

    # Step3: wait until the products appear in the UI
    page.locator(".product").first.wait_for()

    ui_products = page.locator(".product")

    # step4: verify the number of products
    assert ui_products.count() == len(api_products)


    #Step5 :Compare api data with ui data
    for product in api_products:
        ui_product = page.locator(
            f'.product[data-product-id="{product["id"]}"]')
        assert ui_product.count() == 1

        #verify the product name
        ui_name = ui_product.locator("h2").inner_text()
        
        print(product["name"])
        print(ui_name)
        assert ui_name == product["name"]