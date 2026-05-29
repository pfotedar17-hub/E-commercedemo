from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Utilities.Logger import get_logger


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger()


    def click(self, locator):
        self.logger.info(f"Finding and clicking {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def enter_text(self, locator, text):
        self.logger.info(f"Finding {locator} and entering {text}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)


    def get_text(self, locator):

        self.logger.info(f"Retrieving text from {locator} ")
        return self.wait.until(EC.visibility_of_element_located(locator)).text


    def validate_text(self, locator, expected_text):

        actual_text = self.get_text(locator)
        self.logger.info(f"Text fetched from {locator}")
        self.logger.info(f"Comparing {actual_text} with {expected_text}")
        assert actual_text == expected_text, \
            f"Mismatch with {actual_text}"

    def validate_element_text(self, locator, expected_text):

        self.logger.info(f"Waiting for text '{expected_text}' to be present in element {locator}")

        text_present = self.wait.until(EC.text_to_be_present_in_element(locator, expected_text))
        self.logger.info(f"Validation result for {locator}: {text_present}")

        assert text_present, \
            f"Expected text '{expected_text}' not found"

        self.logger.info(f"Successfully validated text '{expected_text}'")

    def get_cart_count(self, locator, expected_count):

        self.logger.info(f"Waiting for cart count to become {expected_count}")

        self.wait.until(EC.text_to_be_present_in_element(locator, str(expected_count)))
        count = self.get_text(locator)

        self.logger.info(f"Cart count fetched: {count}")
        self.logger.info(f"Comparing actual count {count} with expected count {expected_count}")

        assert int(count) == expected_count, \
            f"Expected cart count {expected_count} but got {count}"

        self.logger.info("Cart count validation successful")

    def add_product_to_cart(self, locator, product_name):

        self.logger.info(f"Searching for product '{product_name}'")

        all_products = self.wait.until(EC.visibility_of_all_elements_located(locator))

        for product in all_products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

            self.logger.info(f"Checking product: {name}")

            if name == product_name:
                self.logger.info(f"Adding product '{product_name}' to cart")

                product.find_element(By.TAG_NAME, "button").click()

                self.logger.info(f"Successfully added '{product_name}' to cart")
                break

    def remove_product_from_cart(self, locator, product_name):

        self.logger.info(f"Searching for product '{product_name}' to remove")

        products = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

        for product in products:

            name = product.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            self.logger.info(f"Checking product: {name}")

            if name == product_name:
                self.logger.info(
                    f"Removing product '{product_name}' from cart"
                )

                product.find_element(By.TAG_NAME, "button").click()

                self.logger.info(
                    f"Successfully removed '{product_name}' from cart"
                )

                break

    def validate_page(self, locator, expected_page):

        self.logger.info(
            f"Waiting for page text '{expected_page}' in {locator}"
        )

        self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_page)
        )

        actual_text = self.driver.find_element(*locator).text

        self.logger.info(f"Actual page text: {actual_text}")
        self.logger.info(
            f"Comparing actual page '{actual_text}' with expected '{expected_page}'"
        )

        assert actual_text == expected_page, \
            f"Expected page '{expected_page}' but got '{actual_text}'"

        self.logger.info("Page validation successful")

    def get_product_names(self, locator):

        self.logger.info(f"Fetching all product names from {locator}")

        products = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

        product_list = [product.text for product in products]

        self.logger.info(f"Product names fetched: {product_list}")

        return product_list

    def get_product_count(self, locator):

        self.logger.info(f"Fetching product count from {locator}")

        products = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

        count = len(products)

        self.logger.info(f"Total products found: {count}")

        return count

    def get_product_prices(self, locator):

        self.logger.info(f"Fetching product prices from {locator}")

        products = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

        price_list = [
            product.text.replace("$", "")
            for product in products
        ]

        self.logger.info(f"Prices fetched: {price_list}")

        return price_list