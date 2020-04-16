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
from models.array_of_home_appliances import ArrayOfHomeAppliances  # noqa: E501
from home_connect_api.rest import ApiException


class TestArrayOfHomeAppliances(unittest.TestCase):
    """ArrayOfHomeAppliances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testArrayOfHomeAppliances(self):
        """Test ArrayOfHomeAppliances"""
        # FIXME: construct object with mandatory attributes with example values
        # model = home_connect_api.models.array_of_home_appliances.ArrayOfHomeAppliances()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
