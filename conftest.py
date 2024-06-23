import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_tests import TestData as TD
from data_locators import Locators as L


@pytest.fixture
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)
    driver.get(TD.APP_URL)
    yield driver
    driver.quit()


@pytest.fixture
def driver_reg_form(driver):
    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()
    return driver
