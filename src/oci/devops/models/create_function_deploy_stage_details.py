# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deploy_stage_details import CreateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFunctionDeployStageDetails(CreateDeployStageDetails):
    """
    Specifies the Function stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFunctionDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateFunctionDeployStageDetails.deploy_stage_type` attribute
        of this class is ``DEPLOY_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateFunctionDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateFunctionDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this CreateFunctionDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateFunctionDeployStageDetails.
        :type deploy_pipeline_id: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this CreateFunctionDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFunctionDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFunctionDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param function_deploy_environment_id:
            The value to assign to the function_deploy_environment_id property of this CreateFunctionDeployStageDetails.
        :type function_deploy_environment_id: str

        :param docker_image_deploy_artifact_id:
            The value to assign to the docker_image_deploy_artifact_id property of this CreateFunctionDeployStageDetails.
        :type docker_image_deploy_artifact_id: str

        :param config:
            The value to assign to the config property of this CreateFunctionDeployStageDetails.
        :type config: dict(str, str)

        :param max_memory_in_mbs:
            The value to assign to the max_memory_in_mbs property of this CreateFunctionDeployStageDetails.
        :type max_memory_in_mbs: int

        :param function_timeout_in_seconds:
            The value to assign to the function_timeout_in_seconds property of this CreateFunctionDeployStageDetails.
        :type function_timeout_in_seconds: int

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_pipeline_id': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'function_deploy_environment_id': 'str',
            'docker_image_deploy_artifact_id': 'str',
            'config': 'dict(str, str)',
            'max_memory_in_mbs': 'int',
            'function_timeout_in_seconds': 'int'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_pipeline_id': 'deployPipelineId',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'function_deploy_environment_id': 'functionDeployEnvironmentId',
            'docker_image_deploy_artifact_id': 'dockerImageDeployArtifactId',
            'config': 'config',
            'max_memory_in_mbs': 'maxMemoryInMBs',
            'function_timeout_in_seconds': 'functionTimeoutInSeconds'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_pipeline_id = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._function_deploy_environment_id = None
        self._docker_image_deploy_artifact_id = None
        self._config = None
        self._max_memory_in_mbs = None
        self._function_timeout_in_seconds = None
        self._deploy_stage_type = 'DEPLOY_FUNCTION'

    @property
    def function_deploy_environment_id(self):
        """
        **[Required]** Gets the function_deploy_environment_id of this CreateFunctionDeployStageDetails.
        Function environment OCID.


        :return: The function_deploy_environment_id of this CreateFunctionDeployStageDetails.
        :rtype: str
        """
        return self._function_deploy_environment_id

    @function_deploy_environment_id.setter
    def function_deploy_environment_id(self, function_deploy_environment_id):
        """
        Sets the function_deploy_environment_id of this CreateFunctionDeployStageDetails.
        Function environment OCID.


        :param function_deploy_environment_id: The function_deploy_environment_id of this CreateFunctionDeployStageDetails.
        :type: str
        """
        self._function_deploy_environment_id = function_deploy_environment_id

    @property
    def docker_image_deploy_artifact_id(self):
        """
        **[Required]** Gets the docker_image_deploy_artifact_id of this CreateFunctionDeployStageDetails.
        A Docker image artifact OCID.


        :return: The docker_image_deploy_artifact_id of this CreateFunctionDeployStageDetails.
        :rtype: str
        """
        return self._docker_image_deploy_artifact_id

    @docker_image_deploy_artifact_id.setter
    def docker_image_deploy_artifact_id(self, docker_image_deploy_artifact_id):
        """
        Sets the docker_image_deploy_artifact_id of this CreateFunctionDeployStageDetails.
        A Docker image artifact OCID.


        :param docker_image_deploy_artifact_id: The docker_image_deploy_artifact_id of this CreateFunctionDeployStageDetails.
        :type: str
        """
        self._docker_image_deploy_artifact_id = docker_image_deploy_artifact_id

    @property
    def config(self):
        """
        Gets the config of this CreateFunctionDeployStageDetails.
        User provided key and value pair configuration, which is assigned through constants or parameter.


        :return: The config of this CreateFunctionDeployStageDetails.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this CreateFunctionDeployStageDetails.
        User provided key and value pair configuration, which is assigned through constants or parameter.


        :param config: The config of this CreateFunctionDeployStageDetails.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def max_memory_in_mbs(self):
        """
        Gets the max_memory_in_mbs of this CreateFunctionDeployStageDetails.
        Maximum usable memory for the Function (in MB).


        :return: The max_memory_in_mbs of this CreateFunctionDeployStageDetails.
        :rtype: int
        """
        return self._max_memory_in_mbs

    @max_memory_in_mbs.setter
    def max_memory_in_mbs(self, max_memory_in_mbs):
        """
        Sets the max_memory_in_mbs of this CreateFunctionDeployStageDetails.
        Maximum usable memory for the Function (in MB).


        :param max_memory_in_mbs: The max_memory_in_mbs of this CreateFunctionDeployStageDetails.
        :type: int
        """
        self._max_memory_in_mbs = max_memory_in_mbs

    @property
    def function_timeout_in_seconds(self):
        """
        Gets the function_timeout_in_seconds of this CreateFunctionDeployStageDetails.
        Timeout for execution of the Function. Value in seconds.


        :return: The function_timeout_in_seconds of this CreateFunctionDeployStageDetails.
        :rtype: int
        """
        return self._function_timeout_in_seconds

    @function_timeout_in_seconds.setter
    def function_timeout_in_seconds(self, function_timeout_in_seconds):
        """
        Sets the function_timeout_in_seconds of this CreateFunctionDeployStageDetails.
        Timeout for execution of the Function. Value in seconds.


        :param function_timeout_in_seconds: The function_timeout_in_seconds of this CreateFunctionDeployStageDetails.
        :type: int
        """
        self._function_timeout_in_seconds = function_timeout_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
