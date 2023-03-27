import pytest
from api_utils import post_req
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an API request to the endpoint: {}"
STEP_2 = "Verify that the response is 404."


@pytest.mark.parametrize("endpoint, expected", [("/users", 404), ("/use", 404), ("createUser", 404)])
def test_create_user_incorrect_endpoint(endpoint, expected):
    """
    The testcase verifies that if the client sends request to an incorrect API endpoint,
    then the Server should return an error code of 404 - Not Found
    Returns: None
    """
    # Step - 1
    logger.info(STEP_1.format(endpoint) + " ------------------ done!")
    incorrect_endpoint_resp = post_req(uri=endpoint, protocol=cl.web_protocol, host=cl.web_host,
                                       headers=cl.headers, data={}, api_ver=cl.api_ver)

    assert incorrect_endpoint_resp.status_code == expected
