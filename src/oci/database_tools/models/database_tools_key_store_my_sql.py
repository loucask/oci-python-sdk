# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsKeyStoreMySql(object):
    """
    The details of the key store.
    """

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySql.
    #: This constant has a value of "CLIENT_CERTIFICATE_PEM"
    KEY_STORE_TYPE_CLIENT_CERTIFICATE_PEM = "CLIENT_CERTIFICATE_PEM"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySql.
    #: This constant has a value of "CLIENT_PRIVATE_KEY_PEM"
    KEY_STORE_TYPE_CLIENT_PRIVATE_KEY_PEM = "CLIENT_PRIVATE_KEY_PEM"

    #: A constant which can be used with the key_store_type property of a DatabaseToolsKeyStoreMySql.
    #: This constant has a value of "CA_CERTIFICATE_PEM"
    KEY_STORE_TYPE_CA_CERTIFICATE_PEM = "CA_CERTIFICATE_PEM"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsKeyStoreMySql object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_store_type:
            The value to assign to the key_store_type property of this DatabaseToolsKeyStoreMySql.
            Allowed values for this property are: "CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type key_store_type: str

        :param key_store_content:
            The value to assign to the key_store_content property of this DatabaseToolsKeyStoreMySql.
        :type key_store_content: oci.database_tools.models.DatabaseToolsKeyStoreContentMySql

        :param key_store_password:
            The value to assign to the key_store_password property of this DatabaseToolsKeyStoreMySql.
        :type key_store_password: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySql

        """
        self.swagger_types = {
            'key_store_type': 'str',
            'key_store_content': 'DatabaseToolsKeyStoreContentMySql',
            'key_store_password': 'DatabaseToolsKeyStorePasswordMySql'
        }

        self.attribute_map = {
            'key_store_type': 'keyStoreType',
            'key_store_content': 'keyStoreContent',
            'key_store_password': 'keyStorePassword'
        }

        self._key_store_type = None
        self._key_store_content = None
        self._key_store_password = None

    @property
    def key_store_type(self):
        """
        Gets the key_store_type of this DatabaseToolsKeyStoreMySql.
        The key store type.

        Allowed values for this property are: "CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The key_store_type of this DatabaseToolsKeyStoreMySql.
        :rtype: str
        """
        return self._key_store_type

    @key_store_type.setter
    def key_store_type(self, key_store_type):
        """
        Sets the key_store_type of this DatabaseToolsKeyStoreMySql.
        The key store type.


        :param key_store_type: The key_store_type of this DatabaseToolsKeyStoreMySql.
        :type: str
        """
        allowed_values = ["CLIENT_CERTIFICATE_PEM", "CLIENT_PRIVATE_KEY_PEM", "CA_CERTIFICATE_PEM"]
        if not value_allowed_none_or_none_sentinel(key_store_type, allowed_values):
            key_store_type = 'UNKNOWN_ENUM_VALUE'
        self._key_store_type = key_store_type

    @property
    def key_store_content(self):
        """
        Gets the key_store_content of this DatabaseToolsKeyStoreMySql.

        :return: The key_store_content of this DatabaseToolsKeyStoreMySql.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStoreContentMySql
        """
        return self._key_store_content

    @key_store_content.setter
    def key_store_content(self, key_store_content):
        """
        Sets the key_store_content of this DatabaseToolsKeyStoreMySql.

        :param key_store_content: The key_store_content of this DatabaseToolsKeyStoreMySql.
        :type: oci.database_tools.models.DatabaseToolsKeyStoreContentMySql
        """
        self._key_store_content = key_store_content

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this DatabaseToolsKeyStoreMySql.

        :return: The key_store_password of this DatabaseToolsKeyStoreMySql.
        :rtype: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySql
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this DatabaseToolsKeyStoreMySql.

        :param key_store_password: The key_store_password of this DatabaseToolsKeyStoreMySql.
        :type: oci.database_tools.models.DatabaseToolsKeyStorePasswordMySql
        """
        self._key_store_password = key_store_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
