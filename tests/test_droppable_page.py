import allure

from pages.droppable_page import DroppablePage


@allure.epic("Droppable Page")
@allure.feature("Drag and Drop")

class TestDroppablePage:
    """Тесты для страницы Droppable"""

    @allure.story("Проверка перетаскивания элемента")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_drag_and_drop(self, driver):
            """Тестирование перетаскивания элемента"""
            droppable_page = DroppablePage(driver)
            droppable_page.load()
    
            droppable_page.drag_and_drop_element()
    
            assert droppable_page.is_element_dropped(), (
                "Элемент не был успешно перетащен"
            )