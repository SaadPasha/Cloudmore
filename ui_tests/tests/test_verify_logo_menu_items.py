import allure

from base_script import ConfigLoader
from logger import logging_setup
from pom import locators

cl = ConfigLoader()
logger = logging_setup()

STEP_1 = "Navigate to the homepage."
STEP_2 = "Verify that the logo exists"
STEP_3 = "Verify that the menu bar is visible with the following items: \n- Platform\n- Blog\n- Case Studies \n- About Us"
STEP_4 = "Verify logo and menu items are visible for the Platform, Blog, Case-Studies and About-US pages"


@allure.title("Verify Logo and Menu items")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_logo(homepage_functions):
    """
    Testcase function to verify if the Logo and Menu Items exists on the following pages:
    - Home Page
    - Platform Page
    - Blog Page
    - Case Studies
    - About Us
    Returns: True
    """
    menu_locators = [locators.MENU_PLATFORM, locators.MENU_BLOG, locators.MENU_ABOUT_US, locators.MENU_CASE_STUDIES]

    with allure.step(STEP_1):
        homepage_functions.load_home_page()

    with allure.step(STEP_2):
        assert homepage_functions.verify_logo() is True

    with allure.step(STEP_3):
        assert homepage_functions.verify_menu_bar() is True
        assert homepage_functions.verify_menu_items(menu_locators=menu_locators) is True

    with allure.step(STEP_4):
        assert homepage_functions.nav_page(page_locator=locators.MENU_PLATFORM, url=cl.platform_url) is True
        assert homepage_functions.verify_logo() is True
        assert homepage_functions.verify_menu_bar() is True
        assert homepage_functions.verify_menu_items(menu_locators=menu_locators) is True

        assert homepage_functions.nav_page(page_locator=locators.MENU_BLOG, url=cl.blog_url) is True
        assert homepage_functions.verify_logo() is True
        assert homepage_functions.verify_menu_bar() is True
        assert homepage_functions.verify_menu_items(menu_locators=menu_locators) is True

        assert homepage_functions.nav_page(page_locator=locators.MENU_CASE_STUDIES, url=cl.case_studies_url) is True
        assert homepage_functions.verify_logo() is True
        assert homepage_functions.verify_menu_bar() is True
        assert homepage_functions.verify_menu_items(menu_locators=menu_locators) is True

        assert homepage_functions.nav_page(page_locator=locators.MENU_ABOUT_US, url=cl.about_url) is True
        assert homepage_functions.verify_logo() is True
        assert homepage_functions.verify_menu_bar() is True
        assert homepage_functions.verify_menu_items(menu_locators=menu_locators) is True
