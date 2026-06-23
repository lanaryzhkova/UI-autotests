import allure

from pages.banking.bank_manager.bank_manager_login import BankManagerLoginPage
from pages.banking.customer_page import CustomerPage
from pages.banking.sample_form.sample_form_page import SampleFormPage
from pages.base_page import BasePage

from .banking_app_locators import BankingAppPageLocators


class BankingAppPage(BasePage):
    """Страница BankingApp"""
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"

    @allure.step("Загрузить страницу BankingApp")
    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Перейти к Sample Form")
    def go_to_sample_form(self) -> "BankingAppPage":
        """Перейти к Sample Form"""
        self.click(self.find_element(BankingAppPageLocators.SAMPLE_FORM_BUTTON))
        self.wait.wait_for_url(SampleFormPage.URL)
        return self

    @allure.step("Перейти к Bank Manager Login")
    def go_to_bank_manager_login(self) -> "BankingAppPage":
        """Перейти к Bank Manager Login"""
        self.click(self.find_element(BankingAppPageLocators.BANK_MANAGER_LOGIN_BUTTON))
        self.wait.wait_for_url(BankManagerLoginPage.URL)
        return self

    @allure.step("Перейти к Customer Login")
    def go_to_customer_login(self) -> "BankingAppPage":
        """Перейти к Customer Login"""
        self.click(self.find_element(BankingAppPageLocators.CUSTOMER_LOGIN_BUTTON))
        self.wait.wait_for_url(CustomerPage.URL)
        return self
