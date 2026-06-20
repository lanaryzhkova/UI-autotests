from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница логина"""
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    USERNAME_DESCRIPTION_INPUT = (By.ID, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.TAG_NAME, "button")
    ERROR_ELEMENT = (
        By.XPATH,
        '//*[contains(text(), "Username or password is incorrect")]',
    )

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def login(self, username: str, password: str, description: str) -> "LoginPage":
        """
        Вход в систему
        Args:
            username: Имя пользователя
            password: Пароль
            description: Описание пользователя
        """
        self.send_keys_to_input(self.USERNAME_INPUT, username)
        self.send_keys_to_input(self.PASSWORD_INPUT, password)
        self.send_keys_to_input(self.USERNAME_DESCRIPTION_INPUT, description)
        self.click(self.find_element(self.LOGIN_BUTTON))
        return self

    def is_error_message_displayed(self) -> bool:
        """Отображение сообщения об ошибке
        Returns:
            True, если сообщение отображается, иначе False
        """
        return self.is_visible(self.ERROR_ELEMENT)

    def assert_is_login_elements_visible(self) -> bool:
        """Проверить видимость элементов формы логина
        Returns:
            True, если все видимы, иначе False
        """
        elements = {
            "Поле Имя пользователя": self.USERNAME_INPUT,
            "Поле Пароль": self.PASSWORD_INPUT,
            "Кнопка входа": self.LOGIN_BUTTON,
        }

        for element_name, locator in elements.items():
            assert self.is_visible(locator), f"{element_name} отсутствует"

        return True
