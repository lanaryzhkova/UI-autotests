import pytest

from pages.banking.account.account_page import AccountPage
from pages.banking.banking_app.banking_app_page import BankingAppPage
from pages.banking.bank_manager.bank_manager_login import BankManagerLoginPage

class TestAccountPage:
    """Тесты для страницы Account"""
    def test_valid_deposit(self, driver, customer_is_logged_in):
        """Тестирование успешного пополнения баланса"""
        account_page = AccountPage(driver)

        account_page.deposit_succesfully("100321")

        account_page.load(driver)
        account_page.go_to_transactions()
        
        assert str(account_page.get_last_transaction_amount())=="100321", f'Сумма транзакции {account_page.get_last_transaction_amount()} не равна 100321'


    def test_not_valid_deposit(self, driver, customer_is_logged_in):
        """Тестирование пополнения с невалидным значением (0)"""
        account_page = AccountPage(driver)

        account_page.go_to_deposit()
        account_page.deposit("0")

        assert not account_page.is_success_deposit(), "При невалидном значении транзакция проходит успешно"

        account_page.load(driver)
        account_page.go_to_transactions()
        
        assert not account_page.is_transaction_with_null_amount(), "Найдена транзакция с amount 0"

    def test_valid_withdrawl(self, driver, customer_with_balance):
        """Тестирование успешного снятия средств"""
        account_page = AccountPage(driver)
        withdrawl_value = str(account_page.gen_random_withdrawl())

        account_page.withdrawl_successfully(withdrawl_value)

        account_page.go_to_transactions()
        assert account_page.get_last_transaction_amount()==withdrawl_value, f"Ожидалась транзакиця {withdrawl_value}, получена {account_page.get_last_transaction_amount()}"

    def test_not_valid_withdrawl(self, driver, customer_is_logged_in):
        """Тестирование снятия средств с невалидным значением (1000000 при балансе 0)"""
        account_page = AccountPage(driver)

        account_page.go_to_withdrawl()
        account_page.withdrawl("1000000")
        assert account_page.is_failed_withdrawl(), "Ожидалось, что транзакция пройдет не успешно"

        account_page.go_to_transactions()
        assert account_page.get_last_transaction_amount()!="100000", f"Ожидалась транзакиця {1000000}, получена {account_page.get_last_transaction_amount()}"

    def test_check_balance(self, driver, customer_with_transactions):
        """Тестирование соответствия: баланс аккаунта = баланс, вычисленный по транзакциям"""
        account_page = AccountPage(driver)
        
        account_page.go_to_transactions()
        trans_bal = account_page.get_balance_from_transactions()
        account_page.load(driver)
        acc_bal = account_page.get_balance()
        assert trans_bal==acc_bal, f"Баланс по транзакицям: {trans_bal}, баланс на аккаунте: {acc_bal}"

    def test_withdrawl_all(self, driver, customer_with_balance):
        """Тестирования снятия всех средств с баланса"""
        account_page = AccountPage(driver)

        account_page.go_to_withdrawl()
        withdrawl_value = account_page.get_balance()
        account_page.withdrawl(str(withdrawl_value))

        assert account_page.is_success_withdrawl(), "Транзакция прошла не успешно"
        assert account_page.get_balance()==0, "Баланс не нулевой"

    def test_reset_transactions(self, driver, customer_with_transactions):
        """Тестирование сброса транзакций"""
        account_page = AccountPage(driver)
        account_page.go_to_transactions()

        count_before_reset = account_page.count_transactions()
        assert count_before_reset==6, f"Количество транзакций не совпадает, получено {count_before_reset}"
        account_page.reset_transactions()
        count_after_reset = account_page.count_transactions_after_reset()
        assert count_after_reset==0, f"После удаления остались транзакции {count_after_reset}"
        account_page.back_from_transactions()
        balance = account_page.get_balance()

        assert balance==0,f"Balance {balance}"

    def test_search_and_delete_customer(self, driver, created_customer):
        """Тестирование поиска и удаления кастомера"""
        banking_app_page = BankingAppPage(driver)
        banking_manager_login_page = BankManagerLoginPage(driver)

        banking_app_page.go_to_bank_manager_login()
        banking_manager_login_page.go_to_customers()
        customer = created_customer.split()
        first_name = customer[0]
        last_name = customer[1]

        assert banking_manager_login_page.search_customer(first_name, last_name), "Клиент не найден в списке"
        banking_manager_login_page.delete_customer(first_name, last_name)
        assert not banking_manager_login_page.search_customer(first_name, last_name), "Клиент найден в списке, не удален"