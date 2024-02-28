from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage(BasePage):
    __url = "https://www.saucedemo.com/inventory.html"
    __cart_button = (By.CLASS_NAME, "shopping_cart_link")
    __burger_menu_button = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    def is_cart_button_displayed(self) -> bool:
        return super()._is_displayed(self.__cart_button)

    def is_menu_button_displayed(self) -> bool:
        return super()._is_displayed(self.__burger_menu_button)
