import pytest
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestLoginPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.parametrize("username, password", [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
        ("visual_user", "secret_sauce")])
    def test_positive_login(self, driver, username, password):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login(username, password)

        assert inventory_page.current_url == inventory_page.expected_url
        assert inventory_page.is_cart_button_displayed()
        assert inventory_page.is_menu_button_displayed()
