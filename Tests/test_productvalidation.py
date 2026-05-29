import pytest
from Pages.ProductValidation import ProductPage
from Utilities.excel_utils import access_products,access_prices
from Utilities.Logger import get_logger
from Utilities.read_properties import ReadConfig

logger = get_logger()


@pytest.mark.smoke
def test_product_count_validation(logged_in_user):

    product_page = ProductPage(logged_in_user)
    logger.info("Starting product count validation")
    product_count = product_page.return_product_count()
    assert product_count == 6,\
    f"Expected count: 6 whereas Product count: {product_count}"


def test_product_name_validation(logged_in_user):

    product_page = ProductPage(logged_in_user)
    logger.info("Starting product name validation")
    actual_product_names = product_page.validate_product_names()
    excel_products = access_products(ReadConfig.get_file_path(),
                                     "ProductNames")
    assert actual_product_names == excel_products, "Product names mismatch!"


def test_product_price_validation(logged_in_user):

    product_page = ProductPage(logged_in_user)
    logger.info("Starting product price validation")
    actual_product_prices = product_page.validate_product_prices()
    expected_prices = access_prices(ReadConfig.get_file_path(),
                                     "ProductPrices")
    assert actual_product_prices == expected_prices, "Product prices mismatch!"
