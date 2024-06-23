# Tests for registration functionality

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD


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
def test_navigation(driver_logged, location: str, control, destination):
    driver_logged.get(TD.APP_URL + location)
    driver_logged.find_element(By.XPATH, control).click()
    Wait(driver_logged, 3).until(EC.url_changes(location))

    assert driver_logged.current_url == TD.APP_URL + destination
