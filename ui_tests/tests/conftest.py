import pytest

from pom.home_page import HomePage
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def homepage_functions(page: Page):
    return HomePage(page)
