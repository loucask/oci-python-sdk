# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    Details of the compartment-specific configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Configuration.
        :type compartment_id: str

        :param email_ids:
            The value to assign to the email_ids property of this Configuration.
        :type email_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this Configuration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Configuration.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'email_ids': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'email_ids': 'emailIds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._compartment_id = None
        self._email_ids = None
        self._time_created = None
        self._time_updated = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Configuration.
        The compartment `OCID`__ to which the configuration is specified.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Configuration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Configuration.
        The compartment `OCID`__ to which the configuration is specified.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Configuration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def email_ids(self):
        """
        **[Required]** Gets the email_ids of this Configuration.
        The list of associated configuration email IDs.


        :return: The email_ids of this Configuration.
        :rtype: list[str]
        """
        return self._email_ids

    @email_ids.setter
    def email_ids(self, email_ids):
        """
        Sets the email_ids of this Configuration.
        The list of associated configuration email IDs.


        :param email_ids: The email_ids of this Configuration.
        :type: list[str]
        """
        self._email_ids = email_ids

    @property
    def time_created(self):
        """
        Gets the time_created of this Configuration.
        The time the configuration was created. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Configuration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Configuration.
        The time the configuration was created. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Configuration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Configuration.
        The time the configuration was updated. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Configuration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Configuration.
        The time the configuration was updated. An `RFC 3339`__-formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Configuration.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
