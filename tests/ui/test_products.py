from pages.saucedemo_page import SauceDemoPage
from pages.saucedemo_product import ProductPage
import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_add_product_tocart(logged_in_page):
    # login_page = SauceDemoPage(page)
    # login_page.open_sauce_webpage()
    # login_page.do_login("standard_user","secret_sauce")


    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()
    product_page.add_first_product()
    product_page.open_cart()

product_items = ["backpack","bike_light","bolt_tshirt","one_sie","tshirt_red"]

@pytest.mark.ui
def test_add_multiple_prodcut_tocart(logged_in_page):
    product_items = ["backpack","bike_light","bolt_tshirt","one_sie","tshirt_red"]
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()
    product_page.add_multi_products(product_items)


pytest.mark.ui
pytest.mark.smoke
def test_verify_productCount(logged_in_page):
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_count(6)



 