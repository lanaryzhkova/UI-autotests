import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class FramesAndWindowsPage(BasePage):
    """Класс для работы со страницей Frames and Windows"""

    URL = "https://way2automation.com/way2auto_jquery/frames-and-windows.php#load_box"

    NEW_TAB_A = (By.XPATH, "//a[text()='New Browser Tab']")
    IFRAME = (By.CSS_SELECTOR, "iframe.demo-frame")

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Нажать на ссылку 'New Browser Tab'")
    def click_new_tab(self):
        """Кликает на ссылку 'New Browser Tab'"""
        new_tab_link = self.find_element(self.NEW_TAB_A)
        new_tab_link.click()

    @allure.step("Переключение на iframe")
    def switch_to_iframe(self):
        """Переключается на iframe на странице"""
        iframe = self.find_element(self.IFRAME)
        self.switch_to_frame(iframe)
