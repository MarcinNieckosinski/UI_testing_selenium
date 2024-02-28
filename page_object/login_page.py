from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __login_button = (By.ID, "login-button")
    __error_message = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__login_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, 3)
