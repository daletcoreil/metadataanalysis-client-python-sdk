# coding: utf-8

"""
    Dalet Metadata Analysis API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cortexsupport@dalet.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from metadataanalysis_client.configuration import Configuration


class SegmentTextRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'input_file': 'Locator',
        'output_location': 'SegmentTextResponse',
        'lines': 'Int',
        'characters': 'Int'
    }

    attribute_map = {
        'input_file': 'inputFile',
        'output_location': 'outputLocation',
        'lines': 'lines',
        'characters': 'characters'
    }

    def __init__(self, input_file=None, output_location=None, lines=None, characters=None, local_vars_configuration=None):  # noqa: E501
        """SegmentTextRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._input_file = None
        self._output_location = None
        self._lines = None
        self._characters = None
        self.discriminator = None

        self.input_file = input_file
        self.output_location = output_location
        if lines is not None:
            self.lines = lines
        if characters is not None:
            self.characters = characters

    @property
    def input_file(self):
        """Gets the input_file of this SegmentTextRequest.  # noqa: E501


        :return: The input_file of this SegmentTextRequest.  # noqa: E501
        :rtype: Locator
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        """Sets the input_file of this SegmentTextRequest.


        :param input_file: The input_file of this SegmentTextRequest.  # noqa: E501
        :type: Locator
        """
        if self.local_vars_configuration.client_side_validation and input_file is None:  # noqa: E501
            raise ValueError("Invalid value for `input_file`, must not be `None`")  # noqa: E501

        self._input_file = input_file

    @property
    def output_location(self):
        """Gets the output_location of this SegmentTextRequest.  # noqa: E501


        :return: The output_location of this SegmentTextRequest.  # noqa: E501
        :rtype: SegmentTextResponse
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """Sets the output_location of this SegmentTextRequest.


        :param output_location: The output_location of this SegmentTextRequest.  # noqa: E501
        :type: SegmentTextResponse
        """
        if self.local_vars_configuration.client_side_validation and output_location is None:  # noqa: E501
            raise ValueError("Invalid value for `output_location`, must not be `None`")  # noqa: E501

        self._output_location = output_location

    @property
    def lines(self):
        """Gets the lines of this SegmentTextRequest.  # noqa: E501


        :return: The lines of this SegmentTextRequest.  # noqa: E501
        :rtype: Int
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this SegmentTextRequest.


        :param lines: The lines of this SegmentTextRequest.  # noqa: E501
        :type: Int
        """

        self._lines = lines

    @property
    def characters(self):
        """Gets the characters of this SegmentTextRequest.  # noqa: E501


        :return: The characters of this SegmentTextRequest.  # noqa: E501
        :rtype: Int
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        """Sets the characters of this SegmentTextRequest.


        :param characters: The characters of this SegmentTextRequest.  # noqa: E501
        :type: Int
        """

        self._characters = characters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SegmentTextRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SegmentTextRequest):
            return True

        return self.to_dict() != other.to_dict()
