from pages.saucedemo_page import SauceDemoPage
from pages.saucedemo_product import ProductPage
from pages.saucedemo_cart import CartPage
from config.settings import BASE_URL
from data.users import (
    STANDARD_USER,
    INVALID_USER,
    LOCKED_USER
)

'''
1. Verify exactly 6 products
2. Add Sauce labs Bike light
3. Open cart
4. Verify Bike light is present
'''

def test_addBikelightCart(logged_in_page):
    productpage = ProductPage(logged_in_page)
    cartpage = CartPage(logged_in_page)
    result = productpage.verify_product_count(6)
    if result:
        productitem = ["bike_light"]
        productpage.add_multi_products(productitem)
        productpage.open_cart()
        cartpage.verify_the_badgeCount("1")
        cartpage.verify_bike_light_added()
        

def test_invalidloggedinInvalidUser(page):
    saucedemopage = SauceDemoPage(page)
    saucedemopage.open_sauce_webpage()
    saucedemopage.do_login(INVALID_USER["username"],INVALID_USER["password"])
    saucedemopage.verify_login_error()

def test_lockedoutUser(page):
    saucedemopage = SauceDemoPage(page)
    saucedemopage.open_sauce_webpage()
    saucedemopage.do_login(LOCKED_USER["username"],LOCKED_USER["password"])
    saucedemopage.verify_login_error()

def test_Validcred(page):
    saucedemopage = SauceDemoPage(page)
    saucedemopage.open_sauce_webpage()
    saucedemopage.do_login(STANDARD_USER["username"],STANDARD_USER["password"])
    saucedemopage.verify_login_success()

