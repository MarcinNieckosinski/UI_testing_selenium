import pytest
from page_object.cart_page import CartPage
from page_object.first_checkout_page import FirstCheckoutPage
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage
from page_object.second_checkout_page import SecondCheckoutPage


class TestSecondCheckoutPagePositiveScenarios:
    @pytest.mark.second_checkout
    def test_url_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.current_url == second_checkout_page.expected_url

    @pytest.mark.second_checkout
    def test_all_products_in_second_checkout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.get_product_name(1) == "Sauce Labs Backpack"
        assert second_checkout_page.get_product_name(2) == "Sauce Labs Fleece Jacket"
        assert second_checkout_page.get_product_name(3) == "Test.allTheThings() T-Shirt (Red)"

    @pytest.mark.second_checkout
    def test_all_products_description(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.get_product_description(1) == ("carry.allTheThings() with the sleek, streamlined"
                                                                   " Sly Pack that melds uncompromising style with"
                                                                   " unequaled laptop and tablet protection.")
        assert second_checkout_page.get_product_description(2) == ("It's not every day that you come across a midweight"
                                                                   " quarter-zip fleece jacket capable of handling"
                                                                   " everything from a relaxing day outdoors to a busy"
                                                                   " day at the office.")
        assert second_checkout_page.get_product_description(3) == ("This classic Sauce Labs t-shirt is perfect to wear"
                                                                   " when cozying up to your keyboard to automate a few"
                                                                   " tests. Super-soft and comfy ringspun"
                                                                   " combed cotton.")

    @pytest.mark.second_checkout
    def test_all_products_price(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.get_product_price(1) == "$29.99"
        assert second_checkout_page.get_product_price(2) == "$49.99"
        assert second_checkout_page.get_product_price(3) == "$15.99"

    @pytest.mark.second_checkout
    def test_all_products_quantity(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.get_product_quantity(1) == "1"
        assert second_checkout_page.get_product_quantity(2) == "1"
        assert second_checkout_page.get_product_quantity(3) == "1"

    @pytest.mark.second_checkout
    def test_checkout_information(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        first_checkout_page = FirstCheckoutPage(driver)
        second_checkout_page = SecondCheckoutPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.click_checkout_button()

        first_checkout_page.complete_first_name_field("Standard")
        first_checkout_page.complete_last_name_field("User")
        first_checkout_page.complete_zip_postal_code_field("11-111")
        first_checkout_page.click_continue_button()

        assert second_checkout_page.payment_information == "SauceCard #31337"
        assert second_checkout_page.shipping_information == "Free Pony Express Delivery!"
        assert second_checkout_page.item_total == "Item total: $95.97"
        assert second_checkout_page.item_tax == "Tax: $7.68"
        assert second_checkout_page.total_amount == "Total: $103.65"
