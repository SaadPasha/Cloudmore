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

import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Verify that the invalid API req with username: {} sent to the endpoint: /user/{} results in status code of 404"


@allure.title("Update User Details - Invalid and Null username")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(strict=False, reason="The API should respond with status code of 404")
@pytest.mark.parametrize("username, expected", [(api_utils.gen_rand_str(5), 404),
                                                (api_utils.gen_rand_int(10000, 99999), 404),
                                                (" ", 404)])
def test_update_user_details_invalid_and_null_username(username, expected):
    """
    The testcase verifies that if the API endpoint: /users/{username} is requested with invalid username,
    the API should respond with a status code of 404 - Not found
    """
    with allure.step(STEP_1.format(username, username)):
        assert api_utils.update_user_details(u_name=username).resp.status_code == expected
        logger.info(STEP_1.format(username, username) + " ----------------------- verified successfully!")
