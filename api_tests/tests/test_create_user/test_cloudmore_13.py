import api_utils
import random
from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()

STEP_1 = "Send an POST request to the endpoint: /user with ONLY required keys in the req body as:\n{}"
STEP_2 = "Verify that the response payload is as expected i.e. status code is 200 and body is has specific JSON schema"


def test_create_new_user_only_req_keys() -> None:
    """
    The test case verifies that a new user can be created with only the required keys, specified as follows:
    - id
    - userStatus
    Returns: None
    """
    # Step - 1
    user_id = random.randint(0, 99999999999)

    user_data_req_keys = {
        "id": user_id,
        "username": "saad",
    }
    resp_req_keys_only = api_utils.post_req(uri=cl.create_single_user, protocol=cl.web_protocol, host=cl.web_host,
                                            headers=cl.headers, data=user_data_req_keys, api_ver=cl.api_ver)

    resp_req_keys_only_json = resp_req_keys_only.json()
    logger.info(STEP_1.format(user_data_req_keys) + "------------------ done!")

    # Step - 2
    api_utils.assert_schema(resp_data=resp_req_keys_only_json, schema_file_name="create_user.json")
    assert resp_req_keys_only.headers['Content-Type'] == str(cl.headers_type)
    logger.info(STEP_2 + "--------------------- verified successfully!")
