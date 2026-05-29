import pytest
from Pages.LoginTest import LoginPage
from Utilities.Logger import get_logger
from Utilities.read_properties import ReadConfig

logger = get_logger()

@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        (
                "standard_user", "secret_sauce", "Swag Labs"  # Valid Login
        ),

        (
                "standard_user", "secret_sauc", "Epic sadface: Username and password do not match any user in this service" # Invalid Login
        ),

        (
                "", "secret_sauce", "Epic sadface: Username is required"  # No username login
        ),

        (
                "standard_user", "", "Epic sadface: Password is required"    # No password login
        ),

        (
                "locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."    # locked user Login
        )
    ]
)


def test_login_validation(driver, username, password, expected_result):

    login_page = LoginPage(driver)
    logger.info("Starting Login Test")

    login_page.open_url(ReadConfig.get_application_url())
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if expected_result == "Swag Labs":

        logger.info("Validating successful login")
        login_page.validate_login(expected_result)

    else:

        logger.info("Validating login error message")
        login_page.validate_error(expected_result)



