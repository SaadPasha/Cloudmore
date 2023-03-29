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

import random

import allure

import api_utils
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an POST request to the endpoint: /user with ONLY required keys in the req body as:\n{}"
STEP_2 = "Verify that the response payload is as expected i.e. status code is 200 and body is has specific JSON schema"


@allure.title("Create a new User - With only required keys")
@allure.severity(allure.severity_level.NORMAL)
def test_create_new_user_only_req_keys():
    """
    The test case verifies that a new user can be created with only the required keys, specified as follows:
    - id
    - userStatus
    """
    # Step - 1
    user_id = random.randint(0, 99999999999)

    user_data_req_keys = {
        "id": user_id,
        "username": "saad",
    }
    with allure.step(STEP_1.format(user_data_req_keys)):
        resp_req_keys_only = api_utils.post_req(uri=cl.create_single_user, protocol=cl.web_protocol, host=cl.web_host,
                                                headers=cl.headers, data=user_data_req_keys, api_ver=cl.api_ver)

        resp_req_keys_only_json = resp_req_keys_only.json()
        logger.info(STEP_1.format(user_data_req_keys) + "------------------ done!")

    # Step - 2
    with allure.step(STEP_2):
        api_utils.assert_schema(resp_data=resp_req_keys_only_json, schema_file_name="create_user.json")
        logger.info(STEP_2 + "--------------------- verified successfully!")
