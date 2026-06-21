import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class CustomerPage(BasePage):
    """Страница кастомера"""
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/customer"

    CUSTOMER_SELECT = (By.ID, "userSelect")
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    WELCOME_TEXT = (By.XPATH, "//strong[contains(., 'Welcome')]")

    @allure.step("Загрузить страницу кастомера")
    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Войти в аккаунт кастомера")
    def login_customer(self, customer_name: str) -> "CustomerPage":
        """
        Войти в аккаунт кастомера
        Args:
            customer_name: Имя кастомера
        """
        customers = Select(self.find_element(self.CUSTOMER_SELECT))
        customers.select_by_visible_text(customer_name)
        self.click(self.find_element(self.CUSTOMER_LOGIN_BUTTON))
        return self

    @allure.step("Проверить отображение приветствия")
    def check_account_welcome(self, customer_name: str) -> str:
        """
        Проверить отображение приветствия
        Args:
            customer_name: Имя кастомера
        
        Returns:
            Текст приветствия"""
        welcome_text = self.find_element(self.WELCOME_TEXT).text
        account_name = self.find_element(
            (By.XPATH, f"//strong[contains(., '{customer_name}')]")
        ).text
        return welcome_text + " " + account_name
