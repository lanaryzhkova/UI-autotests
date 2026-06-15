from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы для главной страницы"""
    HEADER_NAVIGATION_SECTION = (By.ID, 'site-navigation')
    HEADER_NAVIGATION_LIST = (By.ID, 'ast-hf-menu-1')
    HEADER_NAVIGATION_SUBMENU = (By.CSS_SELECTOR, '.sub-menu')
    REGISTER_BUTTON = (By.LINK_TEXT, 'Register Now')
    COURSE_SLIDER = (By.CSS_SELECTOR, '[data-id="50827c4"]')
    FOOTER_SECTION = (By.CSS_SELECTOR, '[data-id="573bc308"]')
    COURSES_NEXT_BUTTON = (By.CSS_SELECTOR, '.swiper-button-next-c50f9f0')
    COURSES_PREV_BUTTON = (By.CSS_SELECTOR, '.swiper-button-prev-c50f9f0')
    MENU_LINK = (By.CSS_SELECTOR, '.menu-link')