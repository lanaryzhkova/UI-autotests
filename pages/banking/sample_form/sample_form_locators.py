from selenium.webdriver.common.by import By


class SampleFormLocators:
    """Локаторы для Sample Form"""

    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    HOBBIES_CHECKBOXES = (By.NAME, "hobbies")
    GENDER_SELECTOR = (By.ID, "gender")
    ABOUT_TEXTAREA = (By.ID, "about")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Register']")
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    GENDER_OPTION = (By.TAG_NAME, "option")

    @staticmethod
    def hobby_checkbox(hobby_value: str) -> tuple:
        """Локатор для конкретного хобби"""
        return (By.XPATH, f"//input[@name='hobbies'][@value='{hobby_value}']")
