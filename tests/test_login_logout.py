# Tests for login/logout functionality

import pytest

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import login, wait_for_element


class TestLoginLogout:
    @pytest.mark.dependency(name="successful_login")
    @pytest.mark.parametrize(
        "location, control",
        [
            pytest.param(TD.CONSTR_PATH, L.LOGIN_BUTTON, id="from main page"),
            pytest.param(TD.ACCOUNT_PATH, L.LOGIN_BUTTON, id="from account page"),
            pytest.param(TD.REG_PATH, L.LOGIN_LINK, id="from registration page"),
            pytest.param(TD.RECOVERY_PATH, L.LOGIN_LINK, id="from recovery page"),
        ],
    )
    def test_login(self, driver, location, control):
        driver.get(TD.APP_URL + location)
        driver.find_element(*control).click()
        login(driver)
        element = wait_for_element(driver, L.ORDER_BUTTON)

        assert element is not None

    @pytest.mark.dependency(depends=["successful_login"])
    def test_logout(self, driver_logged):
        driver_logged.find_element(*L.ACCOUNT_LINK).click()
        wait_for_element(driver_logged, L.LOGOUT_BUTTON)
        driver_logged.find_element(*L.LOGOUT_BUTTON).click()
        element = wait_for_element(driver_logged, L.LOGIN_BUTTON)

        assert element is not None
