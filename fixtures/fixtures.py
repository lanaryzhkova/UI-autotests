import pytest

from pages.banking.account.account_page import AccountPage
from pages.banking.banking_app.banking_app_page import BankingAppPage
from pages.banking.banking_manager.bank_manager_login import BankingManagerLoginPage
from pages.banking.customer_page import CustomerPage
from data.data import customer, PageUrls


@pytest.fixture
def created_customer(driver):
    """Кастомер добавлен в сервис"""
    banking_app_page = BankingAppPage(driver)
    banking_manager_login_page = BankingManagerLoginPage(driver)

    banking_app_page.load()
    banking_app_page.go_to_bank_manager_login()
    banking_manager_login_page.go_to_add_customer()

    banking_manager_login_page.add_customer(
        customer["first_name"],
        customer["last_name"],
        customer["postcode"]
    )

    banking_manager_login_page.accept_alert()
    banking_app_page.load()

    return f'{customer["first_name"]} {customer["last_name"]}'

@pytest.fixture
def customer_with_account(driver, created_customer):
    """Кастомер с открытым аккаунтом"""
    banking_app_page = BankingAppPage(driver)
    banking_manager_login_page = BankingManagerLoginPage(driver) 

    banking_app_page.load() 
    banking_app_page.go_to_bank_manager_login()
    banking_manager_login_page.go_to_open_account()
    banking_manager_login_page.open_account(created_customer, "Dollar")

    assert banking_manager_login_page.alert_is_present(), "Алерт с подтверждением открытия аккаунта не отображается"

    banking_manager_login_page.accept_alert()

    return created_customer

@pytest.fixture
def customer_is_logged_in(driver, customer_with_account):
    """Кастомер вошёл в аккаунт"""
    banking_app_page = BankingAppPage(driver)
    banking_manager_login_page = BankingManagerLoginPage(driver) 
    customer_page = CustomerPage(driver)

    banking_app_page.load() 
    banking_app_page.go_to_customer_login()
    customer_page.login_customer(customer_with_account)
    banking_manager_login_page.wait.wait_for_url(PageUrls.CUSTOMER_ACCOUNT_URL)

    assert banking_manager_login_page.get_current_url() == PageUrls.CUSTOMER_ACCOUNT_URL, "Переход на страницу аккаунта не произведен"

    return customer_with_account

@pytest.fixture
def customer_with_balance(driver, customer_is_logged_in):
    """Кастомер с балансом 10000"""
    account_page = AccountPage(driver)

    account_page.deposit_succesfully("10000")

    return customer_is_logged_in

@pytest.fixture
def customer_with_transactions(driver, customer_is_logged_in):
    """Кастомер с историей транзакций"""
    account_page = AccountPage(driver)

    account_page.deposit_succesfully("10000")
    account_page.deposit_succesfully("20000")
    account_page.withdrawl_successfully("5600")
    account_page.withdrawl_successfully("560")
    account_page.deposit_succesfully("200")
    account_page.withdrawl_successfully("1060")

    return customer_is_logged_in