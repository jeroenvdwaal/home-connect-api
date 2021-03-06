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
from api.status_events_api import StatusEventsApi  # noqa: E501
from home_connect_api.rest import ApiException


class TestStatusEventsApi(unittest.TestCase):
    """StatusEventsApi unit test stubs"""

    def setUp(self):
        self.api = api.status_events_api.StatusEventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_events(self):
        """Test case for get_all_events

        Get stream of events for all appliances - NOT WORKING WITH SWAGGER  # noqa: E501
        """
        pass

    def test_get_events(self):
        """Test case for get_events

        Get stream of events for one appliance - NOT WORKING WITH SWAGGER  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        Get current status of home appliance  # noqa: E501
        """
        pass

    def test_get_status_value(self):
        """Test case for get_status_value

        Get current status of home appliance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
