import pytest
from Pages.Cartvalidation import CartPage

@pytest.mark.parametrize(
    "products, expected_count",
    [
        (["Sauce Labs Backpack"], 1),
        (
                [
                    "Sauce Labs Bagpack",
                    "Sauce Labs Bike Light"
                ], 2
        )
    ]
)

def test_validate_cart_functionality(logged_in_user, products, expected_count):
    cart_page = CartPage(logged_in_user)
    for product in products:
        cart_page.add_product(product)

    cart_page.validate_cart_count(expected_count)

