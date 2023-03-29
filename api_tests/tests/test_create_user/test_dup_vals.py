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
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_2 = "Verify that req is successful with 200 HTTP resp code ------------------------- verified successfully!"


@allure.title("Create a new User - Duplicate fields - Duplicate User ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(strict=False, reason="The API should respond with status code of 400")
def test_create_user_duplicate_id():
    """
    The testcase verifies that API should not allow the same user ID in multiple requests
    and should generate a 400 Bad Request error.
    Returns: None
    """
    STEP_1 = "Send a POST req to the endpoint: /users - with the id specified as: {}"
    STEP_3 = "Repeat step - 1 with same id"
    STEP_4 = "Verify that the status code is 400 Bad request because of ID duplication."

    # Step - 1
    rand_id = api_utils.gen_rand_int(10000000000, 99999999999)
    with allure.step(STEP_1.format(rand_id)):
        rand_id_resp = api_utils.create_user(u_id=rand_id)
        logger.info(STEP_1.format(rand_id) + " ------------done!")

    # Step - 2
    with allure.step(STEP_2):
        assert rand_id_resp.resp.status_code == 200
        logger.info(STEP_2)

    # Step - 3
    with allure.step(STEP_3):
        dup_id_resp = api_utils.create_user(u_id=rand_id)
        logger.info(STEP_3 + " --------------------- done")

    # Step - 4
    # This step will purposefully get failed
    with allure.step(STEP_4):
        assert dup_id_resp.resp.status_code == 400
        logger.info(STEP_4 + " ------------------------ verified successfully!")


@allure.title("Create a new User - Duplicate fields - Duplicate Username")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(strict=False, reason="The API should respond with status code of 400")
def test_create_user_dup_uname():
    """
    The testcase verifies that API should not allow the same username in multiple requests
    and should generate a 400 Bad Request error.
    """
    STEP_1 = "Send a POST req to the endpoint: /users - with the username specified as: {}"
    STEP_3 = "Repeat step - 1 with same username"
    STEP_4 = "Verify that the status code is 400 Bad request because of USERNAME duplication."

    # Step - 1
    rand_uname = api_utils.gen_rand_str(10)
    with allure.step(STEP_1.format(rand_uname)):
        rand_uname_resp = api_utils.create_user(u_name=rand_uname)
        logger.info(STEP_1.format(rand_uname) + " ---------------------------- done!")

    # Step - 2
    with allure.step(STEP_2):
        assert rand_uname_resp.resp.status_code == 200
        logger.info(STEP_2)

    # Step - 3
    with allure.step(STEP_3):
        dup_uname_resp = api_utils.create_user(u_name=rand_uname)
        logger.info(STEP_3 + " ------------------------- done!")

    # Step - 4
    # This step will purposefully get failed
    with allure.step(STEP_4):
        assert dup_uname_resp.resp.status_code == 400
        logger.info(STEP_4 + " ------------------------- done!")


@allure.title("Create a new User - Duplicate fields - Duplicate User EMAIL")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(strict=False, reason="The API should respond with status code of 400")
def test_create_user_dup_email():
    """
    The testcase verifies that API should not allow the same email in multiple requests
    and should generate a 400 Bad Request error.
    """
    STEP_1 = "Send a POST req to the endpoint: /users - with the email specified as: {}"
    STEP_3 = "Repeat step - 1 with same username"
    STEP_4 = "Verify that the status code is 400 Bad request because of EMAIL duplication."

    # Step - 1
    rand_email = api_utils.gen_rand_str(6) + "@gmail.com"
    with allure.step(STEP_1.format(rand_email)):
        rand_email_resp = api_utils.create_user(email=rand_email)
        logger.info(STEP_1.format(rand_email_resp) + " ------------------------ done!")

    # Step -2
    with allure.step(STEP_2):
        assert rand_email_resp.resp.status_code == 200
        logger.info(STEP_2)

    # Step - 3
    with allure.step(STEP_3):
        dup_email_resp = api_utils.create_user(email=rand_email)
        logger.info(STEP_3 + " ------------------------- verified successfully!")

    # Step - 4
    # This step will purposefully get failed
    with allure.step(STEP_4):
        assert dup_email_resp.resp.status_code == 400
        logger.info(STEP_4 + " ------------------------- verified successfully!")
