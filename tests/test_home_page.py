from pages.home.home_page import HomePage
from pages.shared.header_contacts_section  import HeaderContactsSection
from pages.shared.footer_section import FooterSection
from pages.lifetime_membership_club_page import LifetimeMembershipClubPage
from data.data import PageUrls


class TestHomePage:
    def test_home_page_opened(self, driver):
        home_page = HomePage(driver)
        header_contacts_section = HeaderContactsSection(driver)
        home_page.load()

        assert header_contacts_section.is_header_contacts_visible(), "Контактная информация в шапке отсутствует"
        home_page.assert_is_header_elements_visible()

    def test_header_contacts(self, driver):
        home_page = HomePage(driver)
        header_contacts_section = HeaderContactsSection(driver)
        home_page.load()
        
        assert header_contacts_section.is_header_contacts_visible(), "Контактная информация в шапке не отображается"
        header_contacts_section.assert_contact_links()
        header_contacts_section.assert_social_links()

    def test_footer_displayed(self, driver):
        home_page = HomePage(driver)
        footer_section = FooterSection(driver)
        home_page.load()

        footer_section.assert_about_us_content()
        assert footer_section.is_footer_displayed(), "Футер не отображается на главной странице"

    def test_navigation_with_scroll(self, driver):
        home_page = HomePage(driver)
        footer_section = FooterSection(driver)
        home_page.load()

        visibility_before_scroll = home_page.is_header_navigation_visible()
        home_page.scroll_to(footer_section.get_footer_element())
        visibility_after_scroll = home_page.is_header_navigation_visible()

        assert visibility_before_scroll == visibility_after_scroll, "Меню навигации не отображается после прокрутки"

    def test_navigation_goto_link(self, driver):
        home_page = HomePage(driver)
        lifetime_membership_page = LifetimeMembershipClubPage(driver)
        home_page.load()

        home_page.hover_over_menu_item("All Courses")
        home_page.click_submenu_item("Lifetime Membership")

        assert home_page.wait.wait_for_url(PageUrls.LIFETIME_MEMBERSHIP_URL), "Переход по ссылке 'Lifetime Membership Club' не произошел"
        assert lifetime_membership_page.get_header_text() == "lifetime membership club", "Заголовок страницы 'Lifetime Membership Club' не соответствует ожидаемому"