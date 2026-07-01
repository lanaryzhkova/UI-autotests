from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.ie.service import Service as IeService


class DriverFactory:
    """Класс, создающий различные WebDriver в зависимости от входных параметров"""
    WINDOWS_DRIVERS = Path(__file__).parent / "windows"

    @staticmethod
    def create_driver(
        browser: str,
        remote: bool = False,
        hub_url: str = "http://localhost:4444",
        headless: bool = True,
    ):
        """
        Метод создания экземпляра WebDriver для указанного браузера
        Args:
            browser: Название браузера (chrome, firefox, edge, ie)
            remote: Использовать ли Selenium Grid
            hub_url: URL Selenium Hub при запуске через Grid
            headless: Запускать ли браузер в headless режиме

        Returns:
            Экземпляр WebDriver
        """
        browser = browser.lower()

        options = DriverFactory._create_options(browser, headless)

        if remote:
            return webdriver.Remote(
                command_executor=hub_url,
                options=options,
            )

        return DriverFactory._create_local(browser, options)
    
    @staticmethod
    def _create_local(browser, options):
        """
        Метод создания локального WebDriver без использования Selenium Grid
        Args:
            browser: Название браузера
            options: Настройки браузера

        Returns:
            Экземпляр локального WebDriver

        Raises:
            ValueError: Если указан неизвестный браузер
        """
        if browser == "chrome":
            return webdriver.Chrome(options=options)

        if browser == "firefox":
            return webdriver.Firefox(options=options)

        if browser == "edge":
            return webdriver.Edge(options=options)

        if browser == "ie":

            service = IeService(
                DriverFactory.WINDOWS_DRIVERS / "IEDriverServer.exe"
            )

            return webdriver.Ie(
                service=service,
                options=options,
            )

        raise ValueError(f"Неизвестный браузер: {browser}")
    
    @staticmethod
    def _create_options(browser, headless):
        """
        Метод создания настроек браузера
        Args:
            browser: Название браузера
            headless: Включить ли headless режим

        Returns:
            Объект Options выбранного браузера

        Raises:
            ValueError: Если указан неизвестный браузер
        """
        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-notifications")

            return options

        if browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            return options

        if browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--window-size=1920,1080")

            return options

        if browser == "ie":

            options = IeOptions()

            options.ignore_protected_mode_settings = True
            options.ignore_zoom_level = True
            options.require_window_focus = False

            return options

        raise ValueError(browser)