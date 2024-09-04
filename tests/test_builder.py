import allure

from helpers.data import Endpoints

class TestBurgerBuilderPage:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_check_open_builder(self, main_page, login_page):
        login_page.open_login_page()
        assert main_page.open_builder()

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_check_open_order_feed(self, main_page, feed_page):
        main_page.open_main_page()
        assert feed_page.open_order_feed() == Endpoints.FEED_PAGE

    @allure.title('Проверка открытия информации об ингредиенте"')
    def test_open_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        assert main_page.open_ingredient_pop_up()

    @allure.title('Проверка закрытия всплывающего окна "Детали ингредиента"')
    def test_close_pop_up_about_ingredient(self, main_page):
        main_page.open_main_page()
        main_page.open_ingredient_pop_up()
        assert main_page.close_ingredient_pop_up()

    @allure.title('Проверка работа счетчика ингредиента после добавления самого ингредиента в заказ')
    def test_check_counter_up_after_add_item_in_order(self, main_page):
        main_page.open_main_page()
        before = main_page.add_items_in_order()
        after = main_page.check_counter_after_add()
        assert before == '0'and after == '2'

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_check_create_order_authorized_user(self, user, login_page, main_page):
        login_page.open_login_page()
        login_page.log_in(user)
        main_page.add_items_in_order()
        assert main_page.click_button_create_order()