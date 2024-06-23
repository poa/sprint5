# Tests for registration functionality

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD


@pytest.mark.dependency()
@pytest.mark.parametrize(
    "location, control",
    [
        [TD.CONSTR_PATH, L.LOGIN_BUTTON],
        [TD.ACCOUNT_PATH, L.LOGIN_BUTTON],
        [TD.RECOVERY_PATH, L.LOGIN_LINK],
        [TD.REG_PATH, L.LOGIN_LINK]
    ],
)
def test_login_from_main_page(driver, location, control):
    driver.get(TD.APP_URL + location)
    driver.find_element(By.XPATH, control).click()
    driver.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    element = Wait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, L.ORDER_BUTTON))
    )

    assert element is not None


def test_login_from_account_page(driver):
    pass


def test_login_from_reg_form(driver):
    pass


def test_login_from_recovery_form(driver):
    pass


@pytest.mark.dependency(dependent=["test_login_from_main_page"])
def test_logout(driver_logged):
    pass
