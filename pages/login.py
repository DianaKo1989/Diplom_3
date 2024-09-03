import allure

from helpers.data import Endpoints
from locators.locators import LoginLocators
from pages.base import BasePage

class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_url(Endpoints.LOGIN_PAGE)
        self.find_element(LoginLocators.BUTTON_LOGIN)      

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_element(LoginLocators.LINK_RECOVERY)
        self.find_element(LoginLocators.BUTTON_RECOVERY)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def password_recovery(self, user):
        email, password = user
        self.send_keys(LoginLocators.FIELD_EMAIL, email)
        self.click_element(LoginLocators.BUTTON_RECOVERY)
        self.find_element(LoginLocators.LINK_LOGIN)

    @allure.step('Клик на иконку глаза для открытия пароля')
    def click_eye_icon(self):
        self.click_element(LoginLocators.BUTTON_VIEW_PASSWORD)
        return self.find_element(LoginLocators.FIELD_ACTIVE)        

    @allure.step('Авторизоваться новым пользователем без заказа')
    def log_in(self, user):
        email, password = user
        self.send_keys(LoginLocators.FIELD_EMAIL, email)
        self.send_keys(LoginLocators.FIELD_PASSWORD, password)
        self.click_element(LoginLocators.BUTTON_LOGIN)
        self.find_element(LoginLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Авторизоваться')
    def log_in_main_page(self, user):
        self.open_login_page()
        self.log_in(user)

    @allure.step('Авторизоваться пользователем с заказом заказа')
    def log_in_with_order(self, log_in_and_create_order):
        email, password, number = log_in_and_create_order
        self.send_keys(LoginLocators.FIELD_EMAIL, email)
        self.send_keys(LoginLocators.FIELD_PASSWORD, password)
        self.find_element(LoginLocators.BUTTON_LOGIN)
        self.click_element(LoginLocators.BUTTON_LOGIN)
        return number