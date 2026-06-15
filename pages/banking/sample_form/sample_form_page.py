from pages.base_page import BasePage
from .sample_form_locators import SampleFormLocators
from data.data import PageUrls
from selenium.webdriver.support.select import Select
from utils.utils import get_longest_word_from_elements


class SampleFormPage(BasePage):
    """Страница Sample Form"""

    def load(self):
        """Загрузить страницу"""
        self.open(PageUrls.SAMPLE_FORM_URL)
        self.wait.wait_for_url(PageUrls.SAMPLE_FORM_URL)
        return self

    def register(self, user: dict) -> "SampleFormPage":
        """Зарегистрироваться"""
        user["about"] = self.calc_text_for_about()

        self.send_keys_to_input(SampleFormLocators.FIRST_NAME_INPUT, user["first_name"])
        self.send_keys_to_input(SampleFormLocators.LAST_NAME_INPUT, user["last_name"])
        self.send_keys_to_input(SampleFormLocators.EMAIL_INPUT, user["email"])
        self.send_keys_to_input(SampleFormLocators.PASSWORD_INPUT, user["password"])
        self.send_keys_to_input(SampleFormLocators.ABOUT_TEXTAREA, user["about"])

        for hobby in user["hobbies"]:
            self.click(self.find_element(SampleFormLocators.hobby_checkbox(hobby)))

        gender_select = Select(self.find_element(SampleFormLocators.GENDER_SELECTOR))
        gender_select.select_by_visible_text(user["gender"])

        self.click(self.find_element(SampleFormLocators.SUBMIT_BUTTON))
        return self

    def calc_text_for_about(self) -> str:
        """Вычислить текст для About"""
        checkboxes = self.find_elements(SampleFormLocators.HOBBIES_CHECKBOXES)
        longest_hobby = get_longest_word_from_elements(checkboxes)
        return f"Самое длинное слово из предложенных хобби - {longest_hobby}"

    def is_success_message_displayed(self) -> bool:
        """Проверить отображение сообщения об успешой регистрации"""
        return self.is_visible(SampleFormLocators.SUCCESS_MESSAGE)
