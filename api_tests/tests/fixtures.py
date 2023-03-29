import time

import allure
import pytest

import api_utils


@allure.step("Fixture to create a new user with randomly generated data")
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


@allure.step("Fixture to add a few seconds sleep time before execution of new test")
@pytest.fixture(scope="function", autouse=True)
def sleep_timer_test_exec():
    """
    Adds sleep time between each test case
    Returns: None
    """
    time.sleep(3)
