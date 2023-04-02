#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
__author__: "Saad Tahir"
__date__: "24/3/2023"
__updated__: "29/03/2023"
__version__ = "1.0"
__maintainer__ = "Saad Tahir"
__email__ = "saad.tahir@ut.ee"
__status__ = "Developed"
# ----------------------------------------------------------------------------
"""

import allure
import pytest
from api_utils import post_req
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an API request to the endpoint: {}"
STEP_2 = "Verify that the response is 404."


@allure.title("Create a new user - Incorrect API endpoint")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("endpoint, expected", [("/users", 404), ("/use", 404), ("createUser", 404)])
def test_create_user_incorrect_endpoint(endpoint, expected):
    """
    The testcase verifies that if the client sends request to an incorrect API endpoint,
    then the Server should return an error code of 404 - Not Found
    Returns: None
    """
    # Step - 1
    with allure.step(STEP_1.format(endpoint) + " ----------------- done!"):
        incorrect_endpoint_resp = post_req(uri=endpoint, protocol=cl.api_web_protocol, host=cl.api_web_host,
                                           headers=cl.headers, data={}, api_ver=cl.api_ver)

        assert incorrect_endpoint_resp.status_code == expected
        logger.info(STEP_1.format(endpoint) + " ------------------ done!")
