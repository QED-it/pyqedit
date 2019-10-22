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


class AnalyticsTransferTx(object):
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
        'spends': 'list[AnalyticsSpendDescription]',
        'outputs': 'list[AnalyticsOutputDescription]',
        'rk': 'str',
        'spend_auth_sig': 'str',
        'binding_sig': 'str'
    }

    attribute_map = {
        'spends': 'spends',
        'outputs': 'outputs',
        'rk': 'rk',
        'spend_auth_sig': 'spend_auth_sig',
        'binding_sig': 'binding_sig'
    }

    def __init__(self, spends=None, outputs=None, rk=None, spend_auth_sig=None, binding_sig=None):  # noqa: E501
        """AnalyticsTransferTx - a model defined in OpenAPI"""  # noqa: E501

        self._spends = None
        self._outputs = None
        self._rk = None
        self._spend_auth_sig = None
        self._binding_sig = None
        self.discriminator = None

        if spends is not None:
            self.spends = spends
        if outputs is not None:
            self.outputs = outputs
        if rk is not None:
            self.rk = rk
        if spend_auth_sig is not None:
            self.spend_auth_sig = spend_auth_sig
        if binding_sig is not None:
            self.binding_sig = binding_sig

    @property
    def spends(self):
        """Gets the spends of this AnalyticsTransferTx.  # noqa: E501

        The information and Proofs associated with the Assets spent in the Transfer  # noqa: E501

        :return: The spends of this AnalyticsTransferTx.  # noqa: E501
        :rtype: list[AnalyticsSpendDescription]
        """
        return self._spends

    @spends.setter
    def spends(self, spends):
        """Sets the spends of this AnalyticsTransferTx.

        The information and Proofs associated with the Assets spent in the Transfer  # noqa: E501

        :param spends: The spends of this AnalyticsTransferTx.  # noqa: E501
        :type: list[AnalyticsSpendDescription]
        """

        self._spends = spends

    @property
    def outputs(self):
        """Gets the outputs of this AnalyticsTransferTx.  # noqa: E501

        The information and Proofs associated with the Assets output from the Transfer  # noqa: E501

        :return: The outputs of this AnalyticsTransferTx.  # noqa: E501
        :rtype: list[AnalyticsOutputDescription]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this AnalyticsTransferTx.

        The information and Proofs associated with the Assets output from the Transfer  # noqa: E501

        :param outputs: The outputs of this AnalyticsTransferTx.  # noqa: E501
        :type: list[AnalyticsOutputDescription]
        """

        self._outputs = outputs

    @property
    def rk(self):
        """Gets the rk of this AnalyticsTransferTx.  # noqa: E501

        The re-randomized public key of the Wallet which created the Transfer  # noqa: E501

        :return: The rk of this AnalyticsTransferTx.  # noqa: E501
        :rtype: str
        """
        return self._rk

    @rk.setter
    def rk(self, rk):
        """Sets the rk of this AnalyticsTransferTx.

        The re-randomized public key of the Wallet which created the Transfer  # noqa: E501

        :param rk: The rk of this AnalyticsTransferTx.  # noqa: E501
        :type: str
        """

        self._rk = rk

    @property
    def spend_auth_sig(self):
        """Gets the spend_auth_sig of this AnalyticsTransferTx.  # noqa: E501

        The signature authorizing the spend of the Assets spent in the Transfer  # noqa: E501

        :return: The spend_auth_sig of this AnalyticsTransferTx.  # noqa: E501
        :rtype: str
        """
        return self._spend_auth_sig

    @spend_auth_sig.setter
    def spend_auth_sig(self, spend_auth_sig):
        """Sets the spend_auth_sig of this AnalyticsTransferTx.

        The signature authorizing the spend of the Assets spent in the Transfer  # noqa: E501

        :param spend_auth_sig: The spend_auth_sig of this AnalyticsTransferTx.  # noqa: E501
        :type: str
        """

        self._spend_auth_sig = spend_auth_sig

    @property
    def binding_sig(self):
        """Gets the binding_sig of this AnalyticsTransferTx.  # noqa: E501

        The signature binding the spent and output Assets and verifying the balance  # noqa: E501

        :return: The binding_sig of this AnalyticsTransferTx.  # noqa: E501
        :rtype: str
        """
        return self._binding_sig

    @binding_sig.setter
    def binding_sig(self, binding_sig):
        """Sets the binding_sig of this AnalyticsTransferTx.

        The signature binding the spent and output Assets and verifying the balance  # noqa: E501

        :param binding_sig: The binding_sig of this AnalyticsTransferTx.  # noqa: E501
        :type: str
        """

        self._binding_sig = binding_sig

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
        if not isinstance(other, AnalyticsTransferTx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
