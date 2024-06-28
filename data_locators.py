# Data module with locator constants

from selenium.webdriver.common.by import By

from data_tests import TestData as TD


class Locators:
    # fmt: off

    LOGIN_BUTTON = (By.XPATH, "//button[starts-with(text(),'Войти')]")  # Login button
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")              # Logout button
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")      # Order button
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")     # Registration button
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")    # Registration button

    ACCOUNT_LINK = (By.XPATH, f"//a[@href='{TD.ACCOUNT_PATH}']")         # Account link
    CONSTR_LINK = (By.XPATH, f"//a[@href='{TD.CONSTR_PATH}']")           # Constructor link (main page)
    LOGIN_LINK = (By.XPATH, f"//a[@href='{TD.LOGIN_PATH}']")             # Login link
    LOGO_LINK = (By.XPATH, f"//div[starts-with(@class,'AppHeader_header__logo')]/a") # Logo link
    RECOVERY_LINK = (By.XPATH,f"//a[@href='{TD.RECOVERY_PATH}']")       # Password recovery link
    REG_LINK = (By.XPATH,f"//a[@href = '{TD.REG_PATH}']")               # Registration link

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")        # Input field for Email
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")           # Input field for Name
    PASSWD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")      # Input field for Password

    CURRENT_TAB = "tab_type_current"                                    # Current tab indication
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']/..")             # Constructor tab with filling
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")                # Constructor tab with loaves
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")                # Constructor tab with sauces

    EXISTING_USER_ERROR = (By.XPATH, "//p[text()='Такой пользователь уже существует']") # Ошибка: Пользователь не существует
    SHORT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")              # Ошибка: Некорректный пароль
    # fmt: on
