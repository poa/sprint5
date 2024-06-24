# Tests for constructor functionality

import pytest
from selenium.webdriver.common.by import By

from data_locators import Locators as L


class TestConstructor:
    @pytest.mark.parametrize(
        "current_tab, next_tab",
        [
            # fmt: off
            pytest.param(L.SAUCES_TAB, L.FILLING_TAB, id="switch from sauces to filling"),
            pytest.param(L.FILLING_TAB, L.SAUCES_TAB, id="switch from filling to sauces"),
            pytest.param(L.FILLING_TAB, L.LOAVES_TAB, id="switch from filling to loaves"),
            # fmt: on
        ],
    )
    def test_constructor_tabs(self, driver, current_tab, next_tab):

        driver.find_element(By.XPATH, current_tab).click()
        tab = driver.find_element(By.XPATH, next_tab)
        tab.click()

        assert tab.get_attribute("class").find(L.CURRENT_TAB) > 0
