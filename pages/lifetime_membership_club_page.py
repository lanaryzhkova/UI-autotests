from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LifetimeMembershipClubPage(BasePage):
    """Страница Lifetime Membership Club"""

    URL = "https://www.way2automation.com/lifetime-membership-club/"

    HEADER_TEXT = (By.TAG_NAME, "h1")

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    def get_header_text(self) -> str:
        """Получить текст заголовка страницы"""
        header_element = self.find_element(self.HEADER_TEXT)
        return header_element.text.strip().lower()
