import pytest
from page_object.inventory_page import InventoryPage
from page_object.login_page import LoginPage


class TestInventoryPagePositiveScenarios:

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_number, product_name", [
        (1, "Sauce Labs Backpack"),
        (2, "Sauce Labs Bike Light"),
        (3, "Sauce Labs Bolt T-Shirt"),
        (4, "Sauce Labs Fleece Jacket"),
        (5, "Sauce Labs Onesie"),
        (6, "Test.allTheThings() T-Shirt (Red)")])
    def test_all_names_ok(self, driver, product_number, product_name):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        assert inventory_page.get_product_name(product_number) == product_name

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_number, product_description", [
        (1, "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled"
            " laptop and tablet protection."),
        (2, "A red light isn't the desired state in testing but it sure helps when riding your bike at night."
            " Water-resistant with 3 lighting modes, 1 AAA battery included."),
        (3, "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel,"
            " 100% ringspun combed cotton, heather gray with red bolt."),
        (4, "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling"
            " everything from a relaxing day outdoors to a busy day at the office."),
        (5, "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom"
            " closure, two-needle hemmed sleeved and bottom won't unravel."),
        (6, "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few"
            " tests. Super-soft and comfy ringspun combed cotton.")])
    def test_description_ok(self, driver, product_number, product_description):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        assert inventory_page.get_product_description(product_number) == product_description

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_number, product_price", [
        (1, "$29.99"),
        (2, "$9.99"),
        (3, "$15.99"),
        (4, "$49.99"),
        (5, "$7.99"),
        (6, "$15.99")])
    def test_price_ok(self, driver, product_number, product_price):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        assert inventory_page.get_product_price(product_number) == product_price

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_number, product_img_url", [
        ("Sauce Labs Backpack", "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"),
        ("Sauce Labs Bike Light", "https://www.saucedemo.com/static/media/bike-light-1200x1500.37c843b0.jpg"),
        ("Sauce Labs Bolt T-Shirt", "https://www.saucedemo.com/static/media/bolt-shirt-1200x1500.c2599ac5.jpg"),
        ("Sauce Labs Fleece Jacket", "https://www.saucedemo.com/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg"),
        ("Sauce Labs Onesie", "https://www.saucedemo.com/static/media/red-onesie-1200x1500.2ec615b2.jpg"),
        ("Test.allTheThings() T-Shirt (Red)", "https://www.saucedemo.com/static/media/red-tatt-1200x1500.30dadef4.jpg")])
    def test_img_ok(self, driver, product_number, product_img_url):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        assert inventory_page.get_product_img_url(product_number) == product_img_url

    @pytest.mark.inventory
    @pytest.mark.parametrize("product_name", [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)"])
    def test_add_remove_cart(self, driver, product_name):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart(product_name)
        assert int(inventory_page.shopping_cart_badge_value) == 1

        inventory_page.remove_item_from_cart(product_name)
        assert not inventory_page.is_shopping_cart_badge_displayed

    @pytest.mark.inventory
    def test_add_remove_multiple_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.add_item_to_cart("sauce-labs-backpack")
        assert int(inventory_page.shopping_cart_badge_value) == 1
        inventory_page.add_item_to_cart("sauce-labs-bike-light")
        assert int(inventory_page.shopping_cart_badge_value) == 2
        inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        assert int(inventory_page.shopping_cart_badge_value) == 3
        inventory_page.add_item_to_cart("sauce-labs-fleece-jacket")
        assert int(inventory_page.shopping_cart_badge_value) == 4
        inventory_page.add_item_to_cart("sauce-labs-onesie")
        assert int(inventory_page.shopping_cart_badge_value) == 5
        inventory_page.add_item_to_cart("test.allthethings()-t-shirt-(red)")
        assert int(inventory_page.shopping_cart_badge_value) == 6

        inventory_page.remove_item_from_cart("test.allthethings()-t-shirt-(red)")
        assert int(inventory_page.shopping_cart_badge_value) == 5
        inventory_page.remove_item_from_cart("sauce-labs-onesie")
        assert int(inventory_page.shopping_cart_badge_value) == 4
        inventory_page.remove_item_from_cart("sauce-labs-fleece-jacket")
        assert int(inventory_page.shopping_cart_badge_value) == 3
        inventory_page.remove_item_from_cart("sauce-labs-bolt-t-shirt")
        assert int(inventory_page.shopping_cart_badge_value) == 2
        inventory_page.remove_item_from_cart("sauce-labs-bike-light")
        assert int(inventory_page.shopping_cart_badge_value) == 1
        inventory_page.remove_item_from_cart("sauce-labs-backpack")
        assert not inventory_page.is_shopping_cart_badge_displayed

    @pytest.mark.inventory
    def test_are_products_sorted_a_to_z(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        assert inventory_page.get_product_name(1) == "Sauce Labs Backpack"
        assert inventory_page.get_product_name(2) == "Sauce Labs Bike Light"
        assert inventory_page.get_product_name(3) == "Sauce Labs Bolt T-Shirt"
        assert inventory_page.get_product_name(4) == "Sauce Labs Fleece Jacket"
        assert inventory_page.get_product_name(5) == "Sauce Labs Onesie"
        assert inventory_page.get_product_name(6) == "Test.allTheThings() T-Shirt (Red)"

    @pytest.mark.inventory
    def test_are_products_sorted_z_to_a(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.sort_products("za")

        assert inventory_page.get_product_name(6) == "Sauce Labs Backpack"
        assert inventory_page.get_product_name(5) == "Sauce Labs Bike Light"
        assert inventory_page.get_product_name(4) == "Sauce Labs Bolt T-Shirt"
        assert inventory_page.get_product_name(3) == "Sauce Labs Fleece Jacket"
        assert inventory_page.get_product_name(2) == "Sauce Labs Onesie"
        assert inventory_page.get_product_name(1) == "Test.allTheThings() T-Shirt (Red)"

    @pytest.mark.inventory
    def test_are_products_sorted_low_to_high_price(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        prices = []

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.sort_products("lohi")
        for i in range(6):
            temp = inventory_page.get_product_price(i + 1).replace("$", "")
            temp = float(temp)
            prices.append(temp)

        assert prices == sorted(prices)

    @pytest.mark.inventory
    def test_are_products_sorted_high_to_low_price(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        prices = []

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        inventory_page.sort_products("hilo")
        for i in range(6):
            temp = inventory_page.get_product_price(i + 1).replace("$", "")
            temp = float(temp)
            prices.append(temp)

        assert prices == sorted(prices, reverse=True)
