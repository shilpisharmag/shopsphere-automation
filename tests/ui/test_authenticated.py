
import pytest
from pages.saucedemo_product import ProductPage

@pytest.mark.ui
def test_authenticated_user_can_access_products(authenticated_page):

    productpage = ProductPage(authenticated_page)
    productpage.verify_product_page()
