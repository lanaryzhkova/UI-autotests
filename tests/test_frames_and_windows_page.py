import allure

from pages.frames_and_windows_page import FramesAndWindowsPage

@allure.epic("Frames and Windows")
@allure.feature("New Tab and Switch")

class TestFramesAndWindowsPage:
    """Тесты для страницы Frames and Windows"""

    @allure.story("Тестирование открытия новой вкладки и переключения между ними")
    def test_new_tab_and_switch(self, driver):
        """Тестирование открытия новой вкладки и переключения между ними"""
        windows_page = FramesAndWindowsPage(driver)
        windows_page.load()

        windows_page.switch_to_iframe()
        windows_page.click_new_tab()
        windows_page.switch_to_new_tab()
        windows_page.click_new_tab()
        
        assert windows_page.count_handles() == 3, "Количество открытых вкладок не равно 3"
