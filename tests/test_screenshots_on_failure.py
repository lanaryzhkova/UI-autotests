import allure
import pytest

from data.login_data import login_test_data, login_test_ids
from pages.auth.login_page import LoginPage
from pages.auth.login_result_page import LoginResultPage

@allure.epic("Authentication (failure)")
@allure.feature("Login Page")
class TestLoginPageFailure:
    """Падающие тесты для страницы логина"""

    @allure.story("Проверка авторизации с разными параметрами (падающие кейсы для демонстрации скриншотов)")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "data", login_test_data, ids=login_test_ids)
    def test_login(self, driver, data):
        """Тестирование входа в учётную запись с разными параметрами"""
        login_page = LoginPage(driver)
        login_result_page = LoginResultPage(driver)
        login_page.load()

        login_page.login(data.username, data.password, data.description)

        if data.expected:
            assert login_page.wait.wait_for_url(LoginResultPage.URL), (
                "Пользователь не был перенаправлен после успешного входа"
            )

        assert login_result_page.is_logged_in() != data.expected, (
            "Пользователь не был успешно авторизован"
        )