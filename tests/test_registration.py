# Tests for registration functionality

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDWait

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import *


@pytest.mark.dependency()
def test_registration_open_reg_form(driver):

    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()
    WDWait(driver, 3).until(EC.url_to_be(TD.APP_URL + TD.REG_PATH))

    assert driver.current_url.endswith(TD.REG_PATH)


@pytest.mark.dependency(depends=["test_registration_open_reg_form"])
def test_registration_successful_registration_correct_inputs(driver_reg_form):
    name = gen_name()
    email = gen_email()
    passwd = gen_passwd()

    driver_reg_form.find_element(By.XPATH, L.NAME_INPUT).send_keys(name)
    driver_reg_form.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(email)
    driver_reg_form.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(passwd)
    driver_reg_form.find_element(By.XPATH, L.REG_BUTTON).click()
    WDWait(driver_reg_form, 3).until(EC.url_changes(driver_reg_form.current_url))

    assert driver_reg_form.current_url.endswith(TD.LOGIN_PATH)


@pytest.mark.dependency(depends=["test_registration_open_reg_form"])
def test_registration_bad_password_short(driver_reg_form):
    name = gen_name()
    email = gen_email()
    passwd = "short"

    driver_reg_form.find_element(By.XPATH, L.NAME_INPUT).send_keys(name)
    driver_reg_form.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(email)
    driver_reg_form.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(passwd)
    driver_reg_form.find_element(By.XPATH, L.REG_BUTTON).click()
    element = WDWait(driver_reg_form, 3).until(
        EC.presence_of_element_located((By.XPATH, L.SHORT_PASSWORD_ERROR))
    )

    assert element is not None


@pytest.mark.dependency(depends=["test_registration_open_reg_form"])
def test_registration_error_existing_user(driver_reg_form):

    driver_reg_form.find_element(By.XPATH, L.NAME_INPUT).send_keys(TD.USER_NAME)
    driver_reg_form.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver_reg_form.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver_reg_form.find_element(By.XPATH, L.REG_BUTTON).click()

    element = WDWait(driver_reg_form, 2).until(
        EC.presence_of_element_located((By.XPATH, L.EXISTING_USER_ERROR))
    )
    assert element is not None
