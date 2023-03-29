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

import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Create a user with a random username in lowercase letters"
STEP_2 = "Fetch the details of the respective user with username: {}"
STEP_3 = "Create another user with the same username as in Step - 1"
STEP_4 = "Fetch the details of the user with uppercase username: {}"
STEP_5 = "Verify that both responses are different"


@allure.title("Get User Details - Case sensitive username")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_case_sensitive_username():
    """
    The testcase verifies that if API endpoint: /user/{username} receives a req with two same
    usernames but with the difference of one being lower case and other being uppercase, the
    response JSON is different for both.
    """
    # Step - 1
    with allure.step(STEP_1):
        lower_case_username = api_utils.gen_rand_str(10).lower()
        create_user_lower_case = api_utils.create_user(u_id=api_utils.gen_rand_int(10000000000, 99999999999),
                                                       u_name=lower_case_username)
        assert create_user_lower_case.resp.status_code == 200
        logger.info(STEP_1 + " ----------------------- done!")

    # Step - 2
    with allure.step(STEP_2.format(lower_case_username)):
        user_details_lower_case = api_utils.get_user_details(u_name=lower_case_username)
        assert user_details_lower_case.status_code == 200
        assert user_details_lower_case.json()['username'] == lower_case_username
        logger.info(STEP_2.format(lower_case_username) + " ---------------------- done!")

    # Step - 3
    with allure.step(STEP_3):
        upper_case_username = lower_case_username.upper()
        create_user_upper_case = api_utils.create_user(u_id=api_utils.gen_rand_int(10000000000, 99999999999),
                                                       u_name=upper_case_username)

        assert create_user_upper_case.resp.status_code == 200
        logger.info(STEP_3 + " --------------------- done!")

    # Step - 4
    with allure.step(STEP_4.format(upper_case_username)):
        user_details_upper_case = api_utils.get_user_details(u_name=upper_case_username)
        assert user_details_upper_case.status_code == 200

        assert user_details_upper_case.json()['username'] == upper_case_username
        logger.info(STEP_4.format(upper_case_username) + " --------------------- done!")

    # Step - 5
    with allure.step(STEP_5):
        assert user_details_upper_case.json() != user_details_lower_case.json()
        logger.info(STEP_5 + " --------------------------- verified successfully!")
