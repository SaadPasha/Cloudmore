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

from api_utils import invalid_req_methods
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Verify that an API request to endpoint: {} with method: {} results in response code of 405"


@allure.title("Create a new user - Incorrect API method & unsupported headers")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("req_method, uri, expected", [("GET", "/user", 405), ("PUT", "/user", 405),
                                                       ("PATCH", "/user", 405), ("DELETE", "/user", 405)])
def test_incorrect_methods_and_invalid_headers(req_method, uri, expected) -> None:
    """
    The testcase verifies that if the API endpoint receives a request with Non-Supported method call,
    then it should respond with a response code of 405.
    Returns: None
    """
    # Step - 1
    with allure.step(STEP_1.format(uri, req_method)):
        assert invalid_req_methods(req_method, uri).status_code == expected
        logger.info(STEP_1.format(uri, req_method) + " ---------------------- done!")
