'''
Authenticated user
    ||
Products
    ||
Add Backpack
    ||
Cart
    ||
Verify checkout

'''

from pages.saucedemo_product import ProductPage
from pages.saucedemo_cart import CartPage

def test_checkout1(authenticated_page):
    productpage = ProductPage(authenticated_page)
    cartpage = CartPage(authenticated_page)
    productpage.add_first_product()
    productpage.open_cart()
    cartpage.verify_backpack_added()
    cartpage.checkout()

