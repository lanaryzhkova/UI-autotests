import allure
import pytest


@allure.epic("Authentication")
@allure.feature("Demo Auth")

class TestDemoAuthPage():
    """Тестирование логина через cookie"""
    @allure.story("Проверка авторизации через cookie")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.repeat(2)
    def test_valid_auth(self, authorized_user):
        """Тестирование входа в систему"""
        assert authorized_user.is_logged_in(), (
            "Пользователь не был успешно авторизован"
        )
        