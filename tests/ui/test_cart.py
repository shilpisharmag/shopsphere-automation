import pytest
from pages.saucedemo_page import SauceDemoPage
from pages.saucedemo_product import ProductPage
from pages.saucedemo_cart import CartPage
import test_products

@pytest.mark.smoke
@pytest.mark.ui
def test_add_backpack_Verify_cart(logged_in_page):
    
    # #Login
    # login_page = SauceDemoPage(page)
    # login_page.open_sauce_webpage()
    # login_page.do_login("standard_user","secret_sauce")

    #Product
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()

    product_page.add_first_product()
    product_page.open_cart()

    #cart
    cart_page = CartPage(logged_in_page)
    cart_page.verify_backpack_added()
   

@pytest.mark.ui
def test_check_the_badgecount_multiple_itme(logged_in_page):
    # adding multiple products

    product_items = ["backpack","bike_light","bolt_tshirt","one_sie","tshirt_red"]
    product_page = ProductPage(logged_in_page)
    product_page.verify_product_page()
    product_page.add_multi_products(product_items)

    cart_page = CartPage(logged_in_page)
    cart_page.verify_the_badgeCount(str(len(product_items)))
    product_page.open_cart()
    cart_page.verify_the_cartItem("backpack")
    # cart_page.verify_the_cartItem("backpackss") # failure case

@pytest.mark.ui
def test_add_RemoveProduct(logged_in_page):

    product_page = ProductPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    product_page.verify_product_page()
    
    product_page.add_first_product()
    product_page.open_cart()
    cart_page.verify_the_cartItem("backpack")
    cart_page.removeProduct_fromCart()






