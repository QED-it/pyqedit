# coding: utf-8

"""
    QEDIT - Asset Transfers

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pyqedit
from pyqedit.api.health_api import HealthApi  # noqa: E501
from pyqedit.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = pyqedit.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_post(self):
        """Test case for health_post

        Perform a healthcheck of the node and its dependent services  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
