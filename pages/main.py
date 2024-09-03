import allure

from helpers.data import MAIN_PAGE
from locators.locators import MainLocators
from pages.base import BasePage


class MainPage(BasePage):

    @allure.step('Открыть главную страницу Stellar Burgers')
    def open_main_page(self):
        self.open_url(MAIN_PAGE)
        self.find_element(MainLocators.BUILDER_BUTTON)

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_url(MAIN_PAGE)
        self.click_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)
        self.find_element(MainLocators.HEADER_LOGIN_PAGE)

    @allure.step('Открыть страницу Конструктора')
    def open_builder(self):
        self.click_element(MainLocators.BUILDER_BUTTON)
        return self.find_element(MainLocators.HEADER_CONSTRUCTOR)

    @allure.step('Открыть всплывающее окно "Детали ингредиента"')
    def open_ingredient_pop_up(self):
        self.click_element(MainLocators.BUN_ITEM)
        return self.find_element(MainLocators.HEADER_POP_UP)

    @allure.step('Открыть всплывающее окно "Детали ингредиента"')
    def close_ingredient_pop_up(self):
        self.click_element(MainLocators.CLOSE_POP_UP_BUTTON)
        return self.find_element(MainLocators.CLOSE_POP_UP)

    @allure.step('Добавить ингредиент в заказ')
    def add_items_in_order(self):
        self.find_element(MainLocators.COUNTER_BUN)
        counter = self.get_text(MainLocators.COUNTER_BUN)
        self.drag_and_drop(MainLocators.BUN_ITEM, MainLocators.ADD_SECTION)
        return counter

    @allure.step('Проверить изменение счетчика ингредиента')
    def check_counter_after_add(self):
        counter = self.get_text(MainLocators.COUNTER_BUN)
        return counter

    @allure.step('Тапнуть на кнопку "Оформить заказ')
    def click_button_create_order(self):
        self.find_element(MainLocators.CREATE_ORDER_BUTTON)
        self.click_element(MainLocators.CREATE_ORDER_BUTTON)
        return self.find_element(MainLocators.HEADER_CREATE_ORDER_POP_UP)

    @allure.step('Оформить заказ')
    def create_order(self):
        self.find_element(MainLocators.CREATE_ORDER_BUTTON)
        self.open_main_page()
        self.add_items_in_order()
        self.click_button_create_order()