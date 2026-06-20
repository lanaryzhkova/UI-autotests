from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginResultPage(BasePage):
    """Страница после успешного логина"""
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/"

    TEXT_ELEMENT = (By.XPATH, '//*[contains(text(), "You\'re logged in!!")]')
    LOGOUT_BUTTON = (By.XPATH, '//*[contains(text(), "Logout")]')

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

    def logout(self) -> "LoginResultPage":
        """Выйти из системы"""
        self.click(self.find_element(self.LOGOUT_BUTTON))
        return self
