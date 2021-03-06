# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import home_connect_api
from api.programs_api import ProgramsApi  # noqa: E501
from home_connect_api.rest import ApiException


class TestProgramsApi(unittest.TestCase):
    """ProgramsApi unit test stubs"""

    def setUp(self):
        self.api = api.programs_api.ProgramsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_active_program(self):
        """Test case for get_active_program

        Get program which is currently executed  # noqa: E501
        """
        pass

    def test_get_active_program_option(self):
        """Test case for get_active_program_option

        Get one specific option of the active program, e.g. the duration.  # noqa: E501
        """
        pass

    def test_get_active_program_options(self):
        """Test case for get_active_program_options

        Get all options of the active program like temperature or duration.  # noqa: E501
        """
        pass

    def test_get_all_programs(self):
        """Test case for get_all_programs

        Get all programs of a given home appliance  # noqa: E501
        """
        pass

    def test_get_available_program(self):
        """Test case for get_available_program

        Get specific available program  # noqa: E501
        """
        pass

    def test_get_available_programs(self):
        """Test case for get_available_programs

        Get all programs which are currently available on the given home appliance  # noqa: E501
        """
        pass

    def test_get_selected_program(self):
        """Test case for get_selected_program

        Get the program which is currently selected   # noqa: E501
        """
        pass

    def test_get_selected_program_option(self):
        """Test case for get_selected_program_option

        Get specific option of selected program  # noqa: E501
        """
        pass

    def test_get_selected_program_options(self):
        """Test case for get_selected_program_options

        Get all options of selected program  # noqa: E501
        """
        pass

    def test_set_active_program_option(self):
        """Test case for set_active_program_option

        Set one specific option of the active program  # noqa: E501
        """
        pass

    def test_set_active_program_options(self):
        """Test case for set_active_program_options

        Set all options of the active program, e.g. to switch from preheating to the actual program options.  # noqa: E501
        """
        pass

    def test_set_selected_program(self):
        """Test case for set_selected_program

        Select a program  # noqa: E501
        """
        pass

    def test_set_selected_program_option(self):
        """Test case for set_selected_program_option

        Set specific option of selected program  # noqa: E501
        """
        pass

    def test_set_selected_program_options(self):
        """Test case for set_selected_program_options

        Set all options of selected program  # noqa: E501
        """
        pass

    def test_start_program(self):
        """Test case for start_program

        Start the given program  # noqa: E501
        """
        pass

    def test_stop_program(self):
        """Test case for stop_program

        Stop the program which is currently executed  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
