from pages.base_page import BasePage

from .home_locators import HomePageLocators


class HomePage(BasePage):
    """Главная страница"""

    def load(self):
        """Загрузить страницу"""
        self.open(BasePage.URL)
        self.wait.wait_for_url(BasePage.URL)

    def get_header_navigation_links(self) -> list:
        """Получить ссылки из меню навигации"""
        navigation_list = self.find_element(HomePageLocators.HEADER_NAVIGATION_LIST)
        links = navigation_list.find_elements(*HomePageLocators.MENU_LINK)
        return links

    def get_header_navigation_submenu_links(self) -> list:
        """Получить ссылки из подменю навигации"""
        submenu = self.find_element(HomePageLocators.HEADER_NAVIGATION_SUBMENU)
        links = submenu.find_elements(*HomePageLocators.MENU_LINK)
        return links

    def assert_is_header_elements_visible(self) -> bool:
        """Проверить видимость элементов шапки"""
        elements = {
            "Навигация": HomePageLocators.HEADER_NAVIGATION_SECTION,
            "Кнопка регистрации": HomePageLocators.REGISTER_BUTTON,
            "Список курсов": HomePageLocators.COURSE_SLIDER,
            "Футер": HomePageLocators.FOOTER_SECTION,
        }

        for element_name, locator in elements.items():
            assert self.is_visible(locator), f"{element_name} отсутствует"

        return True

    def is_header_navigation_visible(self) -> bool:
        """Проверить видимость навигации в хедере"""
        return self.is_visible(HomePageLocators.HEADER_NAVIGATION_SECTION)

    def hover_over_menu_item(self, text: str) -> "HomePage":
        """Навести курсор на элемент меню по тексту"""
        nav_links = self.get_header_navigation_links()
        link = next((link for link in nav_links if link.text.strip() == text), None)
        assert link, f"Элемент меню '{text}' не найден"
        self.hover_over_element(link)
        return self

    def click_submenu_item(self, text: str) -> "HomePage":
        """Кликнуть на элемент подменю по тексту"""
        submenu_links = self.get_header_navigation_submenu_links()
        link = next((link for link in submenu_links if link.text.strip() == text), None)
        assert link, f"Элемент подменю '{text}' не найден"
        self.click(link)
        return self
