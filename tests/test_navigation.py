# Tests for navigation functionality

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD
from tools import wait_for_element


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
    def test_navigation(self, driver_logged, location: str, control, destination):
        wait_for_element(driver_logged, L.ORDER_BUTTON)
        driver_logged.get(TD.APP_URL + location)
        driver_logged.find_element(*control).click()
        Wait(driver_logged, 3).until(EC.url_changes(location))

        assert driver_logged.current_url.startswith(TD.APP_URL + destination)
