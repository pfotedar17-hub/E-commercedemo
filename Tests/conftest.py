import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.LoginTest import LoginPage
from Utilities.screenshot import capture_screenshot

@pytest.fixture
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture()
def logged_in_user(driver):

    LP = LoginPage(driver)
    LP.open_url("https://www.saucedemo.com/")
    LP.enter_username("standard_user")
    LP.enter_password("secret_sauce")
    LP.click_login()
    LP.validate_login("Swag Labs")
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            capture_screenshot(driver,item.name)
