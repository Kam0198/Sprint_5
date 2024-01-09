from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants

class TestExit:
    def test_exit_from_personal_account(self, driver):
        driver.find_element(*Locators.AUTH_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_AUTH).send_keys(constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_ORDER_ENTER))

        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

        driver.find_element(*Locators.EXIT_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
