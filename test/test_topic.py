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
from metadataanalysis_client.models.topic import Topic  # noqa: E501
from metadataanalysis_client.rest import ApiException

class TestTopic(unittest.TestCase):
    """Topic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Topic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metadataanalysis_client.models.topic.Topic()  # noqa: E501
        if include_optional :
            return Topic(
                id = '0', 
                label = '0', 
                wiki_link = '0', 
                score = 1.337, 
                wikidata_id = '0'
            )
        else :
            return Topic(
        )

    def testTopic(self):
        """Test Topic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
