import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_tests import TestData as TD
from data_locators import Locators as L
from tools import login, wait_for_element


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
    driver.find_element(*L.LOGIN_BUTTON).click()
    driver.find_element(*L.REG_LINK).click()
    return driver

@pytest.fixture
def driver_logged(driver):
    driver.find_element(*L.LOGIN_BUTTON).click()
    login(driver)
    wait_for_element(driver, L.ORDER_BUTTON)
    return driver
