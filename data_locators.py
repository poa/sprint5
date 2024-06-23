# Data module with locator constants

from data_tests import TestData as TD


class Locators:
    # fmt: off
    LOGIN_BUTTON = "//button[starts-with(text(),'Войти')]"  # Login button
    ORDER_BUTTON = "//button[text()='Оформить заказ']"      # Order button
    RECOVERY_BUTTON = "//button[text()='Восстановить']"     # Registration button
    REG_BUTTON = "//button[text()='Зарегистрироваться']"    # Registration button

    ACCOUNT_LINK = f"//a[@href='{TD.ACCOUNT_PATH}']"        # Account link
    CONSTR_LINK = f"//a[@href='{TD.CONSTR_PATH}']"          # Constructor link (main page)
    LOGIN_LINK = f"//a[@href = '{TD.LOGIN_PATH}']"          # Login link
    RECOVERY_LINK = f"//a[@href='{TD.RECOVERY_PATH}']"      # Password recovery link
    REG_LINK = f"//a[@href = '{TD.REG_PATH}']"              # Registration link

    EMAIL_INPUT = "//label[text()='Email']/../input"        # Input field for Email
    NAME_INPUT = "//label[text()='Имя']/../input"           # Input field for Name
    PASSWD_INPUT = "//label[text()='Пароль']/../input"      # Input field for Password

    # Ошибка: Пользователь не существует
    EXISTING_USER_ERROR = "//p[text()='Такой пользователь уже существует']"

    # Ошибка: Некорректный пароль
    SHORT_PASSWORD_ERROR = "//p[text()='Некорректный пароль']"
    # fmt: on
