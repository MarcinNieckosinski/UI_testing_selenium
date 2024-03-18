from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutCompletePage(BasePage):
    __url = "https://www.saucedemo.com/checkout-complete.html"
    __thank_you_header = (By.CLASS_NAME, "complete-header")
    __thank_you_text = (By.CLASS_NAME, "complete-text")
    __back_home_button = (By.ID, "back-to-products")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def thank_you_header_text(self) -> str:
        return super()._get_text(self.__thank_you_header)

    @property
    def thank_you_text(self) -> str:
        return super()._get_text(self.__thank_you_text)

    def click_back_home_button(self):
        super()._click(self.__back_home_button)
