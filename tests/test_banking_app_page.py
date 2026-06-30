import allure

from data.data import customer
from data.data import sample_form_user as user
from pages.banking.account.account_page import AccountPage
from pages.banking.bank_manager.bank_manager_login import BankManagerLoginPage
from pages.banking.banking_app.banking_app_page import BankingAppPage
from pages.banking.customer_page import CustomerPage
from pages.banking.sample_form.sample_form_page import SampleFormPage


@allure.epic("Banking Application")
class TestBankingAppPage:
    """Тесты для страницы BankingApp"""

    @allure.feature("Sample Form")
    @allure.story("Успешная регистрация")
    @allure.severity(allure.severity_level.NORMAL)
    def test_valid_fill_sample_form(self, driver):
        """Тестирование успешного заполнения Sample Form"""
        banking_app_page = BankingAppPage(driver)
        sample_form_page = SampleFormPage(driver)
        banking_app_page.load()

        banking_app_page.go_to_sample_form()
        sample_form_page.register(user)

        assert sample_form_page.is_success_message_displayed(), (
            "Сообщение об успешной отправке формы не отображается"
        )

    @allure.feature("Bank Manager")
    @allure.story("Добавление клиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_customer(self, driver):
        """Тестирование добавления кастомера"""
        banking_app_page = BankingAppPage(driver)
        banking_manager_login_page = BankManagerLoginPage(driver)
        banking_app_page.load()
        banking_app_page.go_to_bank_manager_login()
        banking_manager_login_page.go_to_add_customer()

        banking_manager_login_page.add_customer(
            customer["first_name"], customer["last_name"], customer["postcode"]
        )

        assert banking_manager_login_page.alert_is_present(), (
            "Алерт с подтверждением добавления клиента не отображается"
        )
        banking_manager_login_page.accept_alert()

    @allure.feature("Bank Manager")
    @allure.story("Открытие счета")
    def test_open_account(self, driver, created_customer):
        """Тестирование открытия (создания) аккаунта"""
        banking_app_page = BankingAppPage(driver)
        banking_manager_login_page = BankManagerLoginPage(driver)
        banking_app_page.go_to_bank_manager_login()
        banking_manager_login_page.go_to_open_account()

        banking_manager_login_page.open_account(created_customer, "Dollar")

        assert banking_manager_login_page.alert_is_present(), (
            "Алерт с подтверждением открытия аккаунта не отображается"
        )
        banking_manager_login_page.accept_alert()

    @allure.feature("Customer")
    @allure.story("Вход в аккаунт")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_customer_login(self, driver, created_customer):
        """Тестирования входа в аккаунт кастомера"""
        banking_app_page = BankingAppPage(driver)
        banking_manager_login_page = BankManagerLoginPage(driver)
        customer_page = CustomerPage(driver)
        banking_app_page.go_to_customer_login()

        customer_page.login_customer(created_customer)
        banking_manager_login_page.wait.wait_for_url(AccountPage.URL)

        assert banking_manager_login_page.get_current_url() == AccountPage.URL, (
            "Переход на страницу аккаунта не произведен"
        )
        assert "Welcome " + created_customer in customer_page.check_account_welcome(
            created_customer
        )
