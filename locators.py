from selenium.webdriver.common.by import By
class Locators:

    PERSONAL_ACCOUNT_BUTTON_ON_MAIN_PAGE = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") #кнопка ЛК
    PERS_ACCOUNT_BUTTON_ENTER = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") #кнопка ЛК внутри ЛК
    AUTH_BUTTON_ON_MAIN_PAGE = (By.XPATH, "// button[contains(text(), 'Войти в аккаунт')]")  #кнопка Войти в аккаунт на главной странице
    EXIT_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//button[contains(text(),'Выход')]")

    REG_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") #кнопка Зарегистрироваться на странице регистрации
    REG_BUTTON_ = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") #кнопка Зарегистрироваться на странице регистрации
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

    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") #сообщение о некорректном пароле
    BUTTON_ORDER_ENTER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") #кнопка оформить заказ внутри ЛК

    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(., 'Конструктор')]")
    LOGO_BUTTON = (By.XPATH, "//header/nav/div/a/*")

    BUTTON_BREAD = (By.XPATH, "//h2[contains(text(),'Булки')]") #переход на меню Булки
    BUTTON_SOUSE = (By.XPATH, "//h2[contains(text(),'Соусы')]") #переход на меню Соусы
    BUTTON_FILINGS = (By.XPATH, "//h2[contains(text(),'Начинки')]") #переход на меню начинки






