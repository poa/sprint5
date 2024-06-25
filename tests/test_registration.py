# Tests for registration functionality

import pytest

from tools import *


class TestRegistration:
    @pytest.mark.dependency(name="reg_form_is_available")
    def test_registration_open_reg_form(self, driver):

        driver.find_element(*L.LOGIN_BUTTON).click()
        driver.find_element(*L.REG_LINK).click()
        Wait(driver, 3).until(EC.url_to_be(TD.APP_URL + TD.REG_PATH))

        assert driver.current_url.endswith(TD.REG_PATH)

    @pytest.mark.dependency(depends=["reg_form_is_available"])
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
    def test_registration(self, driver_reg_form, name, email, passwd, expected):
        driver_reg_form.find_element(*L.NAME_INPUT).send_keys(name)
        driver_reg_form.find_element(*L.EMAIL_INPUT).send_keys(email)
        driver_reg_form.find_element(*L.PASSWD_INPUT).send_keys(passwd)
        driver_reg_form.find_element(*L.REG_BUTTON).click()
        element = wait_for_element(driver_reg_form, expected)

        assert element is not None
