import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DemoAuthPage(BasePage):
    """Страница с демо-логином с использованием cookie"""
    LOGIN_URL = "https://practice.expandtesting.com/login"
    AFTER_LOGIN_URL = "https://practice.expandtesting.com/secure"

    LOGIN_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "submit-login")
    WELCOME_TEXT = (By.TAG_NAME, "h4")

    def load(self):
        """Загрузить страницу"""
        self.open(self.LOGIN_URL)
        self.wait.wait_for_url(self.LOGIN_URL)

    @allure.step("Выполнить вход в учётную запись")
    def login(self, username, password):
        """
        Вход в демо систему авторизации
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.click(self.find_element(self.LOGIN_INPUT))
        self.send_keys_to_input(self.LOGIN_INPUT, username)
        self.send_keys_to_input(self.PASSWORD_INPUT, password)
        self.wait.wait_for_element_clickable(self.LOGIN_BUTTON)
        self.click(self.find_element(self.LOGIN_BUTTON))

    @allure.step("Проверить отображение никнейма пользователя")
    def is_logged_in(self) -> bool:
        """Проверяет отображение приветственного сообщения о входе в систему
        Returns:
            True, если сообщение отобржается, иначе False
        """
        result = self.find_element(self.WELCOME_TEXT).text
        return True if "Welcome to the Secure Area." in result else False
