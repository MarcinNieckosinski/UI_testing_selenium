import pytest
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestInventoryPageNegativeScenarios:
    @pytest.mark.inventory
    @pytest.mark.parametrize("product_number, product_img_url", [
        ("Sauce Labs Backpack", "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"),
        ("Sauce Labs Bike Light", "https://www.saucedemo.com/static/media/bike-light-1200x1500.37c843b0.jpg"),
        ("Sauce Labs Bolt T-Shirt", "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"),
        ("Sauce Labs Fleece Jacket", "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg"),
        ("Sauce Labs Onesie", "https://www.saucedemo.com/static/media/red-onesie-1200x1500.2ec615b2.jpg"),
        (
                "Test.allTheThings() T-Shirt (Red)",
                "https://www.saucedemo.com/static/media/red-tatt-1200x1500.30dadef4.jpg")])
    def test_img_not_ok(self, driver, product_number, product_img_url):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("problem_user", "secret_sauce")

        assert inventory_page.get_product_img_url(product_number) != product_img_url

    @pytest.mark.inventory
    def test_not_working_filters(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("problem_user", "secret_sauce")

        inventory_page.sort_products("za")
        assert inventory_page.get_product_name(1) == "Sauce Labs Backpack"

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_name", [
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "test.allthethings()-t-shirt-(red)"])
    def test_not_working_add_to_cart(self, driver, product_name):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("problem_user", "secret_sauce")

        inventory_page.add_item_to_cart(product_name)
        assert not inventory_page.is_shopping_cart_badge_displayed

    def test_performance_glitch(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("performance_glitch_user", "secret_sauce")

        assert inventory_page.current_url == inventory_page.expected_url
        assert not inventory_page.is_cart_button_displayed()
        assert not inventory_page.is_menu_button_displayed()
