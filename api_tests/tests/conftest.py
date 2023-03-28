import pytest


def pytest_html_report_title(report):
    report.title = "API tests"


pytest_plugins = [
    "tests.fixtures"
]
# def pytest_configure(config):
#     ''' modifying the table pytest environment'''
#
#     from pwd import getpwuid
#     from os import getuid
#
#     username = getpwuid(getuid())[0]
#
#     # getting python version
#     from platform import python_version
#     py_version = python_version()
#     # overwriting old parameters with  new parameters
#     config._metadata = {
#         "user_name": username,
#         "python_version": py_version,
#     }
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix, summary, postfix):
#     ''' modifying the summary in pytest environment'''
#
#     from py.xml import html
#     prefix.extend([html.h3("Adding prefix message")])
#     summary.extend([html.h3("Adding summary message")])
#     postfix.extend([html.h3("Adding postfix message")])
