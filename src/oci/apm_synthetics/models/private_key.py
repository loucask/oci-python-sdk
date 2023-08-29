# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateKey(object):
    """
    The private key associated with the client certificate in PEM format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_name:
            The value to assign to the file_name property of this PrivateKey.
        :type file_name: str

        :param content:
            The value to assign to the content property of this PrivateKey.
        :type content: str

        """
        self.swagger_types = {
            'file_name': 'str',
            'content': 'str'
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'content': 'content'
        }

        self._file_name = None
        self._content = None

    @property
    def file_name(self):
        """
        **[Required]** Gets the file_name of this PrivateKey.
        Name of the private key file.


        :return: The file_name of this PrivateKey.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this PrivateKey.
        Name of the private key file.


        :param file_name: The file_name of this PrivateKey.
        :type: str
        """
        self._file_name = file_name

    @property
    def content(self):
        """
        **[Required]** Gets the content of this PrivateKey.
        Content of the private key file.


        :return: The content of this PrivateKey.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this PrivateKey.
        Content of the private key file.


        :param content: The content of this PrivateKey.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
