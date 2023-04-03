import allure

from logger import logging_setup

logger = logging_setup()


@allure.title("Search for a phrase that has more than 3 results and take screenshots")
@allure.severity(allure.severity_level.CRITICAL)
def test_basic_search_pass(homepage_functions):
    """
    Verify the Search functionality works in case of phrase added
    Args:
        homepage_functions: Fixture for the homepage POM

    Returns: None
    """
    step_1 = "Verify that the phrase 'Azure' returns more than 3 results and take screenshot(s)"
    with allure.step(step_1):
        assert homepage_functions.search(search_phrase="Azure") is True
        logger.info(step_1 + "verified successfully!")


@allure.title("Search for a phrase that has less than 3 results and take screenshots")
@allure.severity(allure.severity_level.CRITICAL)
def test_basic_search_fail(homepage_functions):
    """
    Fixture for the homepage POM
    Args:
        homepage_functions: Fixture for the homepage POM

    Returns: None
    """
    step_1 = "Verify that the phrase 'Azure' returns more than 3 results and take screenshot(s)"
    with allure.step(step_1):
        assert homepage_functions.search(search_phrase="AZNDSA") is False
        logger.info(step_1 + "verified successfully!")
