import pytest
from page_object.cart_page import CartPage
from page_object.first_checkout_page import FirstCheckoutPage
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestFirstCheckoutPagePositiveScenarios:
    @pytest.mark.first_checkout
    def test_url_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()
        assert first_checkout_page.current_url == first_checkout_page.expected_url

    @pytest.mark.first_checkout
    def test_cancel_button(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.click_cancel_button()
        assert cart_page.current_url == cart_page.expected_url
