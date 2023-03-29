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
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an POST request with user details specified to the endpoint: /user "
STEP_2 = "Verify that the response payload is as expected i.e. status code is 200 and body has a valid specific JSON schema"


@allure.title("Create a new User -  With all the required and optional key values")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_a_new_user(create_user):
    """
    The test case verifies that a new user can be created using the required
    and optional key values in body for the following endpoint: /user
    """
    # Step - 1
    with allure.step(STEP_1):
        assert create_user.resp.status_code == 200
        create_user_resp_json = create_user.resp.json()
        logger.info(STEP_1 + "----------------------- done!")

    # Step - 2
    with allure.step(STEP_2):
        api_utils.assert_schema(resp_data=create_user_resp_json, schema_file_name="create_user.json")
        logger.info(STEP_2 + "--------------------- verified successfully!")
