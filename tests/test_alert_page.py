import allure

from pages.alert_page import AlertPage

@allure.epic("Alert Page")

class TestAlertPage:
    """Тесты для страницы Alert Page"""
    @allure.feature("Input Alert Test")
    @allure.story("Тестирование ввода текста в алерт и его отображения на странице")
    def test_input_alert(self, driver):
        """Тестирование ввода текста в алерт и его отображения на странице"""
        text = "Test User"

        alert_page = AlertPage(driver)
        alert_page.load()

        alert_page.click_input_alert_tab()
        alert_page.switch_to_iframe()
        alert_page.click_show_alert_button()
        alert_page.input_text_in_alert(text)
        alert_page.accept_alert()

        assert alert_page.is_text_displayed(text), "Введенный текст не отображается на странице"
