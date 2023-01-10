# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataSourceDetails(object):
    """
    Creation of Data Source.
    """

    #: A constant which can be used with the data_source_feed_provider property of a CreateDataSourceDetails.
    #: This constant has a value of "LOGGINGQUERY"
    DATA_SOURCE_FEED_PROVIDER_LOGGINGQUERY = "LOGGINGQUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDataSourceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDataSourceDetails.
        :type compartment_id: str

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this CreateDataSourceDetails.
            Allowed values for this property are: "LOGGINGQUERY"
        :type data_source_feed_provider: str

        :param data_source_details:
            The value to assign to the data_source_details property of this CreateDataSourceDetails.
        :type data_source_details: oci.cloud_guard.models.DataSourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDataSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDataSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'data_source_feed_provider': 'str',
            'data_source_details': 'DataSourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'data_source_feed_provider': 'dataSourceFeedProvider',
            'data_source_details': 'dataSourceDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._data_source_feed_provider = None
        self._data_source_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDataSourceDetails.
        Data Source display name.


        :return: The display_name of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataSourceDetails.
        Data Source display name.


        :param display_name: The display_name of this CreateDataSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDataSourceDetails.
        CompartmentId of Data Source.


        :return: The compartment_id of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDataSourceDetails.
        CompartmentId of Data Source.


        :param compartment_id: The compartment_id of this CreateDataSourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def data_source_feed_provider(self):
        """
        **[Required]** Gets the data_source_feed_provider of this CreateDataSourceDetails.
        Possible type of dataSourceFeed Provider(LoggingQuery)

        Allowed values for this property are: "LOGGINGQUERY"


        :return: The data_source_feed_provider of this CreateDataSourceDetails.
        :rtype: str
        """
        return self._data_source_feed_provider

    @data_source_feed_provider.setter
    def data_source_feed_provider(self, data_source_feed_provider):
        """
        Sets the data_source_feed_provider of this CreateDataSourceDetails.
        Possible type of dataSourceFeed Provider(LoggingQuery)


        :param data_source_feed_provider: The data_source_feed_provider of this CreateDataSourceDetails.
        :type: str
        """
        allowed_values = ["LOGGINGQUERY"]
        if not value_allowed_none_or_none_sentinel(data_source_feed_provider, allowed_values):
            raise ValueError(
                "Invalid value for `data_source_feed_provider`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_source_feed_provider = data_source_feed_provider

    @property
    def data_source_details(self):
        """
        Gets the data_source_details of this CreateDataSourceDetails.

        :return: The data_source_details of this CreateDataSourceDetails.
        :rtype: oci.cloud_guard.models.DataSourceDetails
        """
        return self._data_source_details

    @data_source_details.setter
    def data_source_details(self, data_source_details):
        """
        Sets the data_source_details of this CreateDataSourceDetails.

        :param data_source_details: The data_source_details of this CreateDataSourceDetails.
        :type: oci.cloud_guard.models.DataSourceDetails
        """
        self._data_source_details = data_source_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDataSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this CreateDataSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDataSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this CreateDataSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDataSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDataSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDataSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDataSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
