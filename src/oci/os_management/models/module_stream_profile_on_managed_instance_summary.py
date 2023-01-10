# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStreamProfileOnManagedInstanceSummary(object):
    """
    Summary information pertaining to a module stream profile on a managed instance
    """

    #: A constant which can be used with the status property of a ModuleStreamProfileOnManagedInstanceSummary.
    #: This constant has a value of "INSTALLED"
    STATUS_INSTALLED = "INSTALLED"

    #: A constant which can be used with the status property of a ModuleStreamProfileOnManagedInstanceSummary.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStreamProfileOnManagedInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStreamProfileOnManagedInstanceSummary.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStreamProfileOnManagedInstanceSummary.
        :type stream_name: str

        :param profile_name:
            The value to assign to the profile_name property of this ModuleStreamProfileOnManagedInstanceSummary.
        :type profile_name: str

        :param status:
            The value to assign to the status property of this ModuleStreamProfileOnManagedInstanceSummary.
            Allowed values for this property are: "INSTALLED", "AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_modified:
            The value to assign to the time_modified property of this ModuleStreamProfileOnManagedInstanceSummary.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'profile_name': 'str',
            'status': 'str',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'profile_name': 'profileName',
            'status': 'status',
            'time_modified': 'timeModified'
        }

        self._module_name = None
        self._stream_name = None
        self._profile_name = None
        self._status = None
        self._time_modified = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the module that contains the stream profile


        :return: The module_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the module that contains the stream profile


        :param module_name: The module_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the stream that contains the profile


        :return: The stream_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the stream that contains the profile


        :param stream_name: The stream_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def profile_name(self):
        """
        **[Required]** Gets the profile_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the profile


        :return: The profile_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this ModuleStreamProfileOnManagedInstanceSummary.
        The name of the profile


        :param profile_name: The profile_name of this ModuleStreamProfileOnManagedInstanceSummary.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ModuleStreamProfileOnManagedInstanceSummary.
        The status of the profile.

        A profile with the \"INSTALLED\" status indicates that the profile has been
        installed.

        A profile with the \"AVAILABLE\" status indicates that the profile is
        not installed, but can be.

        Allowed values for this property are: "INSTALLED", "AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ModuleStreamProfileOnManagedInstanceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ModuleStreamProfileOnManagedInstanceSummary.
        The status of the profile.

        A profile with the \"INSTALLED\" status indicates that the profile has been
        installed.

        A profile with the \"AVAILABLE\" status indicates that the profile is
        not installed, but can be.


        :param status: The status of this ModuleStreamProfileOnManagedInstanceSummary.
        :type: str
        """
        allowed_values = ["INSTALLED", "AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ModuleStreamProfileOnManagedInstanceSummary.
        The date and time of the last status change for this profile, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this ModuleStreamProfileOnManagedInstanceSummary.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ModuleStreamProfileOnManagedInstanceSummary.
        The date and time of the last status change for this profile, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this ModuleStreamProfileOnManagedInstanceSummary.
        :type: datetime
        """
        self._time_modified = time_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
