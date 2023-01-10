# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImagePullSecret(object):
    """
    The image pull secrets for accessing private registry to pull images for containers
    """

    #: A constant which can be used with the secret_type property of a ImagePullSecret.
    #: This constant has a value of "BASIC"
    SECRET_TYPE_BASIC = "BASIC"

    #: A constant which can be used with the secret_type property of a ImagePullSecret.
    #: This constant has a value of "VAULT"
    SECRET_TYPE_VAULT = "VAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new ImagePullSecret object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_instances.models.VaultImagePullSecret`
        * :class:`~oci.container_instances.models.BasicImagePullSecret`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param secret_type:
            The value to assign to the secret_type property of this ImagePullSecret.
            Allowed values for this property are: "BASIC", "VAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type secret_type: str

        :param registry_endpoint:
            The value to assign to the registry_endpoint property of this ImagePullSecret.
        :type registry_endpoint: str

        """
        self.swagger_types = {
            'secret_type': 'str',
            'registry_endpoint': 'str'
        }

        self.attribute_map = {
            'secret_type': 'secretType',
            'registry_endpoint': 'registryEndpoint'
        }

        self._secret_type = None
        self._registry_endpoint = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['secretType']

        if type == 'VAULT':
            return 'VaultImagePullSecret'

        if type == 'BASIC':
            return 'BasicImagePullSecret'
        else:
            return 'ImagePullSecret'

    @property
    def secret_type(self):
        """
        **[Required]** Gets the secret_type of this ImagePullSecret.
        The type of ImagePullSecret.

        Allowed values for this property are: "BASIC", "VAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The secret_type of this ImagePullSecret.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        """
        Sets the secret_type of this ImagePullSecret.
        The type of ImagePullSecret.


        :param secret_type: The secret_type of this ImagePullSecret.
        :type: str
        """
        allowed_values = ["BASIC", "VAULT"]
        if not value_allowed_none_or_none_sentinel(secret_type, allowed_values):
            secret_type = 'UNKNOWN_ENUM_VALUE'
        self._secret_type = secret_type

    @property
    def registry_endpoint(self):
        """
        **[Required]** Gets the registry_endpoint of this ImagePullSecret.
        The registry endpoint of the container image.


        :return: The registry_endpoint of this ImagePullSecret.
        :rtype: str
        """
        return self._registry_endpoint

    @registry_endpoint.setter
    def registry_endpoint(self, registry_endpoint):
        """
        Sets the registry_endpoint of this ImagePullSecret.
        The registry endpoint of the container image.


        :param registry_endpoint: The registry_endpoint of this ImagePullSecret.
        :type: str
        """
        self._registry_endpoint = registry_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
