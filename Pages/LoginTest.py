from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    def  __init__(self, driver):
        super().__init__(driver)
        self.username_textbox = (By.ID,'user-name')
        self.password_textbox = (By.ID,'password')
        self.login_button = (By.ID,'login-button')
        self.actual_text = (By.XPATH,"//div[@class='app_logo']")
        self.error = (By.XPATH,"//h3[@data-test='error']")

    def open_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(self.username_textbox, username)

    def enter_password(self, password):
        self.enter_text(self.password_textbox, password)

    def click_login(self):
        self.click(self.login_button)

    def validate_login(self, expected_text):
        self.validate_text(self.actual_text, expected_text)

    def validate_error(self, error_text):
        self.validate_text(self.error, error_text)
