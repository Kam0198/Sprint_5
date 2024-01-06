from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestIngredients:
    def test_ingredients_filings(self, driver):
        driver.find_element(*Locators.BUTTON_FILINGS).click()
        filings = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(Locators.BUTTON_FILINGS)).text
        actual_result = filings
        expected_result = "Начинки"
        assert actual_result == expected_result

    def test_ingredient_souse(self, driver):
        driver.find_element(*Locators.BUTTON_SOUSE).click()
        souse = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BUTTON_SOUSE)).text
        actual_result = souse
        expected_result = "Соусы"
        assert  actual_result == expected_result

    def test_ingredient_bread(self, driver):
        driver.find_element(*Locators.BUTTON_SOUSE).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BUTTON_SOUSE))
        driver.find_element(*Locators.BUTTON_BREAD).click()
        bread = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_BREAD)).text

        actual_value = bread
        expected_value = "Булки"
        assert actual_value == expected_value