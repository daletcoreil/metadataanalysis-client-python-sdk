# coding: utf-8

"""
    Dalet Metadata Analysis API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cortexsupport@dalet.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import metadataanalysis_client
from metadataanalysis_client.models.mention import Mention  # noqa: E501
from metadataanalysis_client.rest import ApiException

class TestMention(unittest.TestCase):
    """Mention unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Mention
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metadataanalysis_client.models.mention.Mention()  # noqa: E501
        if include_optional :
            return Mention(
                text = metadataanalysis_client.models.span.Span(
                    content = '0', 
                    begin_offset = 1.337, ), 
                type = 'TYPEUNKNOWN'
            )
        else :
            return Mention(
        )

    def testMention(self):
        """Test Mention"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
