# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateServiceCatalogDetails(object):
    """
    The model for parameter needed to create service catalog.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateServiceCatalogDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateServiceCatalogDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateServiceCatalogDetails.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateServiceCatalogDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateServiceCatalogDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateServiceCatalogDetails.
        The unique identifier for the compartment where the service catalog will be created.


        :return: The compartment_id of this CreateServiceCatalogDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateServiceCatalogDetails.
        The unique identifier for the compartment where the service catalog will be created.


        :param compartment_id: The compartment_id of this CreateServiceCatalogDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateServiceCatalogDetails.
        The display name of the service catalog.


        :return: The display_name of this CreateServiceCatalogDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateServiceCatalogDetails.
        The display name of the service catalog.


        :param display_name: The display_name of this CreateServiceCatalogDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateServiceCatalogDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateServiceCatalogDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateServiceCatalogDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateServiceCatalogDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateServiceCatalogDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateServiceCatalogDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateServiceCatalogDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateServiceCatalogDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
