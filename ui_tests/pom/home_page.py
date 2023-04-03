from playwright.sync_api import Page
from base_script import ConfigLoader
import locators
from logger import logging_setup


cl = ConfigLoader()
logger = logging_setup()


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def load_home_page(self):
        """
        Loads homepage
        Returns: None
        """
        self.page.goto(cl.homepage_url)
        logger.debug("Opening the homepage with URL: {}".format(cl.homepage_url))

    def nav_page(self, page_locator, url):
        """
        Navigates to a specific page using clicks
        Args:
            page_locator: button to click
            url: the URL navigating to - for logging
        Returns: True
        """
        self.page.click(page_locator)
        self.page.wait_for_selector(page_locator)
        logger.debug("Navigating to the URL: {}".format(url))
        return True

    def verify_logo(self):
        """
        Verifies the logo of the page
        Returns: True
        """
        logger.debug("Verifying logo")
        logo = self.page.locator(locators.LOGO)
        if logo.is_visible():
            logger.debug("Logo visible")
            return True

    def verify_menu_bar(self):
        """
        Verifies the menu bar exists or not
        Returns: True
        """
        logger.debug("Verifying menu bar")
        menu_bar = self.page.locator(locators.MENU_BAR)
        if menu_bar.is_visible():
            logger.debug("Menu bar visible")
            return True

    def verify_menu_items(self, menu_locators):
        """
        Verifies the items on the menu bar
        Args: Page locators of the menubar
            menu_locators:
        Returns: True
        """
        logger.debug("Verifying Menu Items")
        for locator in menu_locators:
            logger.debug("Verifying menu item: {}".format(locator))
            menu_locator = self.page.locator(locator)
            if menu_locator.is_visible():
                logger.debug("Menu item: {} visible".format(locator))
                return True

    def search(self, search_phrase):
        """
        Sends a Search query, and verifies if the results are more than 3 or not
        Args:
            search_phrase: Char(s) to search for in the search bar
        Returns: True if successful
        """
        # Create a new page and set viewport size to mobile
        mobile_size = {"width": 720, "height": 1280}

        # Navigate to search page and search for "Azure"
        self.load_home_page()
        self.page.is_visible(locators.OPEN_SEARCH_BUTTON)
        self.page.click(locators.OPEN_SEARCH_BUTTON)
        self.page.fill(locators.SEARCH_BAR, search_phrase)
        logger.debug("Added {} to the search bar".format(search_phrase))

        # Wait for search results to load and take a screenshot of mobile screen
        self.page.click(locators.START_SEARCH_BUTTON)
        logger.debug("Searching for the phrase {} now".format(search_phrase))
        self.page.wait_for_selector(locators.SEARCH_RESULTS)

        # Check if search results have less than 3 items and fail the test if so
        if len(self.page.query_selector_all(locators.SEARCH_RESULTS)) < 3:
            logger.debug("Search Unsuccessful and has less than 3 results. Saving screenshots now!")
            self.page.screenshot(path="/ui_tests/screenshots/desktop_search_result_FAILED.png")
            self.page.set_viewport_size(mobile_size)
            self.page.screenshot(path="/ui_tests/screenshots/mobile_search_result_FAILED.png")
            return False
        else:
            logger.debug("Search Successful and has more than or equal to 3 results. Saving screenshots now!")
            self.page.screenshot(path="/ui_tests/screenshots/desktop_search_result_PASSED.png")
            self.page.set_viewport_size(mobile_size)
            self.page.screenshot(path="/ui_tests/screenshots/mobile_search_result_PASSED.png")
            return True
