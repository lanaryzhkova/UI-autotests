import base64

import allure
import pytest
from allure_commons.types import AttachmentType

pytest_plugins = ["fixtures.customer_state_fixtures", "fixtures.auth_cookies_fixture"]


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    return firefox_options


@pytest.fixture
def edge_options(edge_options):
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--window-size=1920,1080")
    return edge_options


@pytest.fixture
def ie_options(ie_options):
    ie_options.ignore_protected_mode_settings = True
    ie_options.ignore_zoom_level = True
    return ie_options


@pytest.fixture
def driver(selenium):
    return selenium


def pytest_selenium_capture_debug(item, report, extra):
    for log_type in extra:
        if log_type["name"] == "Screenshot":
            content = base64.b64decode(log_type["content"].encode("utf-8"))
            allure.attach(
                content,
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG,
            )
