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


class ExportWalletResponse(object):
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
        'encrypted_sk': 'str',
        'salt': 'str'
    }

    attribute_map = {
        'wallet_id': 'wallet_id',
        'encrypted_sk': 'encrypted_sk',
        'salt': 'salt'
    }

    def __init__(self, wallet_id=None, encrypted_sk=None, salt=None):  # noqa: E501
        """ExportWalletResponse - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_id = None
        self._encrypted_sk = None
        self._salt = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.encrypted_sk = encrypted_sk
        self.salt = salt

    @property
    def wallet_id(self):
        """Gets the wallet_id of this ExportWalletResponse.  # noqa: E501

        The ID of the exported Wallet in the Node from which it was exported  # noqa: E501

        :return: The wallet_id of this ExportWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this ExportWalletResponse.

        The ID of the exported Wallet in the Node from which it was exported  # noqa: E501

        :param wallet_id: The wallet_id of this ExportWalletResponse.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def encrypted_sk(self):
        """Gets the encrypted_sk of this ExportWalletResponse.  # noqa: E501

        The encrypted secret key of the Wallet  # noqa: E501

        :return: The encrypted_sk of this ExportWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_sk

    @encrypted_sk.setter
    def encrypted_sk(self, encrypted_sk):
        """Sets the encrypted_sk of this ExportWalletResponse.

        The encrypted secret key of the Wallet  # noqa: E501

        :param encrypted_sk: The encrypted_sk of this ExportWalletResponse.  # noqa: E501
        :type: str
        """
        if encrypted_sk is None:
            raise ValueError("Invalid value for `encrypted_sk`, must not be `None`")  # noqa: E501

        self._encrypted_sk = encrypted_sk

    @property
    def salt(self):
        """Gets the salt of this ExportWalletResponse.  # noqa: E501

        The salt used in the encryption of the secret key  # noqa: E501

        :return: The salt of this ExportWalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this ExportWalletResponse.

        The salt used in the encryption of the secret key  # noqa: E501

        :param salt: The salt of this ExportWalletResponse.  # noqa: E501
        :type: str
        """
        if salt is None:
            raise ValueError("Invalid value for `salt`, must not be `None`")  # noqa: E501

        self._salt = salt

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
        if not isinstance(other, ExportWalletResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
