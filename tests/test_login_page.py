import allure

from data.data import not_valid_user, valid_user
from pages.auth.login_page.login_page import LoginPage
from pages.auth.login_result_page import LoginResultPage


@allure.epic("Authentication")
@allure.feature("Login Page")
class TestLoginPage:
    """Тесты для страницы логина"""

    @allure.story("Проверка полей ввода")
    @allure.severity(allure.severity_level.NORMAL)
    def test_elements_are_displayed(self, driver):
        """Тестирование отображения элементов формы логина"""
        login_page = LoginPage(driver)
        login_page.load()

        login_page.assert_is_login_elements_visible()

    @allure.story("Проверка успешной авторизации")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_with_valid_credentials(self, driver):
        """Тестирование успешного входа"""
        login_page = LoginPage(driver)
        login_result_page = LoginResultPage(driver)
        login_page.load()

        login_page.login(
            valid_user["username"], valid_user["password"], valid_user["description"]
        )

        assert login_page.wait.wait_for_url(LoginResultPage.URL), (
            "Пользователь не был перенаправлен после успешного входа"
        )
        assert login_result_page.is_logged_in(), (
            "Пользователь не был успешно авторизован"
        )

    @allure.story("Проверка авторизации с невалидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
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

    @allure.story("Проверка успешного выхода из учётной записи")
    @allure.severity(allure.severity_level.NORMAL)
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

    @allure.story("Проверка авторизации с невалидными данными (пустое поле username)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_empty_username(self, driver):
        """Тестирование входа в систему без username"""
        login_page = LoginPage(driver)
        login_page.load()

        login_page.assert_empty_username_error()
        assert not login_page.is_enabled_login_button()

    @allure.story("Проверка наличия скролла после уменьшения размера страницы")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_has_scroll(self, driver):
        """Тестирование наличия скролла после уменьшения размера страницы"""
        login_page = LoginPage(driver)
        login_page.load()

        driver.set_window_size(800, 350)

        assert login_page.is_scroll_on_page(), "На странице нет скролла"