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


class UploadAttachmentRequest(object):
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
        'group_id': 'str',
        'body': 'AttachmentBody'
    }

    attribute_map = {
        'wallet_id': 'wallet_id',
        'authorization': 'authorization',
        'group_id': 'group_id',
        'body': 'body'
    }

    def __init__(self, wallet_id=None, authorization=None, group_id=None, body=None):  # noqa: E501
        """UploadAttachmentRequest - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_id = None
        self._authorization = None
        self._group_id = None
        self._body = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.authorization = authorization
        self.group_id = group_id
        self.body = body

    @property
    def wallet_id(self):
        """Gets the wallet_id of this UploadAttachmentRequest.  # noqa: E501

        The Node-specific identifier of the Wallet whose credentials should be used to upload the Attachment  # noqa: E501

        :return: The wallet_id of this UploadAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this UploadAttachmentRequest.

        The Node-specific identifier of the Wallet whose credentials should be used to upload the Attachment  # noqa: E501

        :param wallet_id: The wallet_id of this UploadAttachmentRequest.  # noqa: E501
        :type: str
        """
        if wallet_id is None:
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def authorization(self):
        """Gets the authorization of this UploadAttachmentRequest.  # noqa: E501

        The authorization password for the Wallet  # noqa: E501

        :return: The authorization of this UploadAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this UploadAttachmentRequest.

        The authorization password for the Wallet  # noqa: E501

        :param authorization: The authorization of this UploadAttachmentRequest.  # noqa: E501
        :type: str
        """
        if authorization is None:
            raise ValueError("Invalid value for `authorization`, must not be `None`")  # noqa: E501

        self._authorization = authorization

    @property
    def group_id(self):
        """Gets the group_id of this UploadAttachmentRequest.  # noqa: E501

        The globally-unique ID of the Group the Attachment should be shared with  # noqa: E501

        :return: The group_id of this UploadAttachmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UploadAttachmentRequest.

        The globally-unique ID of the Group the Attachment should be shared with  # noqa: E501

        :param group_id: The group_id of this UploadAttachmentRequest.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def body(self):
        """Gets the body of this UploadAttachmentRequest.  # noqa: E501


        :return: The body of this UploadAttachmentRequest.  # noqa: E501
        :rtype: AttachmentBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadAttachmentRequest.


        :param body: The body of this UploadAttachmentRequest.  # noqa: E501
        :type: AttachmentBody
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

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
        if not isinstance(other, UploadAttachmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other