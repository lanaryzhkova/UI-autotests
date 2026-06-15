from data.data import PageUrls
from pages.base_page import BasePage
from .banking_app_locators import BankingAppPageLocators


class BankingAppPage(BasePage):
    """Страница BankingApp"""

    def load(self):
        """Загрузить страницу"""
        self.open(PageUrls.BANKING_APP_URL)
        self.wait.wait_for_url(PageUrls.BANKING_APP_URL)
        return self

    def go_to_sample_form(self) -> "BankingAppPage":
        """Перейти к Sample Form"""
        self.click(self.find_element(BankingAppPageLocators.SAMPLE_FORM_BUTTON))
        self.wait.wait_for_url(PageUrls.SAMPLE_FORM_URL)
        return self

    def go_to_bank_manager_login(self) -> "BankingAppPage":
        """Перейти к Bank Manager Login"""
        self.click(self.find_element(BankingAppPageLocators.BANK_MANAGER_LOGIN_BUTTON))
        self.wait.wait_for_url(PageUrls.BANK_MANAGER_URL)
        return self

    def go_to_customer_login(self) -> "BankingAppPage":
        """Перейти к Customer Login"""
        self.click(self.find_element(BankingAppPageLocators.CUSTOMER_LOGIN_BUTTON))
        self.wait.wait_for_url(PageUrls.CUSTOMER_LOGIN_URL)
        return self
