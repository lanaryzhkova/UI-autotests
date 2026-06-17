import random

from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage

from .account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/account"

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def go_to_deposit(self) -> "AccountPage":
        """Перейти к пополнениям"""
        self.click(self.find_element(AccountPageLocators.DEPOSIT_TAB_BUTTON))
        return self

    def go_to_transactions(self) -> "AccountPage":
        """Перейти к транзакциям"""
        self.click(self.find_element(AccountPageLocators.TRANSACTIONS_TAB_BUTTON))
        if not self.is_visible(AccountPageLocators.TRANSACTIONS_ROWS, timeout=2):
            self.driver.refresh()
        return self

    def go_to_withdrawl(self) -> "AccountPage":
        """Перейти к снятиям"""
        self.click(self.find_element(AccountPageLocators.WITHDRAWL_TAB_BUTTON))
        self.wait.wait_for_element_visible(AccountPageLocators.WITHDRAWL_LABEL)
        return self

    def deposit(self, deposit: str) -> "AccountPage":
        """Пополнить баланс"""
        self.send_keys_to_input(AccountPageLocators.AMOUNT_INPUT, deposit)
        self.click(self.find_element(AccountPageLocators.SUBMIT_BUTTON))
        return self

    def deposit_succesfully(self, deposit_value: str) -> "AccountPage":
        """Успешно пополнить баланс"""
        self.go_to_deposit()
        self.deposit(deposit_value)
        assert self.is_success_deposit(), "Пополнение прошло с ошибкой"
        return self

    def withdrawl(self, withdrawl: str) -> "AccountPage":
        """Снять средства с баланса"""
        self.send_keys_to_input(AccountPageLocators.AMOUNT_INPUT, withdrawl)
        self.click(self.find_element(AccountPageLocators.SUBMIT_BUTTON))
        return self

    def withdrawl_successfully(self, withdrawl: str) -> "AccountPage":
        """Успешно снять средства с баланса"""
        self.go_to_withdrawl()
        self.withdrawl(withdrawl)
        assert self.is_success_withdrawl(), "Снятие прошло с ошибкой"
        return self

    def is_success_deposit(self) -> bool:
        """Проверка отображения сообщения об успешном пополнении баланса"""
        return self.is_visible(AccountPageLocators.DEPOSIT_SUCCESS_MESSAGE, timeout=2)

    def is_success_withdrawl(self) -> bool:
        """Проверка отображения сообщения об успешном снятии средств"""
        return self.is_visible(AccountPageLocators.WITHDRAWL_SUCCESS_MESSAGE, timeout=2)

    def is_failed_withdrawl(self) -> bool:
        """Проверка отображения сообщения об ошибке снятия средств"""
        return self.is_visible(AccountPageLocators.WITHDRAWL_FAIL_MESSAGE, timeout=2)

    def get_last_transaction_amount(self) -> str:
        """Получить количество средств из последней транзакции"""
        self.is_visible(AccountPageLocators.TRANSACTIONS_ROWS, timeout=5)
        transactions = self.find_elements_safe(AccountPageLocators.TRANSACTIONS_ROWS)
        if not transactions:
            return ""
        return AccountPageLocators.get_transaction_amount_cell(transactions[-1])

    def is_transaction_with_null_amount(self) -> bool:
        """Проверка наличия транзакции с нулевым значением средств"""
        transactions = self.find_elements_safe(AccountPageLocators.TRANSACTIONS_ROWS)
        if not transactions:
            return False
        return any(
            int(AccountPageLocators.get_transaction_amount_cell(transaction)) == 0
            for transaction in transactions
        )

    def get_balance(self) -> int:
        """Получить баланс аккаунта"""
        return int(self.find_element(AccountPageLocators.BALANCE_VALUE).text.strip())

    def gen_random_withdrawl(self) -> int:
        """Сгенерировать случайное число для снятия средств"""
        return random.randrange(1, int(self.get_balance()))

    def get_balance_from_transactions(self) -> int:
        """Получить баланс исходя из транзакций"""
        self.is_visible(AccountPageLocators.TRANSACTIONS_ROWS, timeout=5)
        transactions = self.find_elements(AccountPageLocators.TRANSACTIONS_ROWS)
        if not transactions:
            return 0
        balance = 0
        for transaction in transactions:
            amount = int(AccountPageLocators.get_transaction_amount_cell(transaction))
            operation = AccountPageLocators.get_transaction_operation_cell(transaction)
            if operation == "Credit":
                balance += amount
            else:
                balance -= amount

        return balance

    def reset_transactions(self) -> "AccountPage":
        """Сбросить все транзакции"""
        self.click(self.find_element(AccountPageLocators.RESET_TRANSACTION_BUTTON))
        return self

    def back_from_transactions(self) -> "AccountPage":
        """Перейти обратно из транзакций"""
        self.click(self.find_element(AccountPageLocators.BACK_TRANSACTION_BUTTON))
        return self

    def count_transactions(self) -> int:
        """Количество транзакций"""
        transactions = self.find_elements(AccountPageLocators.TRANSACTIONS_ROWS)
        return len(transactions)

    def count_transactions_after_reset(self) -> bool | WebElement:
        """Количество транзакций после сброса с ожиданием"""
        return self.wait.wait_for_element_invisible(
            AccountPageLocators.TRANSACTIONS_ROWS
        )
