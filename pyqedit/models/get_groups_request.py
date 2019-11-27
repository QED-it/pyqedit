# coding: utf-8

"""
    QEDIT - Asset Transfers

    This SDK provides a programmatic way for interacting with QEDIT's _Asset Transfer_ API. The specification definition file is publicly available [in this repository](https://github.com/QED-it/asset_transfers_dev_guide/).   # noqa: E501

    OpenAPI spec version: 1.7.0
    Contact: dev@qed-it.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetGroupsRequest(object):
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
        'start_index': 'int',
        'number_of_results': 'int'
    }

    attribute_map = {
        'wallet_id': 'wallet_id',
        'start_index': 'start_index',
        'number_of_results': 'number_of_results'
    }

    def __init__(self, wallet_id=None, start_index=None, number_of_results=None):  # noqa: E501
        """GetGroupsRequest - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_id = None
        self._start_index = None
        self._number_of_results = None
        self.discriminator = None

        self.wallet_id = wallet_id
        if start_index is not None:
            self.start_index = start_index
        if number_of_results is not None:
            self.number_of_results = number_of_results

    @property
    def wallet_id(self):
        """Gets the wallet_id of this GetGroupsRequest.  # noqa: E501

        The Node-specific identifier of the Wallet that is to leave the Group  # noqa: E501

        :return: The wallet_id of this GetGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this GetGroupsRequest.

        The Node-specific identifier of the Wallet that is to leave the Group  # noqa: E501

        :param wallet_id: The wallet_id of this GetGroupsRequest.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def start_index(self):
        """Gets the start_index of this GetGroupsRequest.  # noqa: E501

        An offset used to paginate through the available groups; indexing is 0-based; defaults to 0  # noqa: E501

        :return: The start_index of this GetGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this GetGroupsRequest.

        An offset used to paginate through the available groups; indexing is 0-based; defaults to 0  # noqa: E501

        :param start_index: The start_index of this GetGroupsRequest.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def number_of_results(self):
        """Gets the number_of_results of this GetGroupsRequest.  # noqa: E501

        Maximal number of results to fetch in this call; defaults to 100  # noqa: E501

        :return: The number_of_results of this GetGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_results

    @number_of_results.setter
    def number_of_results(self, number_of_results):
        """Sets the number_of_results of this GetGroupsRequest.

        Maximal number of results to fetch in this call; defaults to 100  # noqa: E501

        :param number_of_results: The number_of_results of this GetGroupsRequest.  # noqa: E501
        :type: int
        """

        self._number_of_results = number_of_results

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
        if not isinstance(other, GetGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other