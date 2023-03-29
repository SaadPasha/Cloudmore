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
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Verify that an API request to endpoint: {} with method: {} results in response code of 405"


@allure.title("Get User Details - Incorrect API methods")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("req_method, uri, expected", [("POST", "/user/123", 405), ("LINK", "/user/123", 405),
                                                       ("PATCH", "/user/123", 405)])
def test_incorrect_methods(req_method, uri, expected) -> None:
    """
    The testcase verifies that if the API endpoint receives a request with Non-Supported method call,
    then it should respond with a response code of 405.
    Returns: None
    """
    # Step - 1
    with allure.step(STEP_1.format(uri, req_method)):
        assert invalid_req_methods(req_method, uri).status_code == expected
        logger.info(STEP_1.format(uri, req_method) + " ---------------------- done!")
