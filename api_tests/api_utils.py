#!/usr/bin/env python3
"""
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
__author__: "Saad Tahir"
__date__: "22/3/2023"
__updated__: ""
__version__ = "1.0"
__maintainer__ = "Saad Tahir"
__email__ = "saad.tahir@ut.ee"
__status__ = "Developed"
# ----------------------------------------------------------------------------
# The script adds the following util methods to be used for the tests:
- Request Method(s)
- Helpers (to load files etc.
- Pet Store - User endpoint specific
# ----------------------------------------------------------------------------
"""
import collections
import json
import os
import random
import string

import requests as re
from jsonschema import validate

from base_script import ConfigLoader
from logger import logging_setup

logger = logging_setup()
cl = ConfigLoader()


# ----------------------------------------------- REQUEST Operations ---------------------------------------------#
#                                                                                                                 #
# ----------------------------------------------------------------------------------------------------------------#
def get_req(uri, protocol, host, headers, api_ver):
    """
    Sends a GET request with the specified parameters
    Args:
        uri: the specific URI of the request
        protocol: HTTP/HTTPS protocol to be used (based on config)
        host: host address
        api_ver: the current api ver
        headers: X-road headers

    Returns: a Rest object with all the properties to proceed for tests
    """
    resp_get = request_operation(req_method="GET", uri=uri, protocol=protocol, host=host,
                                 api_ver=api_ver, headers=headers)
    return resp_get


def post_req(uri, protocol, host, headers, data, api_ver):
    """
    Sends a POST request with the specified parameters
    Args:
        uri: the specific URI of the request
        protocol: HTTP/HTTPS protocol to be used (based on config)
        host: host address
        api_ver: the current api ver
        headers: X-road headers
        data: The request body to be sent

    Returns: a Rest object with all the properties to proceed for tests
    """
    resp_post = request_operation(req_method='POST', uri=uri, protocol=protocol, host=host,
                                  api_ver=api_ver, data=data, headers=headers)
    return resp_post


def put_req(uri, protocol, host, headers, data, api_ver):
    """
    Sends a PUT request with the specified parameters
    Args:
        uri: the specific URI of the request
        protocol: HTTP/HTTPS protocol to be used (based on config)
        host: host address
        api_ver: the current api ver
        headers: X-road headers
        data: The request body to be sent

    Returns: a Rest object with all the properties to proceed for tests
    """
    resp_put = request_operation(req_method='PUT', uri=uri, protocol=protocol, host=host,
                                 api_ver=api_ver, data=data, headers=headers)
    return resp_put


def del_req(uri, protocol, host, headers, api_ver):
    """
    Sends a DELETE request with the specified parameters
    Args:
        uri: the specific URI of the request
        protocol: HTTP/HTTPS protocol to be used (based on config)
        host: host address
        api_ver: the current api ver
        headers: X-road headers

    Returns: a Rest object with all the properties to proceed for tests
    """
    resp_put = request_operation(req_method='DELETE', uri=uri, protocol=protocol, host=host,
                                 api_ver=api_ver, headers=headers)
    return resp_put


def request_operation(req_method, uri, protocol, host, headers, data=None, api_ver=None):
    """
    Method to send the api_tests request using the 'requests' library object.
    Args:
        req_method: specifies the method for the api_tests request to be sent i.e. GET or POST etc.
        uri: the specific URI of the request
        protocol: HTTP/HTTPS protocol to be used (based on config)
        host: host address
        api_ver: the current api ver
        data: The request body to be sent
        headers: X-road headers

    Returns: A Rest object with all the properties in the api_tests response to proceed
    """
    url = f"{protocol}://{host}/{api_ver}{uri}"

    try:
        logger.debug(f"URL: {url} created and now sending the {req_method} request to the server {host}")
        # If there are headers but there's no key specifying the content type
        resp = re.request(req_method, url=url, json=data, headers=headers, timeout=120)
        return resp

    except re.exceptions.RequestException as ex:
        logger.error(f"Unknown exception occurred. Please check the logs for the details. The script is exiting!! \n {ex}")


# ----------------------------------------------- Helpers --------------------------------------------------------#
#                                                                                                                 #
# ----------------------------------------------------------------------------------------------------------------#

def load_valid_schema(file_name):
    try:
        file_path = os.path.join(os.path.join(os.path.dirname(__file__), "user_schema"), file_name)
        with open(file_path, mode="r") as schema_file:
            schema = json.loads(schema_file.read())
            return schema

    except Exception as e:
        logger.error("Failed to load JSON schema file!\n{}".format(e))


