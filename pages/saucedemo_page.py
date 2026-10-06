from playwright.sync_api import Page,expect
from config.settings import BASE_URL

class SauceDemoPage:
    def __init__(self,page:Page):
        self.page = page
        self.url = BASE_URL
        # self.username = "standard_user"
        # self.password = "secret_sauce"
        self.usernamefield = self.page.get_by_placeholder("Username")
        self.passwordifeld = self.page.get_by_placeholder("Password")
        self.loginbutton = self.page.get_by_role("button", name = "Login")
        self.errorMessage = page.locator('[data-test="error"]')


    def open_sauce_webpage(self):
        self.page.goto(self.url)

    def do_login(self,username,password):
        self.usernamefield.click()
        self.usernamefield.fill(username)
        self.passwordifeld.click()
        self.passwordifeld.fill(password)
        self.loginbutton.click()

    def verify_login_success(self):
        expect(self.page.get_by_text("Products")).to_be_visible()

    def verify_login_error(self):
        expect(self.errorMessage).to_be_visible()
     

    




    