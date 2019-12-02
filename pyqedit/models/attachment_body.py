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


class AttachmentBody(object):
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
        'name': 'str',
        'content_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'content_type': 'content_type',
        'content': 'content'
    }

    def __init__(self, name=None, content_type=None, content=None):  # noqa: E501
        """AttachmentBody - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._content_type = None
        self._content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if content_type is not None:
            self.content_type = content_type
        self.content = content

    @property
    def name(self):
        """Gets the name of this AttachmentBody.  # noqa: E501

        A name used by the caller of the API to describe the Attachment; does not have to be unique; should not be relied upon to uniquely identify the Attachment; defaults to the empty string (\"\")  # noqa: E501

        :return: The name of this AttachmentBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttachmentBody.

        A name used by the caller of the API to describe the Attachment; does not have to be unique; should not be relied upon to uniquely identify the Attachment; defaults to the empty string (\"\")  # noqa: E501

        :param name: The name of this AttachmentBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def content_type(self):
        """Gets the content_type of this AttachmentBody.  # noqa: E501

        The media type (a.k.a. MIME type) of the content; defaults to 'application/x-binary'  # noqa: E501

        :return: The content_type of this AttachmentBody.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AttachmentBody.

        The media type (a.k.a. MIME type) of the content; defaults to 'application/x-binary'  # noqa: E501

        :param content_type: The content_type of this AttachmentBody.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this AttachmentBody.  # noqa: E501

        The representation of the Attachment in standard base64 encoding without padding (see RFC-4648)  # noqa: E501

        :return: The content of this AttachmentBody.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this AttachmentBody.

        The representation of the Attachment in standard base64 encoding without padding (see RFC-4648)  # noqa: E501

        :param content: The content of this AttachmentBody.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, AttachmentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
