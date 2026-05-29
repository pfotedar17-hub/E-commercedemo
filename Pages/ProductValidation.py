from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.inventory_item_names = (By.CLASS_NAME, "inventory_item_name")
        self.inventory_item_price = (By.CLASS_NAME, "inventory_item_price")

    def return_product_count(self):
        product_count = self.get_product_count(self.inventory_items)
        return product_count

    def validate_product_names(self):
        product_names = self.get_product_names(self.inventory_item_names)
        return product_names

    def validate_product_prices(self):
        product_prices = self.get_product_prices(self.inventory_item_price)
        return product_prices