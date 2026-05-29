from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.shopping_cart_badge = (By.XPATH,"//span[@class='shopping_cart_badge']")
        self.shopping_list = (By.XPATH,"//div[@class='inventory_item']")


    def add_product(self, product_name):
        self.add_product_to_cart(self.shopping_list, product_name)


    def validate_cart_count(self, expected_count):
        self.get_cart_count(self.shopping_cart_badge, expected_count)


    def remove_product(self, product_name):
        self.remove_product_from_cart(self.shopping_list, product_name)





