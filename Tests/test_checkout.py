import pytest
from Pages.Cartvalidation import CartPage
from Pages.CheckoutTest import CheckoutPage

@pytest.mark.smoke
def test_checkout(logged_in_user):
    cart_page = CartPage(logged_in_user)
    checkout_page = CheckoutPage(logged_in_user)
    cart_page.add_product("Sauce Labs Backpack")
    checkout_page.open_cart()
    checkout_page.validate_page_header("Your Cart")
    checkout_page.click_checkout()
    checkout_page.validate_page_header("Checkout: Your Information")
    checkout_page.fill_first_name("ABC")
    checkout_page.fill_last_name("XYZ")
    checkout_page.fill_pincode("1020")
    checkout_page.click_continue()
    checkout_page.validate_page_header("Checkout: Overview")
    checkout_page.click_finish()
    checkout_page.check_final_status("Thank you for your order!")