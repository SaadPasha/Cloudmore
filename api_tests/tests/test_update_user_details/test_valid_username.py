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

STEP_1 = "Create a user with the random data with POST req using endpoint: /user"
STEP_2 = "Fetch the details of the respective user"
STEP_3 = "Update the details of the same user with PUT req using endpoint: /user/{}"
STEP_4 = "Fetch the updated details of the user"
STEP_5 = "Verify that the details from Step-2 and Step-4 do not match"


@allure.title("Update User Details - Valid username")
@allure.severity(allure.severity_level.BLOCKER)
def test_update_user_details(create_user):
    """
    The testcase verifies that in case a valid req is sent to API endpoint: /user/{username} to update user data,
    the request should be successful and the data should be updated.
    Args:
        create_user: Fixture to create a user
    """
    # Step - 1
    with allure.step(STEP_1):
        assert create_user.resp.status_code == 200
        username = create_user.u_data['username']
        logger.info(STEP_1 + " ------------------------- done!")

    # Step - 2
    with allure.step(STEP_2):
        user_init_details_resp = api_utils.get_user_details(u_name=username)
        assert user_init_details_resp.status_code == 200
        user_init_details = user_init_details_resp.json()
        logger.info(STEP_2 + " --------------------------- done!")

    # Step - 3
    with allure.step(STEP_3.format(username)):
        update_user_details = api_utils.update_user_details(u_id=22, u_name=username, f_name="John", l_name="Smith",
                                                            email="jsmith@gmail.com", p_wrd="abcdefg", phone="22222222", u_status=1)

        assert update_user_details.resp.status_code == 200
        logger.info(STEP_3.format(username) + " -------------------------- done!")

    # Step - 4
    with allure.step(STEP_4):
        time.sleep(10)
        user_updated_details_resp = api_utils.get_user_details(u_name=username)
        assert user_updated_details_resp.status_code == 200
        user_updated_details = user_updated_details_resp.json()
        logger.info(STEP_4 + " -------------------------- done!")

    # Step - 5
    with allure.step(STEP_5):
        assert user_init_details['username'] == user_updated_details['username']
        assert user_init_details != user_updated_details
        logger.info(STEP_5 + " -------------------------- verified successfully!")
