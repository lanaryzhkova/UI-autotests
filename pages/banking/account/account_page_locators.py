from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AccountPageLocators:
    """Локаторы для страницы Account"""
    DEPOSIT_TAB_BUTTON = (By.CSS_SELECTOR, '[ng-click="deposit()"]')
    TRANSACTIONS_TAB_BUTTON = (By.CSS_SELECTOR, '[ng-click="transactions()"]')
    WITHDRAWL_TAB_BUTTON = (By.CSS_SELECTOR, '[ng-click="withdrawl()"]')
    AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='amount']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    DEPOSIT_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Deposit Successful')]")
    WITHDRAWL_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Transaction successful')]")
    WITHDRAWL_FAIL_MESSAGE = (By.XPATH, "//*[contains(text(), "
                                "'Transaction Failed. You can not withdraw amount more than the balance.')]")
    TRANSACTIONS_TABLE = (By.TAG_NAME, 'table')
    TRANSACTIONS_ROWS = (By.CSS_SELECTOR, "tbody tr")
    TRANSACTIONS_CELLS = (By.CSS_SELECTOR, "td")
    BALANCE_VALUE = (By.XPATH, "//div[contains(., 'Balance')]/strong[2]")
    WITHDRAWL_LABEL = (By.XPATH, "//label[contains(text(), 'Amount to be Withdrawn :')]")
    RESET_TRANSACTION_BUTTON = (By.CSS_SELECTOR, '[ng-click="reset()"]')
    BACK_TRANSACTION_BUTTON = (By.CSS_SELECTOR, '[ng-click="back()"]')

    @staticmethod
    def get_transaction_amount_cell(row_element: WebElement) -> str:
        """Получить ячейку с суммой из строки таблицы"""
        cells = row_element.find_elements(*AccountPageLocators.TRANSACTIONS_CELLS)
        return cells[1].text if len(cells) > 1 else ""
    
    @staticmethod
    def get_transaction_operation_cell(row_element: WebElement) -> str:
        """Получить ячейку с типом операции из строки таблицы"""
        cells = row_element.find_elements(*AccountPageLocators.TRANSACTIONS_CELLS)
        return cells[2].text if len(cells) > 2 else ""
