# coding: utf-8

"""
    User exchange API

    User exchange API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mipt@mipt.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExchangePayload(object):
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
        'start_index': 'int',
        'out_dec_number': 'int'
    }

    attribute_map = {
        'start_index': 'startIndex',
        'out_dec_number': 'outDecNumber'
    }

    def __init__(self, start_index=None, out_dec_number=None):  # noqa: E501
        """ExchangePayload - a model defined in Swagger"""  # noqa: E501
        self._start_index = None
        self._out_dec_number = None
        self.discriminator = None
        if start_index is not None:
            self.start_index = start_index
        if out_dec_number is not None:
            self.out_dec_number = out_dec_number

    @property
    def start_index(self):
        """Gets the start_index of this ExchangePayload.  # noqa: E501


        :return: The start_index of this ExchangePayload.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this ExchangePayload.


        :param start_index: The start_index of this ExchangePayload.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def out_dec_number(self):
        """Gets the out_dec_number of this ExchangePayload.  # noqa: E501


        :return: The out_dec_number of this ExchangePayload.  # noqa: E501
        :rtype: int
        """
        return self._out_dec_number

    @out_dec_number.setter
    def out_dec_number(self, out_dec_number):
        """Sets the out_dec_number of this ExchangePayload.


        :param out_dec_number: The out_dec_number of this ExchangePayload.  # noqa: E501
        :type: int
        """

        self._out_dec_number = out_dec_number

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
        if issubclass(ExchangePayload, dict):
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
        if not isinstance(other, ExchangePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other