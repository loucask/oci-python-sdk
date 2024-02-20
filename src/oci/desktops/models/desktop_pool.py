# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopPool(object):
    """
    Provides information about a desktop pool including all configuration parameters.
    """

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DesktopPool.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopPool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DesktopPool.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DesktopPool.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DesktopPool.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DesktopPool.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DesktopPool.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DesktopPool.
        :type time_created: datetime

        :param maximum_size:
            The value to assign to the maximum_size property of this DesktopPool.
        :type maximum_size: int

        :param standby_size:
            The value to assign to the standby_size property of this DesktopPool.
        :type standby_size: int

        :param shape_name:
            The value to assign to the shape_name property of this DesktopPool.
        :type shape_name: str

        :param is_storage_enabled:
            The value to assign to the is_storage_enabled property of this DesktopPool.
        :type is_storage_enabled: bool

        :param storage_size_in_gbs:
            The value to assign to the storage_size_in_gbs property of this DesktopPool.
        :type storage_size_in_gbs: int

        :param storage_backup_policy_id:
            The value to assign to the storage_backup_policy_id property of this DesktopPool.
        :type storage_backup_policy_id: str

        :param device_policy:
            The value to assign to the device_policy property of this DesktopPool.
        :type device_policy: oci.desktops.models.DesktopDevicePolicy

        :param availability_policy:
            The value to assign to the availability_policy property of this DesktopPool.
        :type availability_policy: oci.desktops.models.DesktopAvailabilityPolicy

        :param image:
            The value to assign to the image property of this DesktopPool.
        :type image: oci.desktops.models.DesktopImage

        :param network_configuration:
            The value to assign to the network_configuration property of this DesktopPool.
        :type network_configuration: oci.desktops.models.DesktopNetworkConfiguration

        :param time_start_scheduled:
            The value to assign to the time_start_scheduled property of this DesktopPool.
        :type time_start_scheduled: datetime

        :param time_stop_scheduled:
            The value to assign to the time_stop_scheduled property of this DesktopPool.
        :type time_stop_scheduled: datetime

        :param contact_details:
            The value to assign to the contact_details property of this DesktopPool.
        :type contact_details: str

        :param are_privileged_users:
            The value to assign to the are_privileged_users property of this DesktopPool.
        :type are_privileged_users: bool

        :param availability_domain:
            The value to assign to the availability_domain property of this DesktopPool.
        :type availability_domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DesktopPool.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DesktopPool.
        :type defined_tags: dict(str, dict(str, object))

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DesktopPool.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'maximum_size': 'int',
            'standby_size': 'int',
            'shape_name': 'str',
            'is_storage_enabled': 'bool',
            'storage_size_in_gbs': 'int',
            'storage_backup_policy_id': 'str',
            'device_policy': 'DesktopDevicePolicy',
            'availability_policy': 'DesktopAvailabilityPolicy',
            'image': 'DesktopImage',
            'network_configuration': 'DesktopNetworkConfiguration',
            'time_start_scheduled': 'datetime',
            'time_stop_scheduled': 'datetime',
            'contact_details': 'str',
            'are_privileged_users': 'bool',
            'availability_domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'maximum_size': 'maximumSize',
            'standby_size': 'standbySize',
            'shape_name': 'shapeName',
            'is_storage_enabled': 'isStorageEnabled',
            'storage_size_in_gbs': 'storageSizeInGBs',
            'storage_backup_policy_id': 'storageBackupPolicyId',
            'device_policy': 'devicePolicy',
            'availability_policy': 'availabilityPolicy',
            'image': 'image',
            'network_configuration': 'networkConfiguration',
            'time_start_scheduled': 'timeStartScheduled',
            'time_stop_scheduled': 'timeStopScheduled',
            'contact_details': 'contactDetails',
            'are_privileged_users': 'arePrivilegedUsers',
            'availability_domain': 'availabilityDomain',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'nsg_ids': 'nsgIds'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._time_created = None
        self._maximum_size = None
        self._standby_size = None
        self._shape_name = None
        self._is_storage_enabled = None
        self._storage_size_in_gbs = None
        self._storage_backup_policy_id = None
        self._device_policy = None
        self._availability_policy = None
        self._image = None
        self._network_configuration = None
        self._time_start_scheduled = None
        self._time_stop_scheduled = None
        self._contact_details = None
        self._are_privileged_users = None
        self._availability_domain = None
        self._freeform_tags = None
        self._defined_tags = None
        self._nsg_ids = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DesktopPool.
        The OCID of the desktop pool.


        :return: The id of this DesktopPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DesktopPool.
        The OCID of the desktop pool.


        :param id: The id of this DesktopPool.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DesktopPool.
        The OCID of the compartment of the desktop pool.


        :return: The compartment_id of this DesktopPool.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DesktopPool.
        The OCID of the compartment of the desktop pool.


        :param compartment_id: The compartment_id of this DesktopPool.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DesktopPool.
        A user friendly display name. Avoid entering confidential information.


        :return: The display_name of this DesktopPool.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DesktopPool.
        A user friendly display name. Avoid entering confidential information.


        :param display_name: The display_name of this DesktopPool.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DesktopPool.
        A user friendly description providing additional information about the resource.
        Avoid entering confidential information.


        :return: The description of this DesktopPool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DesktopPool.
        A user friendly description providing additional information about the resource.
        Avoid entering confidential information.


        :param description: The description of this DesktopPool.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DesktopPool.
        The current state of the desktop pool.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DesktopPool.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DesktopPool.
        The current state of the desktop pool.


        :param lifecycle_state: The lifecycle_state of this DesktopPool.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DesktopPool.
        The date and time the resource was created.


        :return: The time_created of this DesktopPool.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DesktopPool.
        The date and time the resource was created.


        :param time_created: The time_created of this DesktopPool.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def maximum_size(self):
        """
        **[Required]** Gets the maximum_size of this DesktopPool.
        The maximum number of desktops permitted in the desktop pool.


        :return: The maximum_size of this DesktopPool.
        :rtype: int
        """
        return self._maximum_size

    @maximum_size.setter
    def maximum_size(self, maximum_size):
        """
        Sets the maximum_size of this DesktopPool.
        The maximum number of desktops permitted in the desktop pool.


        :param maximum_size: The maximum_size of this DesktopPool.
        :type: int
        """
        self._maximum_size = maximum_size

    @property
    def standby_size(self):
        """
        **[Required]** Gets the standby_size of this DesktopPool.
        The maximum number of standby desktops available in the desktop pool.


        :return: The standby_size of this DesktopPool.
        :rtype: int
        """
        return self._standby_size

    @standby_size.setter
    def standby_size(self, standby_size):
        """
        Sets the standby_size of this DesktopPool.
        The maximum number of standby desktops available in the desktop pool.


        :param standby_size: The standby_size of this DesktopPool.
        :type: int
        """
        self._standby_size = standby_size

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this DesktopPool.
        The shape of the desktop pool.


        :return: The shape_name of this DesktopPool.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this DesktopPool.
        The shape of the desktop pool.


        :param shape_name: The shape_name of this DesktopPool.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def is_storage_enabled(self):
        """
        **[Required]** Gets the is_storage_enabled of this DesktopPool.
        Indicates whether storage is enabled for the desktop pool.


        :return: The is_storage_enabled of this DesktopPool.
        :rtype: bool
        """
        return self._is_storage_enabled

    @is_storage_enabled.setter
    def is_storage_enabled(self, is_storage_enabled):
        """
        Sets the is_storage_enabled of this DesktopPool.
        Indicates whether storage is enabled for the desktop pool.


        :param is_storage_enabled: The is_storage_enabled of this DesktopPool.
        :type: bool
        """
        self._is_storage_enabled = is_storage_enabled

    @property
    def storage_size_in_gbs(self):
        """
        **[Required]** Gets the storage_size_in_gbs of this DesktopPool.
        The size in GBs of the storage for the desktop pool.


        :return: The storage_size_in_gbs of this DesktopPool.
        :rtype: int
        """
        return self._storage_size_in_gbs

    @storage_size_in_gbs.setter
    def storage_size_in_gbs(self, storage_size_in_gbs):
        """
        Sets the storage_size_in_gbs of this DesktopPool.
        The size in GBs of the storage for the desktop pool.


        :param storage_size_in_gbs: The storage_size_in_gbs of this DesktopPool.
        :type: int
        """
        self._storage_size_in_gbs = storage_size_in_gbs

    @property
    def storage_backup_policy_id(self):
        """
        **[Required]** Gets the storage_backup_policy_id of this DesktopPool.
        The backup policy OCID of the storage.


        :return: The storage_backup_policy_id of this DesktopPool.
        :rtype: str
        """
        return self._storage_backup_policy_id

    @storage_backup_policy_id.setter
    def storage_backup_policy_id(self, storage_backup_policy_id):
        """
        Sets the storage_backup_policy_id of this DesktopPool.
        The backup policy OCID of the storage.


        :param storage_backup_policy_id: The storage_backup_policy_id of this DesktopPool.
        :type: str
        """
        self._storage_backup_policy_id = storage_backup_policy_id

    @property
    def device_policy(self):
        """
        **[Required]** Gets the device_policy of this DesktopPool.

        :return: The device_policy of this DesktopPool.
        :rtype: oci.desktops.models.DesktopDevicePolicy
        """
        return self._device_policy

    @device_policy.setter
    def device_policy(self, device_policy):
        """
        Sets the device_policy of this DesktopPool.

        :param device_policy: The device_policy of this DesktopPool.
        :type: oci.desktops.models.DesktopDevicePolicy
        """
        self._device_policy = device_policy

    @property
    def availability_policy(self):
        """
        **[Required]** Gets the availability_policy of this DesktopPool.

        :return: The availability_policy of this DesktopPool.
        :rtype: oci.desktops.models.DesktopAvailabilityPolicy
        """
        return self._availability_policy

    @availability_policy.setter
    def availability_policy(self, availability_policy):
        """
        Sets the availability_policy of this DesktopPool.

        :param availability_policy: The availability_policy of this DesktopPool.
        :type: oci.desktops.models.DesktopAvailabilityPolicy
        """
        self._availability_policy = availability_policy

    @property
    def image(self):
        """
        **[Required]** Gets the image of this DesktopPool.

        :return: The image of this DesktopPool.
        :rtype: oci.desktops.models.DesktopImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this DesktopPool.

        :param image: The image of this DesktopPool.
        :type: oci.desktops.models.DesktopImage
        """
        self._image = image

    @property
    def network_configuration(self):
        """
        **[Required]** Gets the network_configuration of this DesktopPool.

        :return: The network_configuration of this DesktopPool.
        :rtype: oci.desktops.models.DesktopNetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this DesktopPool.

        :param network_configuration: The network_configuration of this DesktopPool.
        :type: oci.desktops.models.DesktopNetworkConfiguration
        """
        self._network_configuration = network_configuration

    @property
    def time_start_scheduled(self):
        """
        Gets the time_start_scheduled of this DesktopPool.
        The start time of the desktop pool.


        :return: The time_start_scheduled of this DesktopPool.
        :rtype: datetime
        """
        return self._time_start_scheduled

    @time_start_scheduled.setter
    def time_start_scheduled(self, time_start_scheduled):
        """
        Sets the time_start_scheduled of this DesktopPool.
        The start time of the desktop pool.


        :param time_start_scheduled: The time_start_scheduled of this DesktopPool.
        :type: datetime
        """
        self._time_start_scheduled = time_start_scheduled

    @property
    def time_stop_scheduled(self):
        """
        Gets the time_stop_scheduled of this DesktopPool.
        The stop time of the desktop pool.


        :return: The time_stop_scheduled of this DesktopPool.
        :rtype: datetime
        """
        return self._time_stop_scheduled

    @time_stop_scheduled.setter
    def time_stop_scheduled(self, time_stop_scheduled):
        """
        Sets the time_stop_scheduled of this DesktopPool.
        The stop time of the desktop pool.


        :param time_stop_scheduled: The time_stop_scheduled of this DesktopPool.
        :type: datetime
        """
        self._time_stop_scheduled = time_stop_scheduled

    @property
    def contact_details(self):
        """
        **[Required]** Gets the contact_details of this DesktopPool.
        Contact information of the desktop pool administrator.
        Avoid entering confidential information.


        :return: The contact_details of this DesktopPool.
        :rtype: str
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """
        Sets the contact_details of this DesktopPool.
        Contact information of the desktop pool administrator.
        Avoid entering confidential information.


        :param contact_details: The contact_details of this DesktopPool.
        :type: str
        """
        self._contact_details = contact_details

    @property
    def are_privileged_users(self):
        """
        **[Required]** Gets the are_privileged_users of this DesktopPool.
        Indicates whether desktop pool users have administrative privileges on their desktop.


        :return: The are_privileged_users of this DesktopPool.
        :rtype: bool
        """
        return self._are_privileged_users

    @are_privileged_users.setter
    def are_privileged_users(self, are_privileged_users):
        """
        Sets the are_privileged_users of this DesktopPool.
        Indicates whether desktop pool users have administrative privileges on their desktop.


        :param are_privileged_users: The are_privileged_users of this DesktopPool.
        :type: bool
        """
        self._are_privileged_users = are_privileged_users

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DesktopPool.
        The availability domain of the desktop pool.


        :return: The availability_domain of this DesktopPool.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DesktopPool.
        The availability domain of the desktop pool.


        :param availability_domain: The availability_domain of this DesktopPool.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DesktopPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DesktopPool.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DesktopPool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DesktopPool.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DesktopPool.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DesktopPool.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DesktopPool.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DesktopPool.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DesktopPool.
        A list of network security groups for the desktop pool.


        :return: The nsg_ids of this DesktopPool.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DesktopPool.
        A list of network security groups for the desktop pool.


        :param nsg_ids: The nsg_ids of this DesktopPool.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
