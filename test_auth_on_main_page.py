from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants

class TestAuthMainPage:
    def test_login_main_page(self, driver):
        driver.find_element(*Locators.AUTH_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD_AUTH).send_keys(constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUTTON_ORDER_ENTER))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER).click()

        personal_account = WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER)
        assert personal_account

        profile_email = driver.find_element(*Locators.PROF_EMAIL)
        actual_email = profile_email.get_attribute("value")
        assert actual_email == constants.TEST_EMAIL


