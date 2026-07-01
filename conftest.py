import base64

import allure
import pytest
from allure_commons.types import AttachmentType
from drivers.driver_factory import DriverFactory

pytest_plugins = ["fixtures.customer_state_fixtures", "fixtures.auth_cookies_fixture"]


@pytest.fixture
def driver(request):
    driver = DriverFactory.create_driver(
        browser=request.config.getoption("--browser"),
        remote=request.config.getoption("--remote"),
        hub_url=request.config.getoption("--hub"),
    )

    yield driver

    driver.quit()

def pytest_selenium_capture_debug(item, report, extra):
    for log_type in extra:
        if log_type["name"] == "Screenshot":
            content = base64.b64decode(log_type["content"].encode("utf-8"))
            allure.attach(
                content,
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG,
            )

def pytest_addoption(parser):
    """Добавление опций командной строки для выбора браузера и режима запуска"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузеры: chrome, firefox, edge, ie",
    )

    parser.addoption(
        "--remote",
        action="store_true",
        help="Запуск через Selenium Grid",
    )

    parser.addoption(
        "--hub",
        action="store",
        default="http://localhost:4444",
    )