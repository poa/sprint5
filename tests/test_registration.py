# Tests for registration functionality

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import *


@pytest.mark.dependency()
def test_registration_open_reg_form(driver):

    driver.find_element(By.XPATH, L.LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, L.REG_LINK).click()
    Wait(driver, 3).until(EC.url_to_be(TD.APP_URL + TD.REG_PATH))

    assert driver.current_url.endswith(TD.REG_PATH)


@pytest.mark.dependency(depends=["test_registration_open_reg_form"])
@pytest.mark.parametrize(
    "name, email, passwd, expected",
    [
        # fmt: off
        pytest.param(gen_name(), gen_email(), gen_passwd(), L.LOGIN_BUTTON, id="successful_registration_correct_inputs"),
        pytest.param(gen_name(), gen_email(), "short", L.SHORT_PASSWORD_ERROR, id="bad_password_short"),
        pytest.param(TD.USER_NAME, TD.USER_EMAIL, TD.USER_PASSWD, L.EXISTING_USER_ERROR, id="error_existing_user"),
        # fmt: on
    ],
)
def test_registration(driver_reg_form, name, email, passwd, expected):
    driver_reg_form.find_element(By.XPATH, L.NAME_INPUT).send_keys(name)
    driver_reg_form.find_element(By.XPATH, L.EMAIL_INPUT).send_keys(email)
    driver_reg_form.find_element(By.XPATH, L.PASSWD_INPUT).send_keys(passwd)
    driver_reg_form.find_element(By.XPATH, L.REG_BUTTON).click()
    element = Wait(driver_reg_form, 3).until(
        EC.visibility_of_element_located((By.XPATH, expected))
    )

    assert element is not None

