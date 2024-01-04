from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import Kam1


class Test_recovery_pass:
    def test_recovery_pass(self, driver):
        driver.find_elements(*Locators.PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY).click()
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(Kam1.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/reset-password'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'