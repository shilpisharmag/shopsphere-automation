from playwright.sync_api import Page,expect
from pages.saucedemo_product import ProductPage

class CartPage:
    def __init__(self,page:Page):

        self.page = page
        self.backpack = self.page.get_by_text("Sauce Labs Backpack")
        self.badge = self.page.locator('[data-test="shopping-cart-badge"]')
        self.removeBackpack = self.page.locator('[data-test="remove-sauce-labs-backpack"]')
        

    def verify_backpack_added(self):
        expect(self.backpack).to_be_visible()

    def verify_the_badgeCount(self,count:str):
         expect(self.badge).to_have_text(count)

    def verify_the_cartItem(self,name:str):
        # productpage = ProductPage()
        # key = productpage.product_items[name]

        expect(self.page.get_by_text(f'{name}')).to_be_visible()

    def removeProduct_fromCart(self):
        # productpage = ProductPage()
        # productpage.add_first_product()
        # productpage.open_cart()
        # self.verify_backpack_added()
        self.removeBackpack.click()
        expect(self.page.get_by_text("backpack")).not_to_be_visible()
