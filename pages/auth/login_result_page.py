from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.data import PageUrls


class LoginResultPage(BasePage):
    TEXT_ELEMENT = (By.XPATH, "//*[contains(text(), \"You're logged in!!\")]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), \"Logout\")]")

    def load(self):
        self.open(PageUrls.LOGIN_RESULT_URL)
        self.wait.wait_for_url(PageUrls.LOGIN_RESULT_URL)
        return self
    
    def is_logged_in(self):
        return self.is_visible(self.TEXT_ELEMENT)

    def logout(self):
        self.click(self.find_element(self.LOGOUT_BUTTON))
        return self