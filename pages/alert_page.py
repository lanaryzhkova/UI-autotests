import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertPage(BasePage):
    """Класс для работы с алертами на странице"""

    URL = "https://way2automation.com/way2auto_jquery/alert.php#load_box"

    INPUT_ALERT_TAB = (By.XPATH, "//a[text()='Input Alert']")
    IFRAME = (By.CSS_SELECTOR, "#example-1-tab-2 iframe")
    SHOW_ALERT_BUTTON = (By.CSS_SELECTOR, "button[onclick*='myFunction()']")
    WELCOME_TEXT = (By.ID, "demo")


    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Нажатие на вкладку 'Input Alert'")
    def click_input_alert_tab(self):
        """Нажатие на вкладку 'Input Alert'"""
        input_alert_tab = self.find_element(self.INPUT_ALERT_TAB)
        input_alert_tab.click()

    @allure.step("Переключение на iframe во вкладке 'Input Alert'")
    def switch_to_iframe(self):
        """Переключение на iframe на странице"""
        iframe = self.find_element(self.IFRAME)
        self.switch_to_frame(iframe)

    @allure.step("Нажатие на кнопку демонстрации алерта")
    def click_show_alert_button(self):
        """Нажатие на кнопку демонстрации алерта"""
        alert_button = self.find_element(self.SHOW_ALERT_BUTTON)
        alert_button.click()

    @allure.step("Проверка отображения введенного текста на странице")
    def is_text_displayed(self, text: str) -> bool:
        """Проверяет отображение текста на странице
        Args:
            text: текст для проверки
        Returns:
            True, если текст отображается, иначе False
        """
        welcome_text = self.find_element(self.WELCOME_TEXT)
        return text in welcome_text.text