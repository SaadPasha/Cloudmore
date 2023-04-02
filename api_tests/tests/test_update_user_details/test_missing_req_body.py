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

STEP_1 = "Create a new user"
STEP_2 = "Send an API req to update the user details with an empty json in the req body."
STEP_3 = "Verify the status code to be 400"


@allure.title("Update User Details - Missing req body")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(strict=False, reason="Expects 400 but given 405")
def test_update_user_details_missing_req_body(create_user):
    """
    The testcase verifies that if a req is sent to endpoint: /user/{username} with empty req body params,
    the API should return a 400 - Bad Req status code.
    Returns: None

    """
    # Step - 1
    with allure.step(STEP_1):
        assert create_user.resp.status_code == 200
        username = create_user.u_data['username']
        logger.info(STEP_1 + " ----------------- done!")

    # Step - 2
    with allure.step(STEP_2):
        update_user_no_json = api_utils.put_req(uri="/user/{}".format(username), protocol=cl.api_web_protocol, host=cl.api_web_host,
                                                api_ver=cl.api_ver, headers=cl.headers, data=None)
        logger.info(STEP_2 + " ----------------------- done!")

    # Step - 3
    with allure.step(STEP_3):
        assert update_user_no_json.json()['message'] == "no data"
        assert update_user_no_json.status_code == 400
        logger.info(STEP_3 + " ----------------- verified successfully!")
