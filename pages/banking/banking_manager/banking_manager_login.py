from pages.base_page import BasePage
from data.data import PageUrls
from .banking_manager_locators import BankingManagerPageLocators
from selenium.webdriver.support.select import Select

class BankingManagerLoginPage(BasePage):

    def load(self):
        self.open(PageUrls.BANKING_MANAGER_URL)
        self.wait.wait_for_url(PageUrls.BANKING_MANAGER_URL)
        return self
    
    def go_to_add_customer(self):
        self.click(self.find_element(BankingManagerPageLocators.ADD_CUSTOMER_BUTTON))
        self.wait.wait_for_url(PageUrls.ADD_CUSTOMER_URL)
        return self
    
    def go_to_open_account(self):
        self.click(self.find_element(BankingManagerPageLocators.OPEN_ACCOUNT_BUTTON))
        self.wait.wait_for_url(PageUrls.OPEN_ACCOUNT_URL)
        return self
    
    def go_to_customers(self):
        self.click(self.find_element(BankingManagerPageLocators.CUSTOMERS_BUTTON))
        self.wait.wait_for_url(PageUrls.CUSTOMERS_URL)
        return self

    def add_customer(self, first_name: str, last_name: str, postcode: str):
        self.send_keys_to_input(BankingManagerPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_input(BankingManagerPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_input(BankingManagerPageLocators.POSTCODE_INPUT, postcode)
        self.click(self.find_element(BankingManagerPageLocators.ADD_CUSTOMER_SUBMIT_BUTTON))
        return self
    
    def open_account(self, customer_name: str, currency_value: str):
        customers = Select(self.find_element(BankingManagerPageLocators.CUSTOMER_SELECT))
        currency = Select(self.find_element(BankingManagerPageLocators.CURRENCY_SELECT))
        customers.select_by_visible_text(customer_name)
        currency.select_by_visible_text(currency_value)

        self.click(self.find_element(BankingManagerPageLocators.PROCESS_BUTTON))
        return self
    
    def search_customer(self, first_name: str, last_name: str):
        self.send_keys_to_input(BankingManagerPageLocators.SEARCH_INPUT, f"{first_name}")
        customers = self.find_elements(BankingManagerPageLocators.CUSTOMER_ROW)
        for customer in customers:
            if (first_name in customer.text and last_name in customer.text):
                return customer
        return None

    def delete_customer(self, first_name: str, last_name):
        customers = self.find_elements(BankingManagerPageLocators.CUSTOMER_ROW)
        for customer in customers:
            if (first_name in customer.text and last_name in customer.text):
                self.click(customer.find_element(*BankingManagerPageLocators.DELETE_CUSTOMER_BUTTON))
                return True
        return False

