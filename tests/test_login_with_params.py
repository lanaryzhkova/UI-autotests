from dataclasses import dataclass

import allure
import pytest

from pages.auth.login_page import LoginPage
from pages.auth.login_result_page import LoginResultPage


@dataclass
class LoginData:
    username: str
    password: str
    description: str
    expected: bool


@allure.epic("Authentication")
@allure.feature("Login Page")
class TestLoginPage:
    """Тесты для страницы логина"""

    test_data = [
            LoginData(username="angular", password="password", description="description", expected=True),
            LoginData(username="test", password="password", description="description", expected=False),
            LoginData(username="angular", password="test", description="description", expected=False),
            LoginData(username="angular", password="password", description="", expected=False),
            LoginData(username="", password="password", description="description", expected=False),
            LoginData(username="angular", password="", description="description", expected=False),
            LoginData(username="", password="", description="", expected=False),
        ]
    
    test_ids = [
        "valid_fields",
        "invalid_username",
        "invalid_password",
        "empty_description",
        "empty_username",
        "empty_password",
        "empty_all_fields",
        # можно добавить еще
        # "only_username", 
        # "only_password",
        # "only_description",
        # "uppercase_username",
        # "fields_with_spaces"
    ]


    @allure.story("Проверка авторизации с разными параметрами")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(
        "data", test_data, ids=test_ids)
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

        assert login_result_page.is_logged_in() == data.expected, (
            "Пользователь не был успешно авторизован"
        )