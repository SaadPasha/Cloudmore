import pytest

from api_utils import invalid_req_methods
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Verify that an API request to endpoint: {} with method: {} results in response code of 405"


@pytest.mark.parametrize("req_method, uri, expected", [("POST", "/user/123", 405), ("LINK", "/user/123", 405),
                                                       ("PATCH", "/user/123", 405)])
def test_incorrect_methods_and_invalid_headers(req_method, uri, expected) -> None:
    """
    The testcase verifies that if the API endpoint receives a request with Non-Supported method call,
    then it should respond with a response code of 405.
    Returns: None
    """
    # Step - 1
    assert invalid_req_methods(req_method, uri).status_code == expected
    logger.info(STEP_1.format(uri, req_method) + " ---------------------- done!")
