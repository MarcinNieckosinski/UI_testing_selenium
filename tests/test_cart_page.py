import pytest
from page_object.cart_page import CartPage
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestCartPagePositiveScenarios:
    @pytest.mark.cart
    def test_all_products_in_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        assert cart_page.current_url == cart_page.expected_url
        assert cart_page.get_product_name(1) == "Sauce Labs Backpack"
        assert cart_page.get_product_name(2) == "Sauce Labs Fleece Jacket"
        assert cart_page.get_product_name(3) == "Test.allTheThings() T-Shirt (Red)"

    @pytest.mark.cart
    def test_all_descriptions_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        assert cart_page.get_product_description(1) == ("carry.allTheThings() with the sleek, streamlined Sly Pack"
                                                        " that melds uncompromising style with unequaled laptop and"
                                                        " tablet protection.")
        assert cart_page.get_product_description(2) == ("It's not every day that you come across a midweight"
                                                        " quarter-zip fleece jacket capable of handling everything"
                                                        " from a relaxing day outdoors to a busy day at the office.")
        assert cart_page.get_product_description(3) == ("This classic Sauce Labs t-shirt is perfect to wear when"
                                                        " cozying up to your keyboard to automate a few tests."
                                                        " Super-soft and comfy ringspun combed cotton.")

    @pytest.mark.cart
    def test_all_prices_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        assert cart_page.get_product_price(1) == "$29.99"
        assert cart_page.get_product_price(2) == "$49.99"
        assert cart_page.get_product_price(3) == "$15.99"

    @pytest.mark.cart
    def test_all_quantities_ok(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        assert cart_page.get_product_quantity(1) == "1"
        assert cart_page.get_product_quantity(2) == "1"
        assert cart_page.get_product_quantity(3) == "1"

    @pytest.mark.cart
    def test_remove_button(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        inventory_page.click_cart_button()

        cart_page.remove_item_from_cart("sauce-labs-backpack")
        assert int(cart_page.shopping_cart_badge_value) == 2
        assert cart_page.get_product_name(1) == "Sauce Labs Fleece Jacket"

    @pytest.mark.cart
    def test_continue_shopping_button(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.click_cart_button()

        cart_page.click_continue_shopping_button()
        assert inventory_page.current_url == inventory_page.expected_url
