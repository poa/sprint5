from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from data_locators import Locators as L
from data_tests import TestData as TD


def gen_name():
    fake = Faker(["ru_RU"])
    name = fake.name()
    return name


def gen_email():
    fake = Faker(["ru_RU"])
    email = fake.email()
    return email


def gen_passwd():
    fake = Faker()
    passwd = fake.password(length=8, special_chars=False)
    return passwd


def login(driver):
    driver.find_element(*L.EMAIL_INPUT).send_keys(TD.USER_EMAIL)
    driver.find_element(*L.PASSWD_INPUT).send_keys(TD.USER_PASSWD)
    driver.find_element(*L.LOGIN_BUTTON).click()
    return


def wait_for_element(driver, element):
    result = Wait(driver, 5).until(EC.visibility_of_element_located(element))
    return result
