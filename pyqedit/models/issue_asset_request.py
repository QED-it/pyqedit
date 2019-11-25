# coding: utf-8

"""
    QEDIT - Asset Transfers

    This SDK provides a programmatic way for interacting with QEDIT's _Asset Transfer_ API. The specification definition file is publicly available [in this repository](https://github.com/QED-it/asset_transfers_dev_guide/).   # noqa: E501

    OpenAPI spec version: 1.6.2
    Contact: dev@qed-it.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IssueAssetRequest(object):
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
        'wallet_id': 'str',
        'authorization': 'str',
        'recipient_address': 'str',
        'asset_id': 'str',
        'amount': 'int',
        'confidential': 'bool',
        'memo': 'str'
    }

    attribute_map = {
        'wallet_id': 'wallet_id',
        'authorization': 'authorization',
        'recipient_address': 'recipient_address',
        'asset_id': 'asset_id',
        'amount': 'amount',
        'confidential': 'confidential',
        'memo': 'memo'
    }

    def __init__(self, wallet_id=None, authorization=None, recipient_address=None, asset_id=None, amount=None, confidential=None, memo=None):  # noqa: E501
        """IssueAssetRequest - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_id = None
        self._authorization = None
        self._recipient_address = None
        self._asset_id = None
        self._amount = None
        self._confidential = None
        self._memo = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.authorization = authorization
        self.recipient_address = recipient_address
        self.asset_id = asset_id
        self.amount = amount
        self.confidential = confidential
        self.memo = memo

    @property
    def wallet_id(self):
        """Gets the wallet_id of this IssueAssetRequest.  # noqa: E501

        The ID of the Wallet that has the required Issuance privileges  # noqa: E501

        :return: The wallet_id of this IssueAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this IssueAssetRequest.

        The ID of the Wallet that has the required Issuance privileges  # noqa: E501

        :param wallet_id: The wallet_id of this IssueAssetRequest.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def authorization(self):
        """Gets the authorization of this IssueAssetRequest.  # noqa: E501

        The authorization password for the Wallet that has the Issuance privileges  # noqa: E501

        :return: The authorization of this IssueAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this IssueAssetRequest.

        The authorization password for the Wallet that has the Issuance privileges  # noqa: E501

        :param authorization: The authorization of this IssueAssetRequest.  # noqa: E501
        :type: str
        """
        if authorization is None:
            raise ValueError("Invalid value for `authorization`, must not be `None`")  # noqa: E501

        self._authorization = authorization

    @property
    def recipient_address(self):
        """Gets the recipient_address of this IssueAssetRequest.  # noqa: E501

        The Address of the recipient of the issued Assets  # noqa: E501

        :return: The recipient_address of this IssueAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_address

    @recipient_address.setter
    def recipient_address(self, recipient_address):
        """Sets the recipient_address of this IssueAssetRequest.

        The Address of the recipient of the issued Assets  # noqa: E501

        :param recipient_address: The recipient_address of this IssueAssetRequest.  # noqa: E501
        :type: str
        """
        if recipient_address is None:
            raise ValueError("Invalid value for `recipient_address`, must not be `None`")  # noqa: E501

        self._recipient_address = recipient_address

    @property
    def asset_id(self):
        """Gets the asset_id of this IssueAssetRequest.  # noqa: E501

        The ID of an Asset Type. It must be a string of length 0 to 40 characters. Allowed characters are lower- and uppercase letters, digits, dot (.), and hyphen (-). It must not end with an hyphen. Asset IDs are case-sensitive.   # noqa: E501

        :return: The asset_id of this IssueAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this IssueAssetRequest.

        The ID of an Asset Type. It must be a string of length 0 to 40 characters. Allowed characters are lower- and uppercase letters, digits, dot (.), and hyphen (-). It must not end with an hyphen. Asset IDs are case-sensitive.   # noqa: E501

        :param asset_id: The asset_id of this IssueAssetRequest.  # noqa: E501
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def amount(self):
        """Gets the amount of this IssueAssetRequest.  # noqa: E501

        the amount of Assets to issue  # noqa: E501

        :return: The amount of this IssueAssetRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this IssueAssetRequest.

        the amount of Assets to issue  # noqa: E501

        :param amount: The amount of this IssueAssetRequest.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def confidential(self):
        """Gets the confidential of this IssueAssetRequest.  # noqa: E501

        Boolean which should be true if the issuance should be confidential, and false of the Issuance should be public  # noqa: E501

        :return: The confidential of this IssueAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._confidential

    @confidential.setter
    def confidential(self, confidential):
        """Sets the confidential of this IssueAssetRequest.

        Boolean which should be true if the issuance should be confidential, and false of the Issuance should be public  # noqa: E501

        :param confidential: The confidential of this IssueAssetRequest.  # noqa: E501
        :type: bool
        """
        if confidential is None:
            raise ValueError("Invalid value for `confidential`, must not be `None`")  # noqa: E501

        self._confidential = confidential

    @property
    def memo(self):
        """Gets the memo of this IssueAssetRequest.  # noqa: E501


        :return: The memo of this IssueAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this IssueAssetRequest.


        :param memo: The memo of this IssueAssetRequest.  # noqa: E501
        :type: str
        """
        if memo is None:
            raise ValueError("Invalid value for `memo`, must not be `None`")  # noqa: E501

        self._memo = memo

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
        if not isinstance(other, IssueAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
