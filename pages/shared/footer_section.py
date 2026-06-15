from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.data import expected_about_us_info


class FooterSection(BasePage):
    footer_element = (By.CSS_SELECTOR, '[data-elementor-type="footer"]')
    about_us_info = (By.CSS_SELECTOR, '[data-id="5ca7d707"]')

    def get_about_us_info(self):
        about_us_element = self.find_element(self.about_us_info)
        return about_us_element.text.strip()
    
    def is_footer_displayed(self):
        return self.is_visible(self.footer_element)

    def assert_about_us_content(self):
        about_us_info = self.get_about_us_info()
        for info in expected_about_us_info:
            assert info in about_us_info, f"Раздел About us  не содержит ожидаемый текст: {info}"

        return self
    
    def get_footer_element(self):
        return self.find_element(self.footer_element)