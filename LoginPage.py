from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = "[data-test='username']"
        self.password = "[data-test='password']"
        self.login_btn = "[data-test='login-button']"

    def open(self, url):
        self.page.goto(url)

    def enter_email(self, username):
        self.page.fill(self.username, username, timeout=5000)

    def enter_password(self, password):
        self.page.fill(self.password, password, timeout=5000)

    def click_login(self):
        self.page.click(self.login_btn, timeout=5000)

    def verify_logo(self):
        logo = self.page.locator("text=Swag Labs")
        expect(logo).to_be_visible()
        print("Login successful - Logo visible")