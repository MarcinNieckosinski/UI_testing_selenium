from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):
    __url = "https://www.saucedemo.com/inventory.html"
    __cart_button = (By.CLASS_NAME, "shopping_cart_link")
    __burger_menu_button = (By.ID, "react-burger-menu-btn")
    __add_to_cart_button = (By.ID, 'add-to-cart-{0}')
    __remove_button = (By.XPATH, "//button[@data-test='remove-{0}']")
    __product_price = (By.XPATH, "(//div[@class='inventory_item_price'])[{0}]")
    __product_name = (By.XPATH, "(//div[@class='inventory_item_name '])[{0}]")
    __product_description = (By.XPATH, "(//div[@class='inventory_item_desc'])[{0}]")
    __product_img = (By.XPATH, "//img[@alt='{0}']")
    __shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    __sort_select = (By.XPATH, "//select[@data-test='product_sort_container']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def shopping_cart_badge_value(self) -> str:
        return self._get_text(self.__shopping_cart_badge)

    @property
    def is_shopping_cart_badge_displayed(self) -> bool:
        return super()._is_displayed(self.__shopping_cart_badge)

    def sort_products(self, sort_option):
        select = Select(super()._find(self.__sort_select))
        select.select_by_value(sort_option)

    def is_cart_button_displayed(self) -> bool:
        return super()._is_displayed(self.__cart_button)

    def is_menu_button_displayed(self) -> bool:
        return super()._is_displayed(self.__burger_menu_button)

    def add_item_to_cart(self, item: str):
        item_to_add_locator = (self.__add_to_cart_button[0], self.__add_to_cart_button[1].format(item))
        super()._click(item_to_add_locator)

    def remove_item_from_cart(self, item: str):
        item_to_remove_locator = (self.__remove_button[0], self.__remove_button[1].format(item))
        super()._click(item_to_remove_locator)

    def get_product_img_url(self, alt: str) -> str:
        return super()._find((self.__product_img[0], self.__product_img[1].format(alt))).get_attribute("src")

    def get_product_price(self, product_number: int) -> str:
        return super()._get_text((self.__product_price[0],
                                  self.__product_price[1].format(product_number)), 3)

    def get_product_name(self, product_number: int) -> str:
        return super()._get_text((self.__product_name[0],
                                  self.__product_name[1].format(product_number)), 3)

    def get_product_description(self, product_number: int) -> str:
        return super()._get_text((self.__product_description[0],
                                  self.__product_description[1].format(product_number)), 3)

    def click_cart_button(self):
        super()._click(self.__cart_button)
