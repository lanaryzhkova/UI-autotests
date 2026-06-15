from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from data.data import PageUrls
from pages.base_page import BasePage


class CustomerPage(BasePage):
    """Страница кастомера"""

    CUSTOMER_SELECT = (By.ID, "userSelect")
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    WELCOME_TEXT = (By.XPATH, "//strong[contains(., 'Welcome')]")

    def load(self):
        """Загрузить страницу"""
        self.open(PageUrls.CUSTOMER_LOGIN_URL)
        self.wait.wait_for_url(PageUrls.CUSTOMER_LOGIN_URL)
        return self

    def login_customer(self, customer_name: str) -> "CustomerPage":
        """Войти в аккаунт кастомера"""
        customers = Select(self.find_element(self.CUSTOMER_SELECT))
        customers.select_by_visible_text(customer_name)
        self.click(self.find_element(self.CUSTOMER_LOGIN_BUTTON))
        return self

    def check_account_welcome(self, customer_name: str) -> str:
        """Проверить отображение приветствия"""
        welcome_text = self.find_element(self.WELCOME_TEXT).text
        account_name = self.find_element(
            (By.XPATH, f"//strong[contains(., '{customer_name}')]")
        ).text
        return welcome_text + " " + account_name
