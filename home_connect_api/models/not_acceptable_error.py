# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class NotAcceptableError(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'object'
    }

    attribute_map = {
        'error': 'error'
    }

    def __init__(self, error=None):  # noqa: E501
        """NotAcceptableError - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self.discriminator = None
        self.error = error

    @property
    def error(self):
        """Gets the error of this NotAcceptableError.  # noqa: E501


        :return: The error of this NotAcceptableError.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NotAcceptableError.


        :param error: The error of this NotAcceptableError.  # noqa: E501
        :type: object
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotAcceptableError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotAcceptableError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
