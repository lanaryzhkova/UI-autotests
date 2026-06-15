from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.data import PageUrls


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    USERNAME_DESCRIPTION_INPUT = (By.ID, 'formly_1_input_username_0')
    LOGIN_BUTTON = (By.TAG_NAME, 'button')
    ERROR_ELEMENT = (By.XPATH, "//*[contains(text(), \"Username or password is incorrect\")]")


    def load(self):
        self.open(PageUrls.LOGIN_URL)
        self.wait.wait_for_url(PageUrls.LOGIN_URL)
        return self
    
    def login(self, username: str, password: str, description: str):
        self.send_keys_to_input(self.USERNAME_INPUT, username)
        self.send_keys_to_input(self.PASSWORD_INPUT, password)
        self.send_keys_to_input(self.USERNAME_DESCRIPTION_INPUT, description)
        self.click(self.find_element(self.LOGIN_BUTTON))
        return self
    
    def is_error_message_displayed(self):
        return self.is_visible(self.ERROR_ELEMENT)
    

    def assert_is_login_elements_visible(self):
        """Проверить видимость элементов формы логина"""
        elements = {
            "Поле Имя пользователя": self.USERNAME_INPUT,
            "Поле Пароль": self.PASSWORD_INPUT,
            "Кнопка входа": self.LOGIN_BUTTON,
        }
        
        for element_name, locator in elements.items():
            assert self.is_visible(locator), f"{element_name} отсутствует"
        
        return True
