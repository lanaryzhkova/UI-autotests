import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasicAuthPage(BasePage):

    URL = "https://www.httpwatch.com/httpgallery/authentication/#showExample10"

    DISPLAY_IMAGE_BUTTON = (By.ID, "displayImage")
    IMAGE = (By.ID, "downloadImg")

    username = "httpwatch"
    password = "httpwatch"

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def login(self):
        """Выполнить авторизацию на странице"""
        self.basic_auth(self.username, self.password)
        self.load()
        self.click(self.find_element(self.DISPLAY_IMAGE_BUTTON))
        
    def is_image_displayed(self) -> bool:
        """Проверяет отображение изображения на странице"""
        image = self.find_element(self.IMAGE)
        return image.is_displayed()
    
