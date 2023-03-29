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

import concurrent.futures
import time

import allure

import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Create a new user with a specific username by sending POST req to endpoint: /user"
STEP_2 = "Send simultaneous DELETE reqs to the endpoint: /user/{}"
STEP_3 = "Verify that only first request is returned with a 200 status code and all others are returned with 404"


@allure.title("Delete User - Multiple Delete requests for the same username")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_one_user_multiple_req(create_user):
    """
    The testcase verifies that if the DELETE req for the same user is received multiple times,
    only the first received request will be entertained by the user and the rest will be returned
    with a 404 status code.
    Args:
        create_user: Creates a random user
    """
    # Step - 1
    with allure.step(STEP_1):
        assert create_user.resp.status_code == 200
        username = create_user.u_data['username']
        logger.info(STEP_1 + " ---------------------- done!")
        time.sleep(5)

    # Step - 2
    results = []
    with allure.step(STEP_2.format(username)):
        for req in range(3):
            # Creating 3 different threads, and then each thread requesting the server to delete the user
            with concurrent.futures.ThreadPoolExecutor() as executor:
                resp = executor.submit(api_utils.delete_user, username)
                results.append(resp.result().status_code)
                time.sleep(5)
        logger.info(STEP_2 + " --------------------- done!")

    # Step - 3
    with allure.step(STEP_3.format(username)):
        assert results[0] == 200
        assert results[1] == 404
        assert results[2] == 404
