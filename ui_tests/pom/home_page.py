from playwright.sync_api import Page
from base_script import ConfigLoader
from ui_tests.pom import locators
from logger import logging_setup


cl = ConfigLoader()
logger = logging_setup()


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def load_home_page(self):
        self.page.goto(cl.homepage_url)
        logger.debug("Opening the homepage with URL: {}".format(cl.homepage_url))

    def nav_page(self, page_locator, url):
        self.page.click(page_locator)
        self.page.wait_for_selector(page_locator)
        logger.debug("Navigating to the URL: {}".format(url))
        return True

    def verify_logo(self):
        logo = self.page.locator(locators.LOGO)
        if logo.is_visible():
            return True

    def verify_menu_bar(self):
        menu_bar = self.page.locator(locators.MENU_BAR)
        if menu_bar.is_visible():
            return True

    def verify_menu_items(self, menu_locators):
        for locator in menu_locators:
            menu_locator = self.page.locator(locator)
            if menu_locator.is_visible():
                return True
