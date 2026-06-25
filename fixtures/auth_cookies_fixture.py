import allure
import pytest

from pages.demo_auth_page import DemoAuthPage
from utils.cookie_utils import cookies_exist, load_cookies, save_cookies


@pytest.fixture
def authorized_user(driver):
    """Фикстура для авторизации пользователя (проверяет наличие cookie)"""

    valid_username = "practice"
    valid_password = "SuperSecretPassword!"

    auth_page = DemoAuthPage(driver)
    auth_page.load()

    if cookies_exist():
        with allure.step("Куки на месте, использую"):
            driver.delete_all_cookies() #очищаю куки, чтобы не конфликтовали
            load_cookies(driver)
            driver.refresh()
    
    else:
        with allure.step("Куков нет, логинюсь"):
            auth_page.login(valid_username, valid_password)
            if auth_page.is_logged_in():
                with allure.step('Сохраняю куки'):
                    save_cookies(driver)
            else:
                raise Exception("Login failed, cookies not saved")

    return auth_page