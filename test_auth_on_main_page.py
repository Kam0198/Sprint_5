from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Kam1 import Constants

class Test_auth:
    def test_pers_account(self, driver):
        driver.find_element(*Locators.AUTH_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_AUTH).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()


