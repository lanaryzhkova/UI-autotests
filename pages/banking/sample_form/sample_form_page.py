import allure
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils.utils import get_longest_word_from_elements

from .sample_form_locators import SampleFormLocators


class SampleFormPage(BasePage):
    """Страница Sample Form"""

    URL = "https://www.way2automation.com/angularjs-protractor/banking/registrationform.html"

    @allure.step("Загрузить страницу Sample Form")
    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Зарегистрироваться")
    def register(self, user: dict) -> "SampleFormPage":
        """
        Зарегистрироваться
        Args:
            user: Данные пользователя
        """
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

    @allure.step("Вычислить текст для About")
    def calc_text_for_about(self) -> str:
        """Вычислить текст для About
        Returns:
            Текст для About"""
        checkboxes = self.find_elements(SampleFormLocators.HOBBIES_CHECKBOXES)
        longest_hobby = get_longest_word_from_elements(checkboxes)
        return f"Самое длинное слово из предложенных хобби - {longest_hobby}"

    def is_success_message_displayed(self) -> bool:
        """Проверить отображение сообщения об успешой регистрации
        Returns:
            True, если сообщение отображается, иначе False"""
        return self.is_visible(SampleFormLocators.SUCCESS_MESSAGE)
