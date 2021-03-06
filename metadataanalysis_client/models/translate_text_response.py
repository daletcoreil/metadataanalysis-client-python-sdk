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


class TranslateTextResponse(object):
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
        'detected_source_language': 'str',
        'text': 'str'
    }

    attribute_map = {
        'detected_source_language': 'detectedSourceLanguage',
        'text': 'text'
    }

    def __init__(self, detected_source_language=None, text=None, local_vars_configuration=None):  # noqa: E501
        """TranslateTextResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._detected_source_language = None
        self._text = None
        self.discriminator = None

        if detected_source_language is not None:
            self.detected_source_language = detected_source_language
        self.text = text

    @property
    def detected_source_language(self):
        """Gets the detected_source_language of this TranslateTextResponse.  # noqa: E501

        The source language that was detected by the API in case it was not specified in the request.  # noqa: E501

        :return: The detected_source_language of this TranslateTextResponse.  # noqa: E501
        :rtype: str
        """
        return self._detected_source_language

    @detected_source_language.setter
    def detected_source_language(self, detected_source_language):
        """Sets the detected_source_language of this TranslateTextResponse.

        The source language that was detected by the API in case it was not specified in the request.  # noqa: E501

        :param detected_source_language: The detected_source_language of this TranslateTextResponse.  # noqa: E501
        :type: str
        """

        self._detected_source_language = detected_source_language

    @property
    def text(self):
        """Gets the text of this TranslateTextResponse.  # noqa: E501

        Translated text.  # noqa: E501

        :return: The text of this TranslateTextResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TranslateTextResponse.

        Translated text.  # noqa: E501

        :param text: The text of this TranslateTextResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if not isinstance(other, TranslateTextResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateTextResponse):
            return True

        return self.to_dict() != other.to_dict()
