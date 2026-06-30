import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.auth.login_page.login_page import LoginPage


class LoginResultPage(BasePage):
    """Страница после успешного логина"""

    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/"

    TEXT_ELEMENT = (By.XPATH, '//*[contains(text(), "You\'re logged in!!")]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href*='#/login']")

    @allure.step("Загрузить страницу после успешного логина")
    def load(self):
        """Загрузка страницы"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def is_logged_in(self) -> bool:
        """Проверяет отображение сообщения о входе в систему
        Returns:
            True, если сообщение отображается, иначе False
        """
        return self.is_visible(self.TEXT_ELEMENT)

    @allure.step("Выйти из учётной записи")
    def logout(self) -> "LoginResultPage":
        """Выйти из системы"""
        logout_button = self.wait.wait_for_element_clickable(self.find_element(self.LOGOUT_BUTTON))
        self.click(logout_button)
        self.wait.wait_for_url(LoginPage.URL)
        return self
