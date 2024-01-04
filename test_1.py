from random import random

from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Kam1 import Constants
from locators import Locators

faker = Faker()

class Test1:
    def test_registration(self, driver):
        email = faker.email()
        #email = f'kkkamk{random.randint(1, 10000)}@ya.ru'
        password = 123456
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.STATUS_MESSAGE)).txt
        assert reg_text == 'Вы успешно зарегистрировались'

    def test_change_ava(self, login):
        WebDriverWait(login,10).until(EC.visibility_of_element_located(Locators.PROFILE_IMAGE)).click()
        WebDriverWait(login,10).until(EC.visibility_of_element_located((By.ID, 'owner-avatar'))).send_keys(Constants.AVATAR)
        login.find_element(By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']").click()
        assert WebDriverWait(login, 10).until(EC.text_to_be_present_in_element_attribute(Locators.PROFILE_IMAGE, 'style', f'background-image: url("{Constants.AVATAR}");'))








