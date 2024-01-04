from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestRegistration:
    def test_registration(self, driver):
        self.faker = Faker()
        self.test_email = self.faker.email()
        self.test_name = self.faker.name()
        password = 123456
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(self.test_name)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(self.test_email)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(self.test_email)
        driver.find_element(*Locators.PASSWORD_FIELD_AUTH).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER).click()

        personal_account = WebDriverWait(driver, 10).until(
            EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*Locators.PERS_ACCOUNT_BUTTON_ENTER)
        assert personal_account == True #проверяем, что мы попали в ЛК

        profile_name = driver.find_element(*Locators.PROF_NAME)
        actual_name = profile_name.get_attribute("value")
        expected_name = self.test_name
        assert actual_name == expected_name #проверяем, что имя юзера совпадает с зареганным

        profile_email = driver.find_element(*Locators.PROF_EMAIL)
        actual_email = profile_email.get_attribute("value")
        expected_email = self.test_email
        assert actual_email == expected_email  #проверяем, что email юзера совпадает с зареганным

    def test_pass_incorrect_password(self, driver):
        fake = Faker()
        email = fake.email()
        name = fake.name()
        password = 1222
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD_REG).send_keys(password)
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(*Locators.ERROR_MESSAGE))
        assert error == "Некорректный пароль"






