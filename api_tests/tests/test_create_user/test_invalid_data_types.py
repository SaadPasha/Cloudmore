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

from api_utils import create_user
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Verify that the API req sent to endpoint: /users - with the value of key: {} set as {} returns a 400 status code."


@allure.title("Create a new user - Invalid Data type for ID key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("id_key, expected", [("0", 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_id_data_type(id_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'id' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(id_key, expected)):
        assert create_user(u_id=id_key).resp.status_code == expected
        logger.info(STEP_1.format(id_key, expected))


@allure.title("Create a new user - Invalid Data type for username key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("uname_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_uname_data_type(uname_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'username' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(uname_key, expected)):
        assert create_user(u_name=uname_key).resp.status_code == expected
        logger.info(STEP_1.format(uname_key, expected))


@allure.title("Create a new user - Invalid Data type for firstName key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("f_name_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_f_name_data_type(f_name_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'firstName' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(f_name_key, expected)):
        assert create_user(f_name=f_name_key).resp.status_code == expected
        logger.info(STEP_1.format(f_name_key, expected))


@allure.title("Create a new user - Invalid Data type for lastName key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("l_name_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_l_name_data_type(l_name_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'lastName' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(l_name_key, expected)):
        assert create_user(l_name=l_name_key).resp.status_code == expected
        logger.info(STEP_1.format(l_name_key, expected))


@allure.title("Create a new user - Invalid Data type for email key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("email_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_email_data_type(email_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'email' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(email_key, expected)):
        assert create_user(email=email_key).resp.status_code == expected
        logger.info(STEP_1.format(email_key, expected))


@allure.title("Create a new user - Invalid Data type for password key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("password_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_password_data_type(password_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'password' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(password_key, expected)):
        assert create_user(p_wrd=password_key).resp.status_code == expected
        logger.info(STEP_1.format(password_key, expected))


@allure.title("Create a new user - Invalid Data type for phone key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("phone_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_phone_data_type(phone_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'phone' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(phone_key, expected)):
        assert create_user(phone=phone_key).resp.status_code == expected
        logger.info(STEP_1.format(phone_key, expected))


@allure.title("Create a new user - Invalid Data type for userStatus key values")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("u_status_key, expected", [(0, 200), ([12], 500), ({'12': '12'}, 500)])
def test_create_user_invalid_u_status_data_type(u_status_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'userStatus' key's value,
    then it should respond with a response code of 400.
    """
    with allure.step(STEP_1.format(u_status_key, expected)):
        assert create_user(u_status=u_status_key).resp.status_code == expected
        logger.info(STEP_1.format(u_status_key, expected))
