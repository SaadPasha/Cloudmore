import pytest
import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Verify that the invalid API req with username: {} sent to the endpoint: /user/{} results in status code of 404"


@pytest.mark.parametrize("username, expected", [(api_utils.gen_rand_str(5), 404),
                                                (api_utils.gen_rand_int(10000, 99999), 404),
                                                (" ", 404)])
def test_get_user_invalid_and_null_username(username, expected):
    """
    The testcase verifies that if the API endpoint: /users/{username} is requested with invalid username,
    the API should respond with a status code of 404 - Not found
    Returns: None
    """
    assert api_utils.get_user_details(u_name=username).status_code == expected
    logger.info(STEP_1.format(username, username) + " ----------------------- verified successfully!")
