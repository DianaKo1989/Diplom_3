import allure

from helpers.data import Endpoints
from locators.locators import AutorizationLocators, RecoveryLocators, MainLocators
from pages.base import BasePage

class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_url(Endpoints.LOGIN_PAGE)
        self.wait_element_visibility_of_element_located(AutorizationLocators.BUTTON_LOGIN)      

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_element(AutorizationLocators.LINK_RECOVERY)
        self.wait_element_visibility_of_element_located(RecoveryLocators.BUTTON_RECOVERY)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def password_recovery(self, user):
        email, password = user
        self.send_keys(AutorizationLocators.FIELD_EMAIL, email)
        self.click_element(RecoveryLocators.BUTTON_RECOVERY)
        self.wait_element_visibility_of_element_located(RecoveryLocators.LINK_LOGIN)

    @allure.step('Клик на иконку глаза для открытия пароля')
    def click_eye_icon(self):
        self.click_element(RecoveryLocators.BUTTON_VIEW_PASSWORD)
        return self.find_element(RecoveryLocators.FIELD_ACTIVE)        

    @allure.step('Авторизоваться новым пользователем без заказа')
    def log_in(self, user):
        email, password = user
        self.send_keys(AutorizationLocators.FIELD_EMAIL, email)
        self.send_keys(AutorizationLocators.FIELD_PASSWORD, password)
        self.click_element(AutorizationLocators.BUTTON_LOGIN)
        self.wait_element_visibility_of_element_located(MainLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Авторизоваться')
    def log_in_main_page(self, user):
        self.open_login_page()
        self.log_in(user)

    @allure.step('Авторизоваться пользователем с заказом заказа')
    def log_in_with_order(self, log_in_with_order):
        email, password, number = log_in_with_order
        self.send_keys(AutorizationLocators.FIELD_EMAIL, email)
        self.send_keys(AutorizationLocators.FIELD_PASSWORD, password)
        self.wait_element_visibility_of_element_located(AutorizationLocators.BUTTON_LOGIN)
        self.click_element(AutorizationLocators.BUTTON_LOGIN)
        return number