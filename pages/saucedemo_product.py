from playwright.sync_api import Page,expect

class ProductPage:
    def __init__(self,page:Page):
        self.page = page
        self.product_title = self.page.get_by_text("Products")
        #self.backpack = self.page.get_by_role("button",name = "Add to cart", exact=True)
        self.backpack = self.page.locator('[data-test = "add-to-cart-sauce-labs-backpack"]')
        # self.bike_light = self.page.locator('[data-test = "add-to-cart-sauce-labs-bike-light"]')
        # self.bolt_tshirt = self.page.locator('[data-test = "add-to-cart-sauce-labs-bolt-t-shirt"]')
        # self.fleece_jacket =self.page.locator('[data-test = "add-to-cart-sauce-labs-fleece-jacket]')
        self.prodcuts = self.page.locator(".inventory_item")
        self.product_items = { 
            "backpack" : self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]'),
            "bike_light" : self.page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]'),
            "bolt_tshirt" : self.page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'),
            "one_sie" : self.page.locator('[data-test="add-to-cart-sauce-labs-onesie"]'),
            "tshirt_red": self.page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

        }
        

        self.cart_link = self.page.locator('[data-test = "shopping-cart-link"]')

    def verify_product_page(self):
        expect(self.product_title).to_be_visible()

    def add_first_product(self):
        print("Adding first product")
        self.backpack.click()

    def open_cart(self):
        self.cart_link.click()

    def add_multi_products(self, product_keys: list[str]):
        for key in product_keys:
            self.product_items[key].click()

    def verify_product_count(self, expected_count:int):
        expect(self.prodcuts).to_have_count(expected_count)

