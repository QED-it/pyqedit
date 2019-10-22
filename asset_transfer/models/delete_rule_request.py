# coding: utf-8

"""
    QEDIT - Asset Transfers

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DeleteRuleRequest(object):
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
        'rules_to_delete': 'list[Rule]'
    }

    attribute_map = {
        'wallet_id': 'wallet_id',
        'authorization': 'authorization',
        'rules_to_delete': 'rules_to_delete'
    }

    def __init__(self, wallet_id=None, authorization=None, rules_to_delete=None):  # noqa: E501
        """DeleteRuleRequest - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_id = None
        self._authorization = None
        self._rules_to_delete = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.authorization = authorization
        self.rules_to_delete = rules_to_delete

    @property
    def wallet_id(self):
        """Gets the wallet_id of this DeleteRuleRequest.  # noqa: E501

        The ID of the Wallet whose admin credentials should be used to delete the Rules  # noqa: E501

        :return: The wallet_id of this DeleteRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this DeleteRuleRequest.

        The ID of the Wallet whose admin credentials should be used to delete the Rules  # noqa: E501

        :param wallet_id: The wallet_id of this DeleteRuleRequest.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def authorization(self):
        """Gets the authorization of this DeleteRuleRequest.  # noqa: E501

        The authorization password for the Wallet whose admin credentials should be used to delete the Rules  # noqa: E501

        :return: The authorization of this DeleteRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this DeleteRuleRequest.

        The authorization password for the Wallet whose admin credentials should be used to delete the Rules  # noqa: E501

        :param authorization: The authorization of this DeleteRuleRequest.  # noqa: E501
        :type: str
        """
        if authorization is None:
            raise ValueError("Invalid value for `authorization`, must not be `None`")  # noqa: E501

        self._authorization = authorization

    @property
    def rules_to_delete(self):
        """Gets the rules_to_delete of this DeleteRuleRequest.  # noqa: E501

        The list of Rules to delete from the network  # noqa: E501

        :return: The rules_to_delete of this DeleteRuleRequest.  # noqa: E501
        :rtype: list[Rule]
        """
        return self._rules_to_delete

    @rules_to_delete.setter
    def rules_to_delete(self, rules_to_delete):
        """Sets the rules_to_delete of this DeleteRuleRequest.

        The list of Rules to delete from the network  # noqa: E501

        :param rules_to_delete: The rules_to_delete of this DeleteRuleRequest.  # noqa: E501
        :type: list[Rule]
        """
        if rules_to_delete is None:
            raise ValueError("Invalid value for `rules_to_delete`, must not be `None`")  # noqa: E501

        self._rules_to_delete = rules_to_delete

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
        if not isinstance(other, DeleteRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
