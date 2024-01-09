from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants

class TestAuthOnRecoveryPage:
    def test_login_recovery_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REG).click()
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_ORDER_ENTER))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER).click()
        personal_account = WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER).click()
        assert personal_account
