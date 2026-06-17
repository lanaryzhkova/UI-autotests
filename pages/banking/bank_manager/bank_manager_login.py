from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

from .bank_manager_locators import BankManagerPageLocators


class BankManagerLoginPage(BasePage):
    """Страница Bank Manager Login"""
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager"
    
    OPEN_ACCOUNT_URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager/openAccount"
    SAMPLE_FORM_URL = "https://www.way2automation.com/angularjs-protractor/banking/registrationform.html"
    CUSTOMERS_URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager/list"
    ADD_CUSTOMER_URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager/addCust"

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def go_to_add_customer(self) -> "BankManagerLoginPage":
        """Перейти к Add Customer"""
        self.click(self.find_element(BankManagerPageLocators.ADD_CUSTOMER_BUTTON))
        self.wait.wait_for_url(self.ADD_CUSTOMER_URL)
        return self

    def go_to_open_account(self) -> "BankManagerLoginPage":
        """Перейти к Open Account"""
        self.click(self.find_element(BankManagerPageLocators.OPEN_ACCOUNT_BUTTON))
        self.wait.wait_for_url(self.OPEN_ACCOUNT_URL)
        return self

    def go_to_customers(self) -> "BankManagerLoginPage":
        """Перейти к Customers"""
        self.click(self.find_element(BankManagerPageLocators.CUSTOMERS_BUTTON))
        self.wait.wait_for_url(self.CUSTOMERS_URL)
        return self

    def add_customer(
        self, first_name: str, last_name: str, postcode: str
    ) -> "BankManagerLoginPage":
        """Добавить кастомера"""
        self.send_keys_to_input(BankManagerPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_input(BankManagerPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_input(BankManagerPageLocators.POSTCODE_INPUT, postcode)
        self.click(
            self.find_element(BankManagerPageLocators.ADD_CUSTOMER_SUBMIT_BUTTON)
        )
        return self

    def open_account(
        self, customer_name: str, currency_value: str
    ) -> "BankManagerLoginPage":
        """Открыть (создать) аккаунт с валютой"""
        customers = Select(self.find_element(BankManagerPageLocators.CUSTOMER_SELECT))
        currency = Select(self.find_element(BankManagerPageLocators.CURRENCY_SELECT))
        customers.select_by_visible_text(customer_name)
        currency.select_by_visible_text(currency_value)

        self.click(self.find_element(BankManagerPageLocators.PROCESS_BUTTON))
        return self

    def search_customer(self, first_name: str, last_name: str) -> WebElement | bool:
        """Найти кастомера"""
        self.send_keys_to_input(BankManagerPageLocators.SEARCH_INPUT, f"{first_name}")
        customers = self.find_elements(BankManagerPageLocators.CUSTOMER_ROW)
        for customer in customers:
            if first_name in customer.text and last_name in customer.text:
                return customer
        return False

    def delete_customer(self, first_name: str, last_name: str) -> bool:
        """Удалить кастомера"""
        customers = self.find_elements(BankManagerPageLocators.CUSTOMER_ROW)
        for customer in customers:
            if first_name in customer.text and last_name in customer.text:
                self.click(
                    customer.find_element(
                        *BankManagerPageLocators.DELETE_CUSTOMER_BUTTON
                    )
                )
                return True
        return False
