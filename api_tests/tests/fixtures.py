import pytest

import api_utils


@pytest.fixture(scope="function")
def create_user():
    create_user = api_utils.create_user(u_id=api_utils.gen_rand_int(10000000000, 99999999999),
                                        u_name=api_utils.gen_rand_str(10),
                                        f_name=api_utils.gen_rand_str(10),
                                        l_name=api_utils.gen_rand_str(10),
                                        email=api_utils.gen_rand_str(6) + "@gmail.com",
                                        p_wrd=api_utils.gen_rand_str(8),
                                        phone=api_utils.gen_rand_str(11),
                                        u_status=0)
    return create_user

# @pytest.fixture(scope="module")
# def gen_rand_id() -> int:
#     """
#     Generates a random ID to be used for creating a user
#     Returns: ID
#     """
#     return random.randint(0, 99999999999)
#
#
# @pytest.fixture(scope="module")
# def gen_rand_str() ->
