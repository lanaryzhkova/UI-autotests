import allure

from pages.basic_auth_page import BasicAuthPage

class TestBasicAuthPage:
    """Тесты для страницы Basic Auth Page"""
    @allure.feature("Basic Auth Test")
    @allure.story("Тестирование авторизации на странице Basic Auth")
    def test_basic_auth(self, driver):
        """Тестирование авторизации на странице Basic Auth"""
        basic_auth_page = BasicAuthPage(driver)
        basic_auth_page.load()
        basic_auth_page.login()

        assert basic_auth_page.is_image_displayed(), "Изображение не отображается на странице после авторизации"