import allure

from locators.locators import FeedLocators
from pages.base import BasePage
from helpers.data import Endpoints


@allure.suite('Методы на Ленту Заказов')
class FeedOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу лента заказов')
    def open_feed_page(self):
        self.open_url(Endpoints.FEED_PAGE)
        self.wait_element_visibility_of_element_located(FeedLocators.HEADER_ORDER_FEED)

    @allure.step('Открыть ленту заказа')
    def open_order_feed(self):
        self.click_element(FeedLocators.ORDER_FEED_BUTTON)
        self.wait_element_visibility_of_element_located(FeedLocators.HEADER_ORDER_FEED)
        self.find_element(FeedLocators.HEADER_ORDER_FEED)
        return self.get_url()        

    @allure.step('Тапаем на блок заказа')
    def click_on_order_block(self):
        self.click_element(FeedLocators.ORDER_BLOCK)
        self.wait_element_visibility_of_element_located(FeedLocators.ORDER_BLOCK_POP_UP)
        return self.find_element(FeedLocators.NUMBER_ORDER_BLOCK)
    
    @allure.step('Проверка значения счетчика "Выполнено за все время"')
    def check_counter_all_time(self):
        self.wait_element_visibility_of_element_located(FeedLocators.COUNTER_ALL_TIME)
        counter = self.find_element(FeedLocators.COUNTER_ALL_TIME)
        return counter.text    
    
    @allure.step('Проверка значения счетчика "Выполнено за сегодня"')
    def check_counter_day(self):
        self.wait_element_visibility_of_element_located(FeedLocators.COUNTER_DAY)
        counter = self.find_element(FeedLocators.COUNTER_DAY)
        return counter.text    
    
    @allure.step('Проеряем, что номер заказа появился в разделе "В работе" на Ленте заказов')
    def check_number_order_in_at_work(self):
        self.wait_element_visibility_of_element_located(FeedLocators.NUMBER_ORDER_LIST_ONLINE)
        counter = self.find_element(FeedLocators.NUMBER_ORDER_LIST_ONLINE)
        return counter.text.lstrip('0')
    
    @allure.step('Проверяем, что номер из Истории заказов совпадает с номером на Ленте заказов')
    def check_number_order_in_feed_page(self, number):
        orders = self.find_elements(FeedLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS)
        for _ in orders:
            if number in _.text:
                return True
        return False