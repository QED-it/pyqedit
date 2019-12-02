# coding: utf-8

"""
    QEDIT - Asset Transfers

    This SDK provides a programmatic way for interacting with QEDIT's _Asset Transfer_ API. The specification definition file is publicly available [in this repository](https://github.com/QED-it/asset_transfers_dev_guide/).   # noqa: E501

    OpenAPI spec version: 1.7.2
    Contact: dev@qed-it.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AnalyticsConfidentialIssuanceDescription(object):
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
        'casset': 'str',
        'namespace': 'str',
        'zkproof': 'str'
    }

    attribute_map = {
        'casset': 'casset',
        'namespace': 'namespace',
        'zkproof': 'zkproof'
    }

    def __init__(self, casset=None, namespace=None, zkproof=None):  # noqa: E501
        """AnalyticsConfidentialIssuanceDescription - a model defined in OpenAPI"""  # noqa: E501

        self._casset = None
        self._namespace = None
        self._zkproof = None
        self.discriminator = None

        if casset is not None:
            self.casset = casset
        if namespace is not None:
            self.namespace = namespace
        if zkproof is not None:
            self.zkproof = zkproof

    @property
    def casset(self):
        """Gets the casset of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501

        The commitment to both the Asset Type and amount of the issued Note  # noqa: E501

        :return: The casset of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :rtype: str
        """
        return self._casset

    @casset.setter
    def casset(self, casset):
        """Sets the casset of this AnalyticsConfidentialIssuanceDescription.

        The commitment to both the Asset Type and amount of the issued Note  # noqa: E501

        :param casset: The casset of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :type: str
        """

        self._casset = casset

    @property
    def namespace(self):
        """Gets the namespace of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501

        A `Namespace` describes what Asset IDs can be issued in an Issuance Rule. It is a string in the same format as `AssetId`. Additionally, if it ends with a wildcard character `*`, then the namespace covers all asset IDs with the namespace as a prefix. Without a final wildcard, the namespace covers exactly one asset ID. Example: The namespace `currencies.dollar` covers only this exact asset type, while `currencies.*` covers all asset types that start with `currencies.`.   # noqa: E501

        :return: The namespace of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AnalyticsConfidentialIssuanceDescription.

        A `Namespace` describes what Asset IDs can be issued in an Issuance Rule. It is a string in the same format as `AssetId`. Additionally, if it ends with a wildcard character `*`, then the namespace covers all asset IDs with the namespace as a prefix. Without a final wildcard, the namespace covers exactly one asset ID. Example: The namespace `currencies.dollar` covers only this exact asset type, while `currencies.*` covers all asset types that start with `currencies.`.   # noqa: E501

        :param namespace: The namespace of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def zkproof(self):
        """Gets the zkproof of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501

        The Proof that the issued Asset Type indeed matches the reported Rule  # noqa: E501

        :return: The zkproof of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :rtype: str
        """
        return self._zkproof

    @zkproof.setter
    def zkproof(self, zkproof):
        """Sets the zkproof of this AnalyticsConfidentialIssuanceDescription.

        The Proof that the issued Asset Type indeed matches the reported Rule  # noqa: E501

        :param zkproof: The zkproof of this AnalyticsConfidentialIssuanceDescription.  # noqa: E501
        :type: str
        """

        self._zkproof = zkproof

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
        if not isinstance(other, AnalyticsConfidentialIssuanceDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
