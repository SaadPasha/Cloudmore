import pytest

from api_utils import create_user
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Verify that the API req sent to endpoint: /users - with the value of key: {} set as {} returns a 400 status code."


@pytest.mark.parametrize("id_key, expected", [("0", 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_id_data_type(id_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'id' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(u_id=id_key).status_code == expected
    logger.info(STEP_1.format(id_key, expected))


@pytest.mark.parametrize("uname_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_uname_data_type(uname_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'username' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(u_name=uname_key).status_code == expected
    logger.info(STEP_1.format(uname_key, expected))


@pytest.mark.parametrize("f_name_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_f_name_data_type(f_name_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'firstName' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(f_name=f_name_key).status_code == expected
    logger.info(STEP_1.format(f_name_key, expected))


@pytest.mark.parametrize("l_name_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_l_name_data_type(l_name_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'lastName' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(l_name=l_name_key).status_code == expected
    logger.info(STEP_1.format(l_name_key, expected))


@pytest.mark.parametrize("email_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_email_data_type(email_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'email' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(email=email_key).status_code == expected
    logger.info(STEP_1.format(email_key, expected))


@pytest.mark.parametrize("password_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_password_data_type(password_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'password' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(p_wrd=password_key).status_code == expected
    logger.info(STEP_1.format(password_key, expected))


@pytest.mark.parametrize("phone_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_phone_data_type(phone_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'phone' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(phone=phone_key).status_code == expected
    logger.info(STEP_1.format(phone_key, expected))


@pytest.mark.parametrize("u_status_key, expected", [(0, 200), ([12], 400), ({'12': '12'}, 400)])
def test_create_user_invalid_u_status_data_type(u_status_key, expected):
    """
    The testcase verifies that if the API endpoint receives a request with invalid 'userStatus' key's value,
    then it should respond with a response code of 400.
    Returns: None
    """
    assert create_user(u_status=u_status_key).status_code == expected
    logger.info(STEP_1.format(u_status_key, expected))
