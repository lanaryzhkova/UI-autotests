from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.data import expected_contact_links, expected_social_links


class HeaderContactsSection(BasePage):
    """Хедер с контактной информацией"""
    header_contacts_element = (By.CSS_SELECTOR, '[data-section="section-hb-html-1"]')
    contact_links = (By.CSS_SELECTOR, '[data-section="section-hb-html-1"] a')
    social_links = (By.CSS_SELECTOR, '[data-section="section-hb-social-icons-1"] a')

    def get_contact_links(self) -> list:
        """Получить ссылки на контакты"""
        contact_links = self.find_elements(self.contact_links)
        return [link.get_attribute('href') for link in contact_links]
    
    def get_social_links(self) -> list:
        """Получить ссылки на соцсети"""
        social_links = self.find_elements(self.social_links)
        return [link.get_attribute('href') for link in social_links]

    def is_header_contacts_visible(self) -> bool:
        """Проверка отображения контактов"""
        return self.is_visible(self.header_contacts_element)
    
    def assert_contact_links(self):
        """Проверка ссылок на контакты"""
        contact_links = self.get_contact_links()
        assert set(contact_links) == set(expected_contact_links), f"Ссылки {contact_links} не соответствуют ожидаемым ссылкам на контакты {expected_contact_links}"

    def assert_social_links(self):
        """Проверка ссылок на соцсети"""
        social_links = self.get_social_links()
        assert set(social_links) == set(expected_social_links), f"Ссылки {social_links} не соответствуют ожидаемым ссылкам на соцсети {expected_social_links}"
    
    
