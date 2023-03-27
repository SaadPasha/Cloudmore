import api_utils
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_2 = "Verify that req is successful with 200 HTTP resp code ------------------------- verified successfully!"


def test_create_user_duplicate_id() -> None:
    """
    The testcase verifies that API should not allow the same user ID in multiple requests
    and should generate a 400 Bad Request error.
    Returns: None
    """
    # Step - 1
    STEP_1 = "Send a POST req to the endpoint: /users - with the id specified as: {}"
    STEP_3 = "Repeat step - 1 with same id"
    STEP_4 = "Verify that the status code is 400 Bad request because of ID duplication."

    rand_id = api_utils.gen_rand_int(10000000000, 99999999999)

    rand_id_resp = api_utils.create_user(u_id=rand_id)
    logger.info(STEP_1.format(rand_id) + " ------------done!")

    # Step - 2
    assert rand_id_resp.status_code == 200
    logger.info(STEP_2)

    # Step - 3
    dup_id_resp = api_utils.create_user(u_id=rand_id)
    logger.info(STEP_3 + " --------------------- done")

    # Step - 4
    assert dup_id_resp.status_code == 400
    logger.info(STEP_4 + " ------------------------ verified successfully!")


def test_create_user_dup_uname() -> None:
    """
    The testcase verifies that API should not allow the same username in multiple requests
    and should generate a 400 Bad Request error.
    Returns: None
    """
    STEP_1 = "Send a POST req to the endpoint: /users - with the username specified as: {}"
    STEP_3 = "Repeat step - 1 with same username"
    STEP_4 = "Verify that the status code is 400 Bad request because of USERNAME duplication."

    # Step - 1
    rand_uname = api_utils.gen_rand_str(10)
    rand_uname_resp = api_utils.create_user(u_name=rand_uname)
    logger.info(STEP_1.format(rand_uname) + " ---------------------------- done!")

    # Step - 2
    assert rand_uname_resp.status_code == 200
    logger.info(STEP_2)

    # Step - 3
    dup_uname_resp = api_utils.create_user(u_name=rand_uname)
    logger.info(STEP_3 + " ------------------------- done!")

    # Step - 3
    assert dup_uname_resp.status_code == 400
    logger.info(STEP_4 + " ------------------------- done!")


def test_create_user_dup_email() -> None:
    """
    The testcase verifies that API should not allow the same email in multiple requests
    and should generate a 400 Bad Request error.
    Returns: None
    """
    STEP_1 = "Send a POST req to the endpoint: /users - with the email specified as: {}"
    STEP_3 = "Repeat step - 1 with same username"
    STEP_4 = "Verify that the status code is 400 Bad request because of EMAIL duplication."

    # Step - 1
    rand_email = api_utils.gen_rand_str(6) + "@gmail.com"
    rand_email_resp = api_utils.create_user(email=rand_email)
    logger.info(STEP_1.format(rand_email_resp) + " ------------------------ done!")

    # Step -2
    assert rand_email_resp.status_code == 200
    logger.info(STEP_2)

    # Step - 3
    dup_email_resp = api_utils.create_user(email=rand_email)
    logger.info(STEP_3 + " ------------------------- verified successfully!")

    # Step - 4
    assert dup_email_resp.status_code == 400
    logger.info(STEP_4 + " ------------------------- verified successfully!")
