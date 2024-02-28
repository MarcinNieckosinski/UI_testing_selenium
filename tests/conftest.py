import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome()
    # my_driver.implicitly_wait(10)
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
