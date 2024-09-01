import allure

from helpers.data import Endpoints

class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_check_open_recovery_page_on_button(self, login_page):
        login_page.open_login_page()
        login_page.click_recovery_button()
        assert login_page.get_url() == Endpoints.RECOVERY_PAGE

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_enter_email_and_click_recovery_button(self, login_page, user):
        login_page.open_login_page()
        login_page.click_recovery_button()
        login_page.password_recovery(user)
        assert login_page.check_url(Endpoints.RESET_PASSWORD)

    @allure.title('Проверка тапа на показ/сокрытие пароля в поле "Пароль"')
    def test_check_active_email_input_after_click_eye_icon(self, login_page):
        login_page.open_login_page()
        assert login_page.click_eye_icon()