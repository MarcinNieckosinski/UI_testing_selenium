import pytest
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestLoginNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error", [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("non_existing_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this "
                                              "service"),
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service")
    ])
    def test_negative_login(self, driver, username, password, expected_error):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login(username, password)

        assert login_page.get_error_message() == expected_error
        assert inventory_page.current_url != inventory_page.expected_url
