from pages.auth.login_page import LoginPage
from pages.auth.login_result_page import LoginResultPage
from data.data import PageUrls, valid_user, not_valid_user


class TestLoginPage:
    """Тесты для страницы логина"""

    def test_elements_are_displayed(self, driver):
        """Тестирование отображения элементов формы логина"""
        login_page = LoginPage(driver)
        login_page.load()

        login_page.assert_is_login_elements_visible()

    def test_login_with_valid_credentials(self, driver):
        """Тестирование успешного входа"""
        login_page = LoginPage(driver)
        login_result_page = LoginResultPage(driver)
        login_page.load()

        login_page.login(
            valid_user["username"], valid_user["password"], valid_user["description"]
        )

        assert login_page.wait.wait_for_url(PageUrls.LOGIN_RESULT_URL), (
            "Пользователь не был перенаправлен после успешного входа"
        )
        assert login_result_page.is_logged_in(), (
            "Пользователь не был успешно авторизован"
        )

    def test_login_with_not_valid_credentials(self, driver):
        """Тестирование входа с невалидными данными"""
        login_page = LoginPage(driver)
        login_page.load()

        login_page.login(
            not_valid_user["username"],
            not_valid_user["password"],
            not_valid_user["description"],
        )

        assert login_page.is_error_message_displayed(), (
            "Сообщение об ошибке не отображается при вводе невалидных данных для входа"
        )

    def test_logout(self, driver):
        """Тестирование выхода"""
        login_page = LoginPage(driver)
        login_result_page = LoginResultPage(driver)
        login_page.load()
        login_page.login(
            valid_user["username"], valid_user["password"], valid_user["description"]
        )

        login_result_page.logout()

        login_page.assert_is_login_elements_visible()
