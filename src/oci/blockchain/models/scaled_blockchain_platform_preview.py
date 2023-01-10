# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScaledBlockchainPlatformPreview(object):
    """
    Blockchain Platform Instance Description Preview after Scaling.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScaledBlockchainPlatformPreview object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScaledBlockchainPlatformPreview.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScaledBlockchainPlatformPreview.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScaledBlockchainPlatformPreview.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this ScaledBlockchainPlatformPreview.
        :type description: str

        :param compute_shape:
            The value to assign to the compute_shape property of this ScaledBlockchainPlatformPreview.
        :type compute_shape: str

        :param storage_size_in_tbs:
            The value to assign to the storage_size_in_tbs property of this ScaledBlockchainPlatformPreview.
        :type storage_size_in_tbs: float

        :param storage_size_in_tbs_post_scaling:
            The value to assign to the storage_size_in_tbs_post_scaling property of this ScaledBlockchainPlatformPreview.
        :type storage_size_in_tbs_post_scaling: float

        :param component_details:
            The value to assign to the component_details property of this ScaledBlockchainPlatformPreview.
        :type component_details: oci.blockchain.models.BlockchainPlatformComponentDetails

        :param replicas:
            The value to assign to the replicas property of this ScaledBlockchainPlatformPreview.
        :type replicas: oci.blockchain.models.ReplicaDetails

        :param component_details_post_scaling:
            The value to assign to the component_details_post_scaling property of this ScaledBlockchainPlatformPreview.
        :type component_details_post_scaling: oci.blockchain.models.BlockchainPlatformComponentDetails

        :param replicas_post_scaling:
            The value to assign to the replicas_post_scaling property of this ScaledBlockchainPlatformPreview.
        :type replicas_post_scaling: oci.blockchain.models.ReplicaDetails

        :param host_ocpu_utilization_info:
            The value to assign to the host_ocpu_utilization_info property of this ScaledBlockchainPlatformPreview.
        :type host_ocpu_utilization_info: list[oci.blockchain.models.OcpuUtilizationInfo]

        :param host_ocpu_utilization_info_post_scaling:
            The value to assign to the host_ocpu_utilization_info_post_scaling property of this ScaledBlockchainPlatformPreview.
        :type host_ocpu_utilization_info_post_scaling: list[oci.blockchain.models.OcpuUtilizationInfo]

        :param new_vm_count:
            The value to assign to the new_vm_count property of this ScaledBlockchainPlatformPreview.
        :type new_vm_count: int

        :param metering_preview:
            The value to assign to the metering_preview property of this ScaledBlockchainPlatformPreview.
        :type metering_preview: oci.blockchain.models.ScaledPlatformMeteringPreview

        :param scale_payload:
            The value to assign to the scale_payload property of this ScaledBlockchainPlatformPreview.
        :type scale_payload: oci.blockchain.models.ScaleBlockchainPlatformDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'compute_shape': 'str',
            'storage_size_in_tbs': 'float',
            'storage_size_in_tbs_post_scaling': 'float',
            'component_details': 'BlockchainPlatformComponentDetails',
            'replicas': 'ReplicaDetails',
            'component_details_post_scaling': 'BlockchainPlatformComponentDetails',
            'replicas_post_scaling': 'ReplicaDetails',
            'host_ocpu_utilization_info': 'list[OcpuUtilizationInfo]',
            'host_ocpu_utilization_info_post_scaling': 'list[OcpuUtilizationInfo]',
            'new_vm_count': 'int',
            'metering_preview': 'ScaledPlatformMeteringPreview',
            'scale_payload': 'ScaleBlockchainPlatformDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'compute_shape': 'computeShape',
            'storage_size_in_tbs': 'storageSizeInTBs',
            'storage_size_in_tbs_post_scaling': 'storageSizeInTBsPostScaling',
            'component_details': 'componentDetails',
            'replicas': 'replicas',
            'component_details_post_scaling': 'componentDetailsPostScaling',
            'replicas_post_scaling': 'replicasPostScaling',
            'host_ocpu_utilization_info': 'hostOcpuUtilizationInfo',
            'host_ocpu_utilization_info_post_scaling': 'hostOcpuUtilizationInfoPostScaling',
            'new_vm_count': 'newVmCount',
            'metering_preview': 'meteringPreview',
            'scale_payload': 'scalePayload'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._compute_shape = None
        self._storage_size_in_tbs = None
        self._storage_size_in_tbs_post_scaling = None
        self._component_details = None
        self._replicas = None
        self._component_details_post_scaling = None
        self._replicas_post_scaling = None
        self._host_ocpu_utilization_info = None
        self._host_ocpu_utilization_info_post_scaling = None
        self._new_vm_count = None
        self._metering_preview = None
        self._scale_payload = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScaledBlockchainPlatformPreview.
        unique identifier that is immutable on creation


        :return: The id of this ScaledBlockchainPlatformPreview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScaledBlockchainPlatformPreview.
        unique identifier that is immutable on creation


        :param id: The id of this ScaledBlockchainPlatformPreview.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScaledBlockchainPlatformPreview.
        Platform Instance Display name, can be renamed


        :return: The display_name of this ScaledBlockchainPlatformPreview.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScaledBlockchainPlatformPreview.
        Platform Instance Display name, can be renamed


        :param display_name: The display_name of this ScaledBlockchainPlatformPreview.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScaledBlockchainPlatformPreview.
        Compartment Identifier


        :return: The compartment_id of this ScaledBlockchainPlatformPreview.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScaledBlockchainPlatformPreview.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ScaledBlockchainPlatformPreview.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this ScaledBlockchainPlatformPreview.
        Platform Instance Description


        :return: The description of this ScaledBlockchainPlatformPreview.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScaledBlockchainPlatformPreview.
        Platform Instance Description


        :param description: The description of this ScaledBlockchainPlatformPreview.
        :type: str
        """
        self._description = description

    @property
    def compute_shape(self):
        """
        **[Required]** Gets the compute_shape of this ScaledBlockchainPlatformPreview.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM


        :return: The compute_shape of this ScaledBlockchainPlatformPreview.
        :rtype: str
        """
        return self._compute_shape

    @compute_shape.setter
    def compute_shape(self, compute_shape):
        """
        Sets the compute_shape of this ScaledBlockchainPlatformPreview.
        Compute shape - STANDARD or ENTERPRISE_SMALL or ENTERPRISE_MEDIUM or ENTERPRISE_LARGE or ENTERPRISE_EXTRA_LARGE or ENTERPRISE_CUSTOM


        :param compute_shape: The compute_shape of this ScaledBlockchainPlatformPreview.
        :type: str
        """
        self._compute_shape = compute_shape

    @property
    def storage_size_in_tbs(self):
        """
        Gets the storage_size_in_tbs of this ScaledBlockchainPlatformPreview.
        Storage size in TBs


        :return: The storage_size_in_tbs of this ScaledBlockchainPlatformPreview.
        :rtype: float
        """
        return self._storage_size_in_tbs

    @storage_size_in_tbs.setter
    def storage_size_in_tbs(self, storage_size_in_tbs):
        """
        Sets the storage_size_in_tbs of this ScaledBlockchainPlatformPreview.
        Storage size in TBs


        :param storage_size_in_tbs: The storage_size_in_tbs of this ScaledBlockchainPlatformPreview.
        :type: float
        """
        self._storage_size_in_tbs = storage_size_in_tbs

    @property
    def storage_size_in_tbs_post_scaling(self):
        """
        Gets the storage_size_in_tbs_post_scaling of this ScaledBlockchainPlatformPreview.
        Storage size in TBs post scaling


        :return: The storage_size_in_tbs_post_scaling of this ScaledBlockchainPlatformPreview.
        :rtype: float
        """
        return self._storage_size_in_tbs_post_scaling

    @storage_size_in_tbs_post_scaling.setter
    def storage_size_in_tbs_post_scaling(self, storage_size_in_tbs_post_scaling):
        """
        Sets the storage_size_in_tbs_post_scaling of this ScaledBlockchainPlatformPreview.
        Storage size in TBs post scaling


        :param storage_size_in_tbs_post_scaling: The storage_size_in_tbs_post_scaling of this ScaledBlockchainPlatformPreview.
        :type: float
        """
        self._storage_size_in_tbs_post_scaling = storage_size_in_tbs_post_scaling

    @property
    def component_details(self):
        """
        Gets the component_details of this ScaledBlockchainPlatformPreview.

        :return: The component_details of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        return self._component_details

    @component_details.setter
    def component_details(self, component_details):
        """
        Sets the component_details of this ScaledBlockchainPlatformPreview.

        :param component_details: The component_details of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        self._component_details = component_details

    @property
    def replicas(self):
        """
        Gets the replicas of this ScaledBlockchainPlatformPreview.

        :return: The replicas of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this ScaledBlockchainPlatformPreview.

        :param replicas: The replicas of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._replicas = replicas

    @property
    def component_details_post_scaling(self):
        """
        Gets the component_details_post_scaling of this ScaledBlockchainPlatformPreview.

        :return: The component_details_post_scaling of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        return self._component_details_post_scaling

    @component_details_post_scaling.setter
    def component_details_post_scaling(self, component_details_post_scaling):
        """
        Sets the component_details_post_scaling of this ScaledBlockchainPlatformPreview.

        :param component_details_post_scaling: The component_details_post_scaling of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.BlockchainPlatformComponentDetails
        """
        self._component_details_post_scaling = component_details_post_scaling

    @property
    def replicas_post_scaling(self):
        """
        Gets the replicas_post_scaling of this ScaledBlockchainPlatformPreview.

        :return: The replicas_post_scaling of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._replicas_post_scaling

    @replicas_post_scaling.setter
    def replicas_post_scaling(self, replicas_post_scaling):
        """
        Sets the replicas_post_scaling of this ScaledBlockchainPlatformPreview.

        :param replicas_post_scaling: The replicas_post_scaling of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._replicas_post_scaling = replicas_post_scaling

    @property
    def host_ocpu_utilization_info(self):
        """
        Gets the host_ocpu_utilization_info of this ScaledBlockchainPlatformPreview.
        List of OcpuUtilization for all hosts


        :return: The host_ocpu_utilization_info of this ScaledBlockchainPlatformPreview.
        :rtype: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        return self._host_ocpu_utilization_info

    @host_ocpu_utilization_info.setter
    def host_ocpu_utilization_info(self, host_ocpu_utilization_info):
        """
        Sets the host_ocpu_utilization_info of this ScaledBlockchainPlatformPreview.
        List of OcpuUtilization for all hosts


        :param host_ocpu_utilization_info: The host_ocpu_utilization_info of this ScaledBlockchainPlatformPreview.
        :type: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        self._host_ocpu_utilization_info = host_ocpu_utilization_info

    @property
    def host_ocpu_utilization_info_post_scaling(self):
        """
        Gets the host_ocpu_utilization_info_post_scaling of this ScaledBlockchainPlatformPreview.
        List of OcpuUtilization for all hosts after scaling


        :return: The host_ocpu_utilization_info_post_scaling of this ScaledBlockchainPlatformPreview.
        :rtype: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        return self._host_ocpu_utilization_info_post_scaling

    @host_ocpu_utilization_info_post_scaling.setter
    def host_ocpu_utilization_info_post_scaling(self, host_ocpu_utilization_info_post_scaling):
        """
        Sets the host_ocpu_utilization_info_post_scaling of this ScaledBlockchainPlatformPreview.
        List of OcpuUtilization for all hosts after scaling


        :param host_ocpu_utilization_info_post_scaling: The host_ocpu_utilization_info_post_scaling of this ScaledBlockchainPlatformPreview.
        :type: list[oci.blockchain.models.OcpuUtilizationInfo]
        """
        self._host_ocpu_utilization_info_post_scaling = host_ocpu_utilization_info_post_scaling

    @property
    def new_vm_count(self):
        """
        Gets the new_vm_count of this ScaledBlockchainPlatformPreview.
        Number of new VMs that would be created


        :return: The new_vm_count of this ScaledBlockchainPlatformPreview.
        :rtype: int
        """
        return self._new_vm_count

    @new_vm_count.setter
    def new_vm_count(self, new_vm_count):
        """
        Sets the new_vm_count of this ScaledBlockchainPlatformPreview.
        Number of new VMs that would be created


        :param new_vm_count: The new_vm_count of this ScaledBlockchainPlatformPreview.
        :type: int
        """
        self._new_vm_count = new_vm_count

    @property
    def metering_preview(self):
        """
        Gets the metering_preview of this ScaledBlockchainPlatformPreview.

        :return: The metering_preview of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.ScaledPlatformMeteringPreview
        """
        return self._metering_preview

    @metering_preview.setter
    def metering_preview(self, metering_preview):
        """
        Sets the metering_preview of this ScaledBlockchainPlatformPreview.

        :param metering_preview: The metering_preview of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.ScaledPlatformMeteringPreview
        """
        self._metering_preview = metering_preview

    @property
    def scale_payload(self):
        """
        Gets the scale_payload of this ScaledBlockchainPlatformPreview.

        :return: The scale_payload of this ScaledBlockchainPlatformPreview.
        :rtype: oci.blockchain.models.ScaleBlockchainPlatformDetails
        """
        return self._scale_payload

    @scale_payload.setter
    def scale_payload(self, scale_payload):
        """
        Sets the scale_payload of this ScaledBlockchainPlatformPreview.

        :param scale_payload: The scale_payload of this ScaledBlockchainPlatformPreview.
        :type: oci.blockchain.models.ScaleBlockchainPlatformDetails
        """
        self._scale_payload = scale_payload

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
