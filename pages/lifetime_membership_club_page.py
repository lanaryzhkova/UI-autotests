from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.data import PageUrls


class LifetimeMembershipClubPage(BasePage):
    """Страница Lifetime Membership Club"""
    HEADER_TEXT = (By.TAG_NAME, 'h1')

    def load(self):
        """Загрузить страницу"""
        self.open(PageUrls.LIFETIME_MEMBERSHIP_URL)
        self.wait.wait_for_url(PageUrls.LIFETIME_MEMBERSHIP_URL)
        return self

    def get_header_text(self):
        """Получить текст заголовка страницы"""
        header_element = self.find_element(self.HEADER_TEXT)
        return header_element.text.strip().lower()