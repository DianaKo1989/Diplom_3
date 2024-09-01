import allure
from helpers.data import Endpoints

class TestAccontPage:

    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    def test_check_enter_to_personal_account_in_main_page(self, main_page):
        main_page.open_login_page()
        assert main_page.get_url() == Endpoints.LOGIN_PAGE

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_check_open_history_orders_in_profile_page(self, user, login_page, profile_page):
        login_page.open_login_page()
        login_page.log_in(user)
        profile_page.open_profile_page()
        assert profile_page.open_history_orders() == Endpoints.HISTORY_PAGE

    @allure.title('Проверка выход из аккаунта')
    def test_check_log_out_account_in_profile_page(self, user, login_page, profile_page):
        login_page.open_login_page()
        login_page.log_in(user)
        profile_page.open_profile_page()
        assert profile_page.log_out_in_pesonal_account() == Endpoints.LOGIN_PAGE