import pytest
from page_object.cart_page import CartPage
from page_object.checkout_complete_page import CheckoutCompletePage
from page_object.first_checkout_page import FirstCheckoutPage
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage
from page_object.second_checkout_page import SecondCheckoutPage


class TestCheckoutCompletePagePositiveScenarios:
    @pytest.mark.checkout_complete
    def test_url_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        second_checkout_page.click_finish_button()

        assert checkout_complete_page.current_url == checkout_complete_page.expected_url

    @pytest.mark.checkout_complete
    def test_thank_you_visibility(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        second_checkout_page.click_finish_button()

        assert checkout_complete_page.thank_you_header_text == "Thank you for your order!"
        assert checkout_complete_page.thank_you_text == ("Your order has been dispatched, and will arrive just as"
                                                         " fast as the pony can get there!")

    @pytest.mark.checkout_complete
    def test_back_home_button(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        second_checkout_page.click_finish_button()

        checkout_complete_page.click_back_home_button()
        assert inventory_page.current_url == inventory_page.expected_url
