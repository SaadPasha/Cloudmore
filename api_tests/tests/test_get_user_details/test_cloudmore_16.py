import api_utils
from logger import logging_setup

logger = logging_setup()

STEP_1 = "Create a user by sending an API req to the endpoint: /user"
STEP_2 = "Verify that the req was successful"
STEP_3 = "Send an API req to the endpoint: /user/{} - with user name of the user created in STEP_1"
STEP_4 = "Validate the JSON schema of the resp"
STEP_5 = "Verify the data that is received in the response JSON is the one that was used to create user"


def test_get_user_details() -> None:
    """
    The testcase verifies that if the API endpoint: /user/{username} receives a valid request,
    it should respond with a status code of 200 and the details of the respective user.
    Returns: None

    """

    # Step - 1
    create_user = api_utils.create_user(u_id=api_utils.gen_rand_int(10000000000, 99999999999),
                                        u_name=api_utils.gen_rand_str(10),
                                        f_name=api_utils.gen_rand_str(10),
                                        l_name=api_utils.gen_rand_str(10),
                                        email=api_utils.gen_rand_str(6)+"@gmail.com",
                                        p_wrd=api_utils.gen_rand_str(8),
                                        phone=api_utils.gen_rand_str(11),
                                        u_status=0)

    logger.info(STEP_1 + " --------------------- done!")

    # Step - 2
    assert create_user.resp.status_code == 200
    logger.info(STEP_2 + " ---------------------------- verified successfully!")

    # Step - 3
    username = create_user.u_data['username']
    user_details = api_utils.get_user_details(u_name=username)
    assert user_details.status_code == 200

    # Step - 4
    actual_schema = user_details.json()
    api_utils.assert_schema(resp_data=actual_schema, schema_file_name="user_details.json")
    logger.info(STEP_4 + " ------------------------------ verified successfully!")

    # Step - 5
    assert create_user.u_data == actual_schema
