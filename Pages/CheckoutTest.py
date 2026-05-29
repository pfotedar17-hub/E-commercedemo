from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_icon = (By.XPATH,"//span[@class='shopping_cart_badge']")
        self.cart_item = (By.XPATH,"//div[@class = 'inventory_item_name']")
        self.checkout_button = (By.ID,"checkout")
        self.header_info = (By.XPATH,"//*[@id='header_container']/div[2]/span")
        self.first_name = (By.ID,"first-name")
        self.last_name = (By.ID,"last-name")
        self.pincode = (By.ID,"postal-code")
        self.continue_button = (By.ID,"continue")
        self.finish_button = (By.ID,"finish")
        self.confirm_text = (By.XPATH,"//h2[@class='complete-header']")


    def open_cart(self):

        self.click(self.cart_icon)


    def click_checkout(self):

        self.click(self.checkout_button)


    def validate_page_header(self, expected_text):

        self.validate_page(self.header_info, expected_text)


    def fill_first_name(self, firstname):

        self.enter_text(self.first_name, firstname)


    def fill_last_name(self, lastname):

        self.enter_text(self.last_name, lastname)


    def fill_pincode(self, pin):

        self.enter_text(self.pincode, pin)

    def click_continue(self):

        self.click(self.continue_button)


    def click_finish(self):

        self.click(self.finish_button)


    def check_final_status(self, expected_text):
        self.validate_text(self.confirm_text, expected_text)








