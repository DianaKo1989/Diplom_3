import allure

from locators.locators import ProfileLocators
from pages.base import BasePage


@allure.suite('Методы на Личный кабинет')
class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть персональную страницу')
    def open_profile_page(self):
        self.wait_element_visibility_of_element_located(ProfileLocators.PROFILE_BUTTON)
        self.click_element(ProfileLocators.PROFILE_BUTTON)

    @allure.step('Открыть историю заказов через меню личного кабинета')
    def open_history_orders(self):
        self.wait_element_visibility_of_element_located(ProfileLocators.USER_HISTORY_MENU)
        self.click_element(ProfileLocators.USER_HISTORY_MENU)
        return self.get_url()

    @allure.step('Найти номер заказа в истории заказов')
    def find_number_order_in_history_orders(self):
        self.wait_element_visibility_of_element_located(ProfileLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        number_in_history = self.get_text(ProfileLocators.NUMBER_ORDER_BLOCK)
        clean_number_in_history = number_in_history.lstrip('#0')
        return clean_number_in_history

    @allure.step('Выйти из аккаунта')
    def log_out_in_pesonal_account(self):
        self.wait_element_visibility_of_element_located(ProfileLocators.LOG_OUT_MENU)
        self.click_element(ProfileLocators.LOG_OUT_MENU)
        self.wait_element_visibility_of_element_located(ProfileLocators.LOG_IN_BUTTON)
        return self.get_url()        

