from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage(BasePage):
    __url = "https://www.saucedemo.com/cart.html"
    __continue_shopping_button = (By.XPATH, "//div[@data-test='continue-shopping']")
    __checkout_button = (By.ID, "checkout")
    __product_name = (By.XPATH, "(//div[@class='inventory_item_name')[{0}]")
    __product_description = (By.XPATH, "(//div[@class='inventory_item_desc')[{0}]")
    __product_price = (By.XPATH, "(//div[@class='inventory_item_price')[{0}]")
    __product_quantity = (By.XPATH, "(//div[@class='cart_quantity')[{0}]")
    __remove_button = (By.XPATH, "//button[@data-test='remove-{0}']")
    __shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def shopping_cart_badge_value(self) -> str:
        return self._get_text(self.__shopping_cart_badge)

    def remove_item_from_cart(self, item: str):
        item_to_remove_locator = (self.__remove_button[0], self.__remove_button[1].format(item))
        super()._click(item_to_remove_locator)

    def get_product_price(self, product_number: int) -> str:
        return super()._get_text((self.__product_price[0],
                                  self.__product_price[1].format(product_number)), 3)

    def get_product_name(self, product_number: int) -> str:
        return super()._get_text((self.__product_name[0],
                                  self.__product_name[1].format(product_number)), 3)

    def get_product_description(self, product_number: int) -> str:
        return super()._get_text((self.__product_description[0],
                                  self.__product_description[1].format(product_number)), 3)

    def get_product_quantity(self, product_number: int) -> str:
        return super()._get_text((self.__product_quantity[0],
                                  self.__product_quantity[1].format(product_number)), 3)

    def click_continue_shopping_button(self):
        super()._click(self.__continue_shopping_button)

    def click_checkout_button(self):
        super()._click(self.__checkout_button)
