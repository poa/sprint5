# Tests for navigation functionality

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import login


class TestNavigation:
    @pytest.mark.dependency(dependent=["test_login"])
    @pytest.mark.parametrize(
        "location, control, destination",
        [
            # fmt: off
            pytest.param(TD.CONSTR_PATH, L.ACCOUNT_LINK, TD.ACCOUNT_PATH, id="from main to account"),
            pytest.param(TD.ACCOUNT_PATH, L.CONSTR_LINK, TD.CONSTR_PATH, id="from account to main by constructor"),
            pytest.param(TD.ACCOUNT_PATH, L.LOGO_LINK, TD.CONSTR_PATH, id="from account to main by logo"),
            # fmt: on
        ],
    )
    def test_navigation(self, driver, location: str, control, destination):
        driver.find_element(*L.LOGIN_BUTTON).click()
        login(driver)
        Wait(driver, 3).until(EC.visibility_of_element_located(L.ORDER_BUTTON))
        driver.get(TD.APP_URL + location)
        driver.find_element(*control).click()
        Wait(driver, 3).until(EC.url_changes(location))

        assert driver.current_url.startswith(TD.APP_URL + destination)
