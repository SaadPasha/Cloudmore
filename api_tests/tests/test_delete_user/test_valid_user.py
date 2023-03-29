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

import time

import allure

import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Create a new user with a specific username by sending POST req to endpoint: /user"
STEP_2 = "Verify the user details by sending GET req to endpoint: /user/{}"
STEP_3 = "Delete the respective user by sending a DEL req to endpoint: /user/{}"
STEP_4 = "Verify the user doesn't exist by sending GET req to endpoint: /user/{}"


@allure.title("Delete User - valid username")
@allure.severity(allure.severity_level.BLOCKER)
def test_delete_valid_user(create_user):
    """
    The testcase verifies that incase a valid user is requested to be deleted using the API endpoint: /user/{username},
    the API responds in a 200 HTTP status code.
    Args:
        create_user: Fixture that creates a random user
    """
    # Step - 1
    with allure.step(STEP_1):
        assert create_user.resp.status_code == 200
        username = create_user.u_data['username']
        logger.info(STEP_1 + " ----------------------------- done!")

    # Step - 2
    with allure.step(STEP_2.format(username)):
        user_init_details_resp = api_utils.get_user_details(u_name=username)
        assert user_init_details_resp.status_code == 200
        logger.info(STEP_2.format(username) + " --------------------------- verified successfully!")

    # Step - 3
    with allure.step(STEP_3.format(username)):
        delete_user_resp = api_utils.delete_user(u_name=username)
        assert delete_user_resp.status_code == 200
        logger.info(STEP_3.format(username) + " -------------------------------- done!")

    # Step - 4
    time.sleep(5)
    with allure.step(STEP_4.format(username)):
        user_post_del_details_resp = api_utils.get_user_details(u_name=username)
        assert user_post_del_details_resp.status_code == 404
        assert user_post_del_details_resp.json()['message'] == "User not found"
        logger.info(STEP_4.format(username) + " --------------------------- verified successfully!")
