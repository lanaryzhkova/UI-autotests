from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement

from utils.wait_helper import WaitHelper


class BasePage:
    """Базовый класс"""

    URL = "https://www.way2automation.com/"

    def __init__(self, driver):
        """Инициализация базового класса"""
        self.driver = driver
        self.base_url = BasePage.URL
        self.wait = WaitHelper(driver, 10)

    def open(self, url: str) -> "BasePage":
        """Открывает страницу по ссылке"""
        self.driver.get(url or self.base_url)
        return self

    def find_element(self, locator: tuple) -> WebElement:
        """Поиск элемента по локатору"""
        return self.wait.wait_for_element_visible(locator)

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Поиск элементов по локатору"""
        return self.wait.wait_for_all_elements_visible(locator)

    def find_elements_safe(self, locator):
        """Поиск элементов по локатору без ожидания"""
        try:
            return self.wait.wait_for_all_elements_present(locator)
        except TimeoutException:
            return []

    def scroll_to(self, elem) -> "BasePage":
        """Прокрутка до элемента"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'start'});", elem
        )
        return self

    def click(self, element: WebElement) -> "BasePage":
        """Метод нажатия на элемент"""
        elem = element
        self.scroll_to(elem)
        elem.click()
        return self

    def send_keys_to_input(self, locator: tuple, text: str):
        """Метод для ввода текста"""
        elem = self.wait.wait_for_element_clickable(locator)
        elem.clear()
        elem.send_keys(text)
        return self

    def text_of(self, element: WebElement) -> str:
        """Метод получения текста элемента"""
        return element.text.strip()

    def is_visible(self, locator: tuple) -> bool:
        """Метод проверки видимости элемента"""
        try:
            self.wait.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def hover_over_element(self, element: WebElement) -> "BasePage":
        """Метод наведения курсора на элемент"""
        ActionChains(self.driver).move_to_element(element).perform()
        return self

    def alert_is_present(self) -> bool:
        """Метод проверки наличия алерта"""
        try:
            self.wait.wait_for_alert()
            return True
        except TimeoutException:
            return False

    def accept_alert(self):
        try:
            self.wait.wait_for_alert()
            alert = Alert(self.driver)
            alert.accept()
        except TimeoutException:
            return False

    def get_attribute_of_element(
        self, element: WebElement, attribute: str
    ) -> str | int | float | None:
        """Метод получения атрибута элемента"""
        return element.get_attribute(attribute)

    def get_current_url(self) -> str:
        """Метод получения текущего URL"""
        return self.driver.current_url
