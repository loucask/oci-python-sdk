# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobDetails(object):
    """
    Parameters needed to create a new job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param project_id:
            The value to assign to the project_id property of this CreateJobDetails.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateJobDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateJobDetails.
        :type description: str

        :param job_configuration_details:
            The value to assign to the job_configuration_details property of this CreateJobDetails.
        :type job_configuration_details: oci.data_science.models.JobConfigurationDetails

        :param job_infrastructure_configuration_details:
            The value to assign to the job_infrastructure_configuration_details property of this CreateJobDetails.
        :type job_infrastructure_configuration_details: oci.data_science.models.JobInfrastructureConfigurationDetails

        :param job_environment_configuration_details:
            The value to assign to the job_environment_configuration_details property of this CreateJobDetails.
        :type job_environment_configuration_details: oci.data_science.models.JobEnvironmentConfigurationDetails

        :param job_log_configuration_details:
            The value to assign to the job_log_configuration_details property of this CreateJobDetails.
        :type job_log_configuration_details: oci.data_science.models.JobLogConfigurationDetails

        :param job_storage_mount_configuration_details_list:
            The value to assign to the job_storage_mount_configuration_details_list property of this CreateJobDetails.
        :type job_storage_mount_configuration_details_list: list[oci.data_science.models.StorageMountConfigurationDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'project_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'job_configuration_details': 'JobConfigurationDetails',
            'job_infrastructure_configuration_details': 'JobInfrastructureConfigurationDetails',
            'job_environment_configuration_details': 'JobEnvironmentConfigurationDetails',
            'job_log_configuration_details': 'JobLogConfigurationDetails',
            'job_storage_mount_configuration_details_list': 'list[StorageMountConfigurationDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'job_configuration_details': 'jobConfigurationDetails',
            'job_infrastructure_configuration_details': 'jobInfrastructureConfigurationDetails',
            'job_environment_configuration_details': 'jobEnvironmentConfigurationDetails',
            'job_log_configuration_details': 'jobLogConfigurationDetails',
            'job_storage_mount_configuration_details_list': 'jobStorageMountConfigurationDetailsList',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._project_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._job_configuration_details = None
        self._job_infrastructure_configuration_details = None
        self._job_environment_configuration_details = None
        self._job_log_configuration_details = None
        self._job_storage_mount_configuration_details_list = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateJobDetails.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateJobDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateJobDetails.
        The `OCID`__ of the project to associate the job with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateJobDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateJobDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateJobDetails.
        The `OCID`__ of the compartment where you want to create the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateJobDetails.
        A user-friendly display name for the resource.


        :return: The display_name of this CreateJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateJobDetails.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this CreateJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateJobDetails.
        A short description of the job.


        :return: The description of this CreateJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateJobDetails.
        A short description of the job.


        :param description: The description of this CreateJobDetails.
        :type: str
        """
        self._description = description

    @property
    def job_configuration_details(self):
        """
        **[Required]** Gets the job_configuration_details of this CreateJobDetails.

        :return: The job_configuration_details of this CreateJobDetails.
        :rtype: oci.data_science.models.JobConfigurationDetails
        """
        return self._job_configuration_details

    @job_configuration_details.setter
    def job_configuration_details(self, job_configuration_details):
        """
        Sets the job_configuration_details of this CreateJobDetails.

        :param job_configuration_details: The job_configuration_details of this CreateJobDetails.
        :type: oci.data_science.models.JobConfigurationDetails
        """
        self._job_configuration_details = job_configuration_details

    @property
    def job_infrastructure_configuration_details(self):
        """
        **[Required]** Gets the job_infrastructure_configuration_details of this CreateJobDetails.

        :return: The job_infrastructure_configuration_details of this CreateJobDetails.
        :rtype: oci.data_science.models.JobInfrastructureConfigurationDetails
        """
        return self._job_infrastructure_configuration_details

    @job_infrastructure_configuration_details.setter
    def job_infrastructure_configuration_details(self, job_infrastructure_configuration_details):
        """
        Sets the job_infrastructure_configuration_details of this CreateJobDetails.

        :param job_infrastructure_configuration_details: The job_infrastructure_configuration_details of this CreateJobDetails.
        :type: oci.data_science.models.JobInfrastructureConfigurationDetails
        """
        self._job_infrastructure_configuration_details = job_infrastructure_configuration_details

    @property
    def job_environment_configuration_details(self):
        """
        Gets the job_environment_configuration_details of this CreateJobDetails.

        :return: The job_environment_configuration_details of this CreateJobDetails.
        :rtype: oci.data_science.models.JobEnvironmentConfigurationDetails
        """
        return self._job_environment_configuration_details

    @job_environment_configuration_details.setter
    def job_environment_configuration_details(self, job_environment_configuration_details):
        """
        Sets the job_environment_configuration_details of this CreateJobDetails.

        :param job_environment_configuration_details: The job_environment_configuration_details of this CreateJobDetails.
        :type: oci.data_science.models.JobEnvironmentConfigurationDetails
        """
        self._job_environment_configuration_details = job_environment_configuration_details

    @property
    def job_log_configuration_details(self):
        """
        Gets the job_log_configuration_details of this CreateJobDetails.

        :return: The job_log_configuration_details of this CreateJobDetails.
        :rtype: oci.data_science.models.JobLogConfigurationDetails
        """
        return self._job_log_configuration_details

    @job_log_configuration_details.setter
    def job_log_configuration_details(self, job_log_configuration_details):
        """
        Sets the job_log_configuration_details of this CreateJobDetails.

        :param job_log_configuration_details: The job_log_configuration_details of this CreateJobDetails.
        :type: oci.data_science.models.JobLogConfigurationDetails
        """
        self._job_log_configuration_details = job_log_configuration_details

    @property
    def job_storage_mount_configuration_details_list(self):
        """
        Gets the job_storage_mount_configuration_details_list of this CreateJobDetails.
        Collection of JobStorageMountConfigurationDetails.


        :return: The job_storage_mount_configuration_details_list of this CreateJobDetails.
        :rtype: list[oci.data_science.models.StorageMountConfigurationDetails]
        """
        return self._job_storage_mount_configuration_details_list

    @job_storage_mount_configuration_details_list.setter
    def job_storage_mount_configuration_details_list(self, job_storage_mount_configuration_details_list):
        """
        Sets the job_storage_mount_configuration_details_list of this CreateJobDetails.
        Collection of JobStorageMountConfigurationDetails.


        :param job_storage_mount_configuration_details_list: The job_storage_mount_configuration_details_list of this CreateJobDetails.
        :type: list[oci.data_science.models.StorageMountConfigurationDetails]
        """
        self._job_storage_mount_configuration_details_list = job_storage_mount_configuration_details_list

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateJobDetails.
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
