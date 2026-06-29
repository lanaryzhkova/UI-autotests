import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница логина"""

    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    USERNAME_DESCRIPTION_INPUT = (By.ID, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.TAG_NAME, "button")
    LOGIN_ERROR_ELEMENT = (
        By.XPATH,
        '//*[contains(text(), "Username or password is incorrect")]',
    )
    EMPTY_USERNAME_ERROR_DIV = (
        By.CSS_SELECTOR,
        '[ng-messages="form.username.$error"]',
    )

    EMPTY_USERNAME_TEXT_ERROR = "You did not enter a username"

    @allure.step("Загрузить страницу логина")
    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Войти в учётную запись")
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
        return self.is_visible(self.LOGIN_ERROR_ELEMENT)

    @allure.step("Проверить отображение элементов формы логина")
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

    @allure.step("Проверить подсветку поля и отображение ошибки у Username")
    def assert_empty_username_error(self):
        """Проверка отображения ошибки, если поле Username не заполнено"""
        username = self.find_element(self.USERNAME_INPUT)

        self.set_focus(username)
        self.remove_focus(username)

        error = self.find_element(self.EMPTY_USERNAME_ERROR_DIV)

        assert 'ng-active' in error.get_attribute('class'), "Блок ошибки не активен, у элемента ожидался класс ng-active"
        assert error.text == self.EMPTY_USERNAME_TEXT_ERROR, (
            f"Описание ошибки '{error.text}' не соответствует ожидаемому '{self.EMPTY_USERNAME_TEXT_ERROR}'"
        )

    @allure.step("Проверить активна ли кнопка входа")
    def is_enabled_login_button(self):
        """Проверка активности кнопки входа"""
        login_button = self.find_element(self.LOGIN_BUTTON)
        return login_button.is_enabled()
    