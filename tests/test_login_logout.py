# Tests for login/logout functionality

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
        pytest.param(TD.CONSTR_PATH, L.LOGIN_BUTTON, id="from main page"),
        pytest.param(TD.ACCOUNT_PATH, L.LOGIN_BUTTON, id="from account page"),
        pytest.param(TD.REG_PATH, L.LOGIN_LINK, id="from registration page"),
        pytest.param(TD.RECOVERY_PATH, L.LOGIN_LINK, id="from recovery page"),
    ],
)
def test_login(driver, location, control):
    driver.get(TD.APP_URL + location)
    driver.find_element(By.XPATH, control).click()
    driver.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    element = Wait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, L.ORDER_BUTTON))
    )

    assert element is not None


@pytest.mark.dependency(dependent=["test_login"])
def test_logout(driver):
    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.ACCOUNT_LINK).click()
    Wait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, L.LOGOUT_BUTTON)))
    driver.find_element(By.XPATH, L.LOGOUT_BUTTON).click()
    element = Wait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, L.LOGIN_BUTTON))
    )

    assert element is not None

