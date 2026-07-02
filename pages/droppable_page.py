import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DroppablePage(BasePage):
    """Страница с элементами, которые можно перетаскивать"""

    URL = "https://way2automation.com/way2auto_jquery/droppable.php#load_box"

    DRAGGABLE_ELEMENT = (By.ID, "draggable")
    DROPPABLE_ELEMENT = (By.ID, "droppable")
    IFRAME = (By.CSS_SELECTOR, "iframe.demo-frame")

    def load(self):
        """Загрузить страницу"""
        self.open(self.URL)
        self.wait.wait_for_url(self.URL)

    @allure.step("Перетаскивание элемента Draggable в область Droppable")
    def drag_and_drop_element(self):
        """Перетаскивает элемент в целевую область"""
        iframe = self.find_element(self.IFRAME)
        self.switch_to_frame(iframe)
        draggable_element = self.find_element(self.DRAGGABLE_ELEMENT)
        droppable_element = self.find_element(self.DROPPABLE_ELEMENT)

        self.drag_and_drop(draggable_element, droppable_element)

    @allure.step("Проверка текста принимающего элемента после перетаскивания")
    def is_element_dropped(self) -> bool:
        """Проверяет, был ли элемент успешно перетащен в целевую область
        Returns:
            True, если элемент был успешно перетащен, иначе False
        """
        droppable_element = self.find_element(self.DROPPABLE_ELEMENT)
        is_dropped = droppable_element.text.strip() == "Dropped!"

        return is_dropped