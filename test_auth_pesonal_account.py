from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_login_personal_account:
    def test_pers_account(self, driver):
        email = "ka@ya.ru"
        password = 123456
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_AUTH).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()
        WebDriverWait