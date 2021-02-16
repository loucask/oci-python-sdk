# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Migration(object):
    """
    The properties that define a migration. A migration represents the end-to-end workflow of moving an application from a source
    environment to Oracle Cloud Infrastructure. Each migration moves a single application to Oracle Cloud Infrastructure.
    For more information, see `Manage Migrations`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
    If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/application-migration/manage_migrations.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "JCS"
    APPLICATION_TYPE_JCS = "JCS"

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "SOACS"
    APPLICATION_TYPE_SOACS = "SOACS"

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "OIC"
    APPLICATION_TYPE_OIC = "OIC"

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "OAC"
    APPLICATION_TYPE_OAC = "OAC"

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "ICS"
    APPLICATION_TYPE_ICS = "ICS"

    #: A constant which can be used with the application_type property of a Migration.
    #: This constant has a value of "PCS"
    APPLICATION_TYPE_PCS = "PCS"

    #: A constant which can be used with the pre_created_target_database_type property of a Migration.
    #: This constant has a value of "DATABASE_SYSTEM"
    PRE_CREATED_TARGET_DATABASE_TYPE_DATABASE_SYSTEM = "DATABASE_SYSTEM"

    #: A constant which can be used with the pre_created_target_database_type property of a Migration.
    #: This constant has a value of "NOT_SET"
    PRE_CREATED_TARGET_DATABASE_TYPE_NOT_SET = "NOT_SET"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Migration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "DISCOVERING_APPLICATION"
    MIGRATION_STATE_DISCOVERING_APPLICATION = "DISCOVERING_APPLICATION"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "DISCOVERY_FAILED"
    MIGRATION_STATE_DISCOVERY_FAILED = "DISCOVERY_FAILED"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "MISSING_CONFIG_VALUES"
    MIGRATION_STATE_MISSING_CONFIG_VALUES = "MISSING_CONFIG_VALUES"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "READY"
    MIGRATION_STATE_READY = "READY"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "MIGRATING"
    MIGRATION_STATE_MIGRATING = "MIGRATING"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "MIGRATION_FAILED"
    MIGRATION_STATE_MIGRATION_FAILED = "MIGRATION_FAILED"

    #: A constant which can be used with the migration_state property of a Migration.
    #: This constant has a value of "MIGRATION_SUCCEEDED"
    MIGRATION_STATE_MIGRATION_SUCCEEDED = "MIGRATION_SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new Migration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Migration.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Migration.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Migration.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Migration.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Migration.
        :type time_created: datetime

        :param source_id:
            The value to assign to the source_id property of this Migration.
        :type source_id: str

        :param application_name:
            The value to assign to the application_name property of this Migration.
        :type application_name: str

        :param application_type:
            The value to assign to the application_type property of this Migration.
            Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type application_type: str

        :param pre_created_target_database_type:
            The value to assign to the pre_created_target_database_type property of this Migration.
            Allowed values for this property are: "DATABASE_SYSTEM", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pre_created_target_database_type: str

        :param is_selective_migration:
            The value to assign to the is_selective_migration property of this Migration.
        :type is_selective_migration: bool

        :param service_config:
            The value to assign to the service_config property of this Migration.
        :type service_config: dict(str, ConfigurationField)

        :param application_config:
            The value to assign to the application_config property of this Migration.
        :type application_config: dict(str, ConfigurationField)

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Migration.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Migration.
        :type lifecycle_details: str

        :param migration_state:
            The value to assign to the migration_state property of this Migration.
            Allowed values for this property are: "DISCOVERING_APPLICATION", "DISCOVERY_FAILED", "MISSING_CONFIG_VALUES", "READY", "MIGRATING", "MIGRATION_FAILED", "MIGRATION_SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type migration_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Migration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Migration.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'source_id': 'str',
            'application_name': 'str',
            'application_type': 'str',
            'pre_created_target_database_type': 'str',
            'is_selective_migration': 'bool',
            'service_config': 'dict(str, ConfigurationField)',
            'application_config': 'dict(str, ConfigurationField)',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'migration_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'source_id': 'sourceId',
            'application_name': 'applicationName',
            'application_type': 'applicationType',
            'pre_created_target_database_type': 'preCreatedTargetDatabaseType',
            'is_selective_migration': 'isSelectiveMigration',
            'service_config': 'serviceConfig',
            'application_config': 'applicationConfig',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'migration_state': 'migrationState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._source_id = None
        self._application_name = None
        self._application_type = None
        self._pre_created_target_database_type = None
        self._is_selective_migration = None
        self._service_config = None
        self._application_config = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._migration_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Migration.
        The `OCID`__ of the migration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Migration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Migration.
        The `OCID`__ of the migration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Migration.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Migration.
        The `OCID`__ of the compartment that contains the migration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Migration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Migration.
        The `OCID`__ of the compartment that contains the migration.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Migration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Migration.
        User-friendly name of the migration.


        :return: The display_name of this Migration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Migration.
        User-friendly name of the migration.


        :param display_name: The display_name of this Migration.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Migration.
        Description of the migration.


        :return: The description of this Migration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Migration.
        Description of the migration.


        :param description: The description of this Migration.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Migration.
        The date and time at which the migration was created, in the format defined by RFC3339.


        :return: The time_created of this Migration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Migration.
        The date and time at which the migration was created, in the format defined by RFC3339.


        :param time_created: The time_created of this Migration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def source_id(self):
        """
        Gets the source_id of this Migration.
        The `OCID`__ of the source with which this migration is associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_id of this Migration.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this Migration.
        The `OCID`__ of the source with which this migration is associated.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this Migration.
        :type: str
        """
        self._source_id = source_id

    @property
    def application_name(self):
        """
        Gets the application_name of this Migration.
        Name of the application which is being migrated. This is the name of the application in the source environment.


        :return: The application_name of this Migration.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this Migration.
        Name of the application which is being migrated. This is the name of the application in the source environment.


        :param application_name: The application_name of this Migration.
        :type: str
        """
        self._application_name = application_name

    @property
    def application_type(self):
        """
        Gets the application_type of this Migration.
        The type of application being migrated.

        Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The application_type of this Migration.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """
        Sets the application_type of this Migration.
        The type of application being migrated.


        :param application_type: The application_type of this Migration.
        :type: str
        """
        allowed_values = ["JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"]
        if not value_allowed_none_or_none_sentinel(application_type, allowed_values):
            application_type = 'UNKNOWN_ENUM_VALUE'
        self._application_type = application_type

    @property
    def pre_created_target_database_type(self):
        """
        Gets the pre_created_target_database_type of this Migration.
        The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
        Infrastrure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.

        Allowed values for this property are: "DATABASE_SYSTEM", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pre_created_target_database_type of this Migration.
        :rtype: str
        """
        return self._pre_created_target_database_type

    @pre_created_target_database_type.setter
    def pre_created_target_database_type(self, pre_created_target_database_type):
        """
        Sets the pre_created_target_database_type of this Migration.
        The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
        Infrastrure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance types.


        :param pre_created_target_database_type: The pre_created_target_database_type of this Migration.
        :type: str
        """
        allowed_values = ["DATABASE_SYSTEM", "NOT_SET"]
        if not value_allowed_none_or_none_sentinel(pre_created_target_database_type, allowed_values):
            pre_created_target_database_type = 'UNKNOWN_ENUM_VALUE'
        self._pre_created_target_database_type = pre_created_target_database_type

    @property
    def is_selective_migration(self):
        """
        Gets the is_selective_migration of this Migration.
        If set to `true`, Application Migration migrates the application resources selectively depending on the source.


        :return: The is_selective_migration of this Migration.
        :rtype: bool
        """
        return self._is_selective_migration

    @is_selective_migration.setter
    def is_selective_migration(self, is_selective_migration):
        """
        Sets the is_selective_migration of this Migration.
        If set to `true`, Application Migration migrates the application resources selectively depending on the source.


        :param is_selective_migration: The is_selective_migration of this Migration.
        :type: bool
        """
        self._is_selective_migration = is_selective_migration

    @property
    def service_config(self):
        """
        Gets the service_config of this Migration.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided
        to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
        CreateMigration operation.


        :return: The service_config of this Migration.
        :rtype: dict(str, ConfigurationField)
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """
        Sets the service_config of this Migration.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided
        to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
        CreateMigration operation.


        :param service_config: The service_config of this Migration.
        :type: dict(str, ConfigurationField)
        """
        self._service_config = service_config

    @property
    def application_config(self):
        """
        Gets the application_config of this Migration.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided
        to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
        CreateMigration operation.


        :return: The application_config of this Migration.
        :rtype: dict(str, ConfigurationField)
        """
        return self._application_config

    @application_config.setter
    def application_config(self, application_config):
        """
        Sets the application_config of this Migration.
        Configuration required to migrate the application. In addition to the key and value, additional fields are provided
        to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
        CreateMigration operation.


        :param application_config: The application_config of this Migration.
        :type: dict(str, ConfigurationField)
        """
        self._application_config = application_config

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Migration.
        The current state of the migration.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "SUCCEEDED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Migration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Migration.
        The current state of the migration.


        :param lifecycle_state: The lifecycle_state of this Migration.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "SUCCEEDED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Migration.
        Details about the current lifecycle state of the migration.


        :return: The lifecycle_details of this Migration.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Migration.
        Details about the current lifecycle state of the migration.


        :param lifecycle_details: The lifecycle_details of this Migration.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def migration_state(self):
        """
        Gets the migration_state of this Migration.
        The current state of the overall migration process.

        Allowed values for this property are: "DISCOVERING_APPLICATION", "DISCOVERY_FAILED", "MISSING_CONFIG_VALUES", "READY", "MIGRATING", "MIGRATION_FAILED", "MIGRATION_SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The migration_state of this Migration.
        :rtype: str
        """
        return self._migration_state

    @migration_state.setter
    def migration_state(self, migration_state):
        """
        Sets the migration_state of this Migration.
        The current state of the overall migration process.


        :param migration_state: The migration_state of this Migration.
        :type: str
        """
        allowed_values = ["DISCOVERING_APPLICATION", "DISCOVERY_FAILED", "MISSING_CONFIG_VALUES", "READY", "MIGRATING", "MIGRATION_FAILED", "MIGRATION_SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(migration_state, allowed_values):
            migration_state = 'UNKNOWN_ENUM_VALUE'
        self._migration_state = migration_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Migration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Migration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Migration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Migration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Migration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Migration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Migration.
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
