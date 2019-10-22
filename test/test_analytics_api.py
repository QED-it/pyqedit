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
from pyqedit.api.analytics_api import AnalyticsApi  # noqa: E501
from pyqedit.rest import ApiException


class TestAnalyticsApi(unittest.TestCase):
    """AnalyticsApi unit test stubs"""

    def setUp(self):
        self.api = pyqedit.api.analytics_api.AnalyticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_analytics_get_network_activity_post(self):
        """Test case for analytics_get_network_activity_post

        Get details on past blocks either by order using start_index and number_of_results or by the tx_hashes of the transactions  # noqa: E501
        """
        pass

    def test_analytics_get_sync_status_post(self):
        """Test case for analytics_get_sync_status_post

        Get blockchain sync status information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
