from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FirstCheckoutPage(BasePage):
    __url = "https://www.saucedemo.com/checkout-step-one.html"
    __first_name_field = (By.XPATH, "//input[@data-test='firstName']")
    __last_name_field = (By.XPATH, "//input[@data-test='lastName']")
    __zip_postal_code_field = (By.XPATH, "//input[@data-test='postalCode']")
    __cancel_button = (By.XPATH, "//button[@data-test='cancel']")
    __continue_button = (By.XPATH, "//button[@data-test='continue']")
    __error_field = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def first_name_field_value(self) -> str:
        return super()._get_text(self.__first_name_field)

    @property
    def last_name_field_value(self) -> str:
        return super()._get_text(self.__first_name_field)

    @property
    def zip_code_field_value(self) -> str:
        return super()._get_text(self.__first_name_field)

    @property
    def error_field_value(self) -> str:
        return super()._get_text(self.__error_field)

    def complete_first_name_field(self, first_name: str):
        super()._type(self.__first_name_field, first_name)

    def complete_last_name_field(self, last_name: str):
        super()._type(self.__last_name_field, last_name)

    def complete_zip_postal_code_field(self, zip_postal_code: str):
        super()._type(self.__zip_postal_code_field, zip_postal_code)

    def click_cancel_button(self):
        super()._click(self.__cancel_button)

    def click_continue_button(self):
        super()._click(self.__continue_button)
