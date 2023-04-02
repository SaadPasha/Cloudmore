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
import time

import pytest

import api_utils
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Create a new user with a specific username by sending POST req to endpoint: /user"
STEP_2 = "Verify the user details by sending GET req to endpoint: /user/{}"
STEP_3 = "Update only the user name by sending a PUT req the endpoint: /user/{} with the new username as: {}"
STEP_4 = "Repeat step - 2 and verify that the respective endpoint doesn't exist i.e. username updated"


@allure.title("Update User Details - update already updated username")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(strict=False, reason="Previously existing username should not be found - 404 expected")
def test_update_existing_username(create_user):
    """
    Testcase to verify that if a username is updated by sending a PUT req to endpoint: /user/{username},
    and if the same req (with same username) is sent again, then the API response should be 404 - Notfound.
    Args:
        create_user: Creates a random user

    Returns: None
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
    with allure.step(STEP_3.format(username, username)):
        new_username = api_utils.gen_rand_str(5)
        update_details = api_utils.put_req(uri="/user/{}".format(username), protocol=cl.api_web_protocol, host=cl.api_web_host,
                                           api_ver=cl.api_ver, headers=cl.headers, data={"username": new_username})

        assert update_details.status_code == 200
        time.sleep(5)
        logger.info(STEP_3.format(username, new_username) + " -------------------------- done!")

    # Step - 4
    with allure.step(STEP_4):
        user_updated_details_resp = api_utils.get_user_details(u_name=username)
        assert user_updated_details_resp.status_code == 404
