from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SecondCheckoutPage(BasePage):
    __url = "https://www.saucedemo.com/checkout-step-two.html"
    __payment_information_field = (By.XPATH, "div[@class='summary_value_label'])[1]")
    __shipping_information_field = (By.XPATH, "div[@class='summary_value_label'])[2]")
    __item_total_field = (By.XPATH, "div[@class='summary_subtotal_label')")
    __item_tax_field = (By.XPATH, "div[@class='summary_tax_label')")
    __total_amount_field = (By.XPATH, "div[@class='summary_total_label']")
    __cancel_button = (By.ID, "cancel")
    __finish_button = (By.ID, "finish")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def payment_information(self) -> str:
        return super()._get_text(self.__payment_information_field)

    @property
    def shipping_information(self) -> str:
        return super()._get_text(self.__shipping_information_field)

    @property
    def item_total(self) -> str:
        return super()._get_text(self.__item_total_field)

    @property
    def item_tax(self) -> str:
        return super()._get_text(self.__item_tax_field)

    @property
    def total_amount(self) -> str:
        return super()._get_text(self.__total_amount_field)

    def click_cancel_button(self):
        super()._click(self.__cancel_button)

    def click_finish_button(self):
        super()._click(self.__finish_button)
