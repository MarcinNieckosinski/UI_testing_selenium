import pytest
from page_object.cart_page import CartPage
from page_object.first_checkout_page import FirstCheckoutPage
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestFirstCheckoutPageNegativeScenarios:
    @pytest.mark.first_checkout
    def test_no_data_in_form(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.click_continue_button()
        assert first_checkout_page.error_field_value == "Error: First Name is required"

    @pytest.mark.first_checkout
    def test_no_last_name(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.click_continue_button()
        assert first_checkout_page.error_field_value == "Error: Last Name is required"

    @pytest.mark.first_checkout
    def test_no_zip_code(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.click_continue_button()
        assert first_checkout_page.error_field_value == "Error: Postal Code is required"
