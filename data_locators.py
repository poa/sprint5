# Data module with locator constants

from data_tests import TestData as TD


class Locators:
    # fmt: off
    LOGIN_BUTTON = "//button[starts-with(text(),'Войти')]"  # Login button
    REG_BUTTON = "//button[text()='Зарегистрироваться']"    # Registration button
    LOGIN_LINK = f"//a[@href = '{TD.LOGIN_PATH}']"          # Login link
    REG_LINK = f"//a[@href = '{TD.REG_PATH}']"              # Registration link
    NAME_INPUT = "//label[text()='Имя']/../input"           # Input field for Name
    EMAIL_INPUT = "//label[text()='Email']/../input"        # Input field for Email
    PASSWD_INPUT = "//label[text()='Пароль']/../input"      # Input field for Password
    EXISTING_USER_ERROR = "//p[text()='Такой пользователь уже существует']"
    # fmt: on
