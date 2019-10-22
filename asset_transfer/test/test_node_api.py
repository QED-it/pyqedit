# coding: utf-8

"""
    QEDIT - Asset Transfers

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import asset_transfer
from asset_transfer.api.node_api import NodeApi  # noqa: E501
from asset_transfer.rest import ApiException


class TestNodeApi(unittest.TestCase):
    """NodeApi unit test stubs"""

    def setUp(self):
        self.api = asset_transfer.api.node_api.NodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_node_approve_task_post(self):
        """Test case for node_approve_task_post

        Approve task with pending incoming transaction [async call]  # noqa: E501
        """
        pass

    def test_node_cancel_task_post(self):
        """Test case for node_cancel_task_post

        Cancel task with pending incoming transaction both incoming and outgoing [async call]  # noqa: E501
        """
        pass

    def test_node_delete_wallet_post(self):
        """Test case for node_delete_wallet_post

        Delete a Wallet [async call]  # noqa: E501
        """
        pass

    def test_node_export_auditor_access_wallet_post(self):
        """Test case for node_export_auditor_access_wallet_post

        Export viewing credentials for a Wallet  # noqa: E501
        """
        pass

    def test_node_export_wallet_post(self):
        """Test case for node_export_wallet_post

        Export wallet secret key  # noqa: E501
        """
        pass

    def test_node_generate_wallet_post(self):
        """Test case for node_generate_wallet_post

        Generate a new Wallet  # noqa: E501
        """
        pass

    def test_node_get_all_wallets_post(self):
        """Test case for node_get_all_wallets_post

        Get all wallet IDs  # noqa: E501
        """
        pass

    def test_node_get_rules_post(self):
        """Test case for node_get_rules_post

        Get network governance Rules  # noqa: E501
        """
        pass

    def test_node_get_task_status_post(self):
        """Test case for node_get_task_status_post

        Get a specific task (by ID)  # noqa: E501
        """
        pass

    def test_node_get_tasks_post(self):
        """Test case for node_get_tasks_post

        Get a (potentially) filtered list of all Tasks  # noqa: E501
        """
        pass

    def test_node_import_auditor_access_wallet_post(self):
        """Test case for node_import_auditor_access_wallet_post

        Import viewing credentials for a Wallet [async call]  # noqa: E501
        """
        pass

    def test_node_import_wallet_post(self):
        """Test case for node_import_wallet_post

        Import Wallet from a known secret key and authorization [async call]  # noqa: E501
        """
        pass

    def test_node_unlock_wallet_post(self):
        """Test case for node_unlock_wallet_post

        Unlocks a wallet for a given amount of seconds [async call]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
