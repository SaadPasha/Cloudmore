import api_utils
import random
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an POST request specified to the endpoint: /user with the req body:\n{} "
STEP_2 = "Verify that the response payload is as expected i.e. status code is 200 and body is has specific JSON schema"


def test_create_a_new_user() -> None:
    """
    The test case verifies that a new user can be created using the required
    and optional key values in body for the following endpoint: /user
    Returns: None
    """
    # Step - 1
    user_id = random.randint(0, 99999999999)

    user_data = {
        "id": user_id,
        "username": "saad",
        "firstName": "Saad",
        "lastName": "Tahir",
        "email": "saadtahir96@test.com",
        "password": "abcdefg",
        "phone": "123456789",
        "userStatus": 0
    }
    resp = api_utils.post_req(uri=cl.create_single_user, protocol=cl.web_protocol, host=cl.web_host,
                              headers=cl.headers, data=user_data, api_ver=cl.api_ver)

    assert resp.status_code == 200
    resp_json = resp.json()
    logger.info(STEP_1.format(user_data) + "----------------------- done!")

    # Step - 2
    api_utils.assert_schema(resp_data=resp_json, schema_file_name="create_user.json")
    assert resp.headers['Content-Type'] == str(cl.headers_type)
    logger.info(STEP_2 + "--------------------- verified successfully!")
