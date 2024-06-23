# Tests for registration functionality
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDWait

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import *


def test_registration_open_reg_form(driver):

    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()

    assert driver.current_url.endswith(TD.REG_PATH)


def test_registration_successful_registration_correct_inputs(driver):
    name = gen_name()
    email = gen_email()
    passwd = gen_passwd()

    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()
    driver.find_element(By.XPATH, L.NAME_INPUT).send_keys(name)
    driver.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(email)
    driver.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(passwd)
    driver.find_element(By.XPATH, L.REG_BUTTON).click()

    assert driver.current_url.endswith(TD.LOGIN_PATH)


def test_registration_error_existing_user(driver):

    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()
    driver.find_element(By.XPATH, L.NAME_INPUT).send_keys(TD.USER_NAME)
    driver.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver.find_element(By.XPATH, L.REG_BUTTON).click()

    element = WDWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, L.EXISTING_USER_ERROR))
    )
    assert element is not None
