import allure

class TestFeedOrderPage:

    @allure.title('Проверка перехода к деталям заказа по клику на заказ в Ленте заказов')
    def test_check_open_order_details(self, feed_page):
        feed_page.open_feed_page()
        assert feed_page.click_on_order_block()

    @allure.title('Синхронизация раздела "История заказов" со страницей "Лента заказов"')
    def test_check_sync_history_order_and_feed_orders(self, feed_page, log_in_with_order, login_page, profile_page):
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_with_order)
        profile_page.open_profile_page()
        profile_page.open_history_orders()
        number_in_history = profile_page.find_number_order_in_history_orders()
        feed_page.open_feed_page()
        number_in_feed = feed_page.check_number_order_in_feed_page(number)
        assert number == number_in_history and number_in_feed

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" после создания заказа')
    def test_check_rise_counter_all_time_after_made_order(self, feed_page, login_page, main_page, user):
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_all_time()
        login_page.log_in_main_page(user)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_all_time()
        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" после создания заказа')
    def test_check_rise_counter_day_after_made_order(self, feed_page, login_page, main_page, user):
        feed_page.open_feed_page()
        counter_before = feed_page.check_counter_day()
        login_page.log_in_main_page(user)
        main_page.create_order()
        feed_page.open_feed_page()
        counter_after = feed_page.check_counter_day()
        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка увеличения счетчика "В работе" после создания заказа')
    def test_check_rise_counter_at_work_after_made_order(self, feed_page, login_page, log_in_with_order):
        login_page.open_login_page()
        number = login_page.log_in_with_order(log_in_with_order)
        feed_page.open_feed_page()
        number_in_at_work = feed_page.check_number_order_in_at_work()
        assert int(number) == int(number_in_at_work) or int(number) == int(number_in_at_work) + 1