def assert_schema(resp_data, schema_file_name):
    valid_schema = load_valid_schema(file_name=schema_file_name)
    return validate(resp_data, schema=valid_schema)


def gen_rand_int(min_length, max_length) -> int:
    """
    Generates a random ID to be used for creating a user
    Args:
        min_length: Min length of the ID
        max_length: Max length of the ID
    Returns: An int value
    """
    rand_int = random.randint(min_length, max_length)
    return rand_int


def gen_rand_str(length) -> str:
    """
    Generates a random str to be used for creating a user
    Args:
        length: Max length of str

    Returns: A str value
    """
    rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return rand_str


def invalid_req_methods(req_method, uri):
    """
    Sends the API requests using incorrect methods
    Args:
        req_method:
        uri:

    Returns:

    """
    resp_invalid_methods = request_operation(req_method=req_method, uri=uri, protocol=cl.api_web_protocol, host=cl.api_web_host,
                                             data=None, api_ver=cl.api_ver, headers=cl.headers)
    return resp_invalid_methods


# ----------------------------------------------- User Specific --------------------------------------------------#
#                                                                                                                 #
# ----------------------------------------------------------------------------------------------------------------#


def create_user(u_id=0, u_name="jdoe1", f_name="Jane", l_name="Doe", email="jdoe@gmail.com",
                p_wrd="abcd123", phone="123456789", u_status=0):
    """
    Creates a User using the endpoint: /user
    Args:
        u_id: ID of the User
        u_name: Username
        f_name: First Name
        l_name: Last Name
        email: Email Address
        p_wrd: Password
        phone: Phone Number
        u_status: User Status i.e. 0 or any other number

    Returns: REST Response Object
    """
    created_user = collections.namedtuple('created_user', ['u_data', 'resp'])

    u_data = {
        "id": u_id,
        "username": u_name,
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
        "password": p_wrd,
        "phone": phone,
        "userStatus": u_status
    }

    create_user_resp = post_req(uri=cl.create_single_user, protocol=cl.api_web_protocol, host=cl.api_web_host,
                                headers=cl.headers, data=u_data, api_ver=cl.api_ver)

    created_user = created_user(u_data, create_user_resp)
    if create_user_resp.status_code == 200:
        logger.debug("User created with the following details:\n{}".format(u_data))
    return created_user


def get_user_details(u_name):
    """
    Fetches the Details of a specific user
    Args:
        u_name: Username of the respective User

    Returns: REST Response Object
    """
    user_details_resp = get_req(uri=cl.get_user_details.format(u_name), protocol=cl.api_web_protocol, host=cl.api_web_host,
                                headers=cl.headers, api_ver=cl.api_ver)
    return user_details_resp


def update_user_details(u_id=0, u_name="jdoe1", f_name="Jane", l_name="Doe", email="jdoe@gmail.com",
                        p_wrd="abcd123", phone="123456789", u_status=0):
    """
    Creates a User using the endpoint: /user
    Args:
        u_id: ID of the User
        u_name: Username
        f_name: First Name
        l_name: Last Name
        email: Email Address
        p_wrd: Password
        phone: Phone Number
        u_status: User Status i.e. 0 or any other number

    Returns: REST Response Object
    """
    updated_user = collections.namedtuple('updated_user', ['u_data', 'resp'])

    u_data = {
        "id": u_id,
        "username": u_name,
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
        "password": p_wrd,
        "phone": phone,
        "userStatus": u_status
    }

    update_user_resp = put_req(uri=cl.update_user_details.format(u_name), protocol=cl.api_web_protocol, host=cl.api_web_host,
                               headers=cl.headers, data=u_data, api_ver=cl.api_ver)

    updated_user = updated_user(u_data, update_user_resp)
    if update_user_resp.status_code == 200:
        logger.debug("User updated with the following details:\n{}".format(u_data))
    return updated_user


def delete_user(u_name):
    """
    Deletes a user and its data
    Args:
        u_name: Username of the user

    Returns: None
    """
    delete_user_resp = del_req(uri=cl.delete_user_details.format(u_name), protocol=cl.api_web_protocol, host=cl.api_web_host,
                               headers=cl.headers, api_ver=cl.api_ver)

    return delete_user_resp
