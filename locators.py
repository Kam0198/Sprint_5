from selenium.webdriver.common.by import By
class Locators:

    PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") #кнопка ЛК
    PERS_ACCOUNT_BUTTON_ENTER = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") #кнопка ЛК внутри ЛК
    AUTH_BUTTON_ON_MAIN_PAGE = (
    By.XPATH, "// button[contains(text(), 'Войти в аккаунт')]")  #кнопка Войти в аккаунт на главной странице

    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") #кнопка Зарегистрироваться на странице регистрации
    NAME_FIELD_REG = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']") #поле имя на странице регистрации
    EMAIL_FIELD_REG = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']") #поле email на странице регистрации
    PASSWORD_FIELD_REG = (By.NAME, "Пароль") #поле пароль на странице регистрации
    LOGIN_BUTTON_REG = (By.XPATH, "// a[contains(text(), 'Войти')]") #копка Войти на странице Регистрации

    EMAIL_FIELD_AUTH = (By.XPATH, "//input[@type='text']") #поле email на странице авторизации
    PASSWORD_FIELD_AUTH = (By.XPATH, "//input[@type='password']") #поле пароль на странице авторизации
    LOGIN_BUTTON_AUTH_PERSONAL_ACCOUNT = (By.XPATH, "//button[contains(text(),'Войти')]")  #кнопка Войти на странице авторизации
    PASSWORD_RECOVERY = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") #кнопка восстановить пароль
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")  #кнопка восстановить

    PROF_NAME = (By.XPATH, "//li[1]/div/div/input") #имя пользователя в профиле
    PROF_EMAIL = (By.XPATH, "//li[2]/div/div/input") #email пользователя в профиле

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error text_type_main-default") #сообщение о некорректном пароле





