# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopPoolDesktopSummary(object):
    """
    Provides information about a desktop within a desktop pool, such as if it is assigned to a user, the state, owner, desktop pool, resource id, and time created.
    """

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DesktopPoolDesktopSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopPoolDesktopSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DesktopPoolDesktopSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param instance_id:
            The value to assign to the instance_id property of this DesktopPoolDesktopSummary.
        :type instance_id: str

        :param user_name:
            The value to assign to the user_name property of this DesktopPoolDesktopSummary.
        :type user_name: str

        :param desktop_id:
            The value to assign to the desktop_id property of this DesktopPoolDesktopSummary.
        :type desktop_id: str

        :param is_assigned:
            The value to assign to the is_assigned property of this DesktopPoolDesktopSummary.
        :type is_assigned: bool

        :param time_created:
            The value to assign to the time_created property of this DesktopPoolDesktopSummary.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DesktopPoolDesktopSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DesktopPoolDesktopSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'instance_id': 'str',
            'user_name': 'str',
            'desktop_id': 'str',
            'is_assigned': 'bool',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'instance_id': 'instanceId',
            'user_name': 'userName',
            'desktop_id': 'desktopId',
            'is_assigned': 'isAssigned',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._lifecycle_state = None
        self._instance_id = None
        self._user_name = None
        self._desktop_id = None
        self._is_assigned = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DesktopPoolDesktopSummary.
        The state of the desktop.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DesktopPoolDesktopSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DesktopPoolDesktopSummary.
        The state of the desktop.


        :param lifecycle_state: The lifecycle_state of this DesktopPoolDesktopSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this DesktopPoolDesktopSummary.
        The OCID of the compute resource used by this desktop.


        :return: The instance_id of this DesktopPoolDesktopSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this DesktopPoolDesktopSummary.
        The OCID of the compute resource used by this desktop.


        :param instance_id: The instance_id of this DesktopPoolDesktopSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """
        Gets the user_name of this DesktopPoolDesktopSummary.
        The owner of the desktop.


        :return: The user_name of this DesktopPoolDesktopSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DesktopPoolDesktopSummary.
        The owner of the desktop.


        :param user_name: The user_name of this DesktopPoolDesktopSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def desktop_id(self):
        """
        **[Required]** Gets the desktop_id of this DesktopPoolDesktopSummary.
        The OCID of the desktop.


        :return: The desktop_id of this DesktopPoolDesktopSummary.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """
        Sets the desktop_id of this DesktopPoolDesktopSummary.
        The OCID of the desktop.


        :param desktop_id: The desktop_id of this DesktopPoolDesktopSummary.
        :type: str
        """
        self._desktop_id = desktop_id

    @property
    def is_assigned(self):
        """
        **[Required]** Gets the is_assigned of this DesktopPoolDesktopSummary.
        Indicates whether the desktop is assigned to a user.


        :return: The is_assigned of this DesktopPoolDesktopSummary.
        :rtype: bool
        """
        return self._is_assigned

    @is_assigned.setter
    def is_assigned(self, is_assigned):
        """
        Sets the is_assigned of this DesktopPoolDesktopSummary.
        Indicates whether the desktop is assigned to a user.


        :param is_assigned: The is_assigned of this DesktopPoolDesktopSummary.
        :type: bool
        """
        self._is_assigned = is_assigned

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DesktopPoolDesktopSummary.
        The date and time the resource was created.


        :return: The time_created of this DesktopPoolDesktopSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DesktopPoolDesktopSummary.
        The date and time the resource was created.


        :param time_created: The time_created of this DesktopPoolDesktopSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DesktopPoolDesktopSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DesktopPoolDesktopSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DesktopPoolDesktopSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DesktopPoolDesktopSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DesktopPoolDesktopSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DesktopPoolDesktopSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DesktopPoolDesktopSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DesktopPoolDesktopSummary.
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
