# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceUsage(object):
    """
    The resource usage information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations_insights_warehouse_id:
            The value to assign to the operations_insights_warehouse_id property of this ResourceUsage.
        :type operations_insights_warehouse_id: str

        :param id:
            The value to assign to the id property of this ResourceUsage.
        :type id: str

        :param em_instance_count:
            The value to assign to the em_instance_count property of this ResourceUsage.
        :type em_instance_count: int

        :param targets_count:
            The value to assign to the targets_count property of this ResourceUsage.
        :type targets_count: int

        :param em_instances:
            The value to assign to the em_instances property of this ResourceUsage.
        :type em_instances: list[oci.em_warehouse.models.EmInstancesDetails]

        :param schema_name:
            The value to assign to the schema_name property of this ResourceUsage.
        :type schema_name: str

        """
        self.swagger_types = {
            'operations_insights_warehouse_id': 'str',
            'id': 'str',
            'em_instance_count': 'int',
            'targets_count': 'int',
            'em_instances': 'list[EmInstancesDetails]',
            'schema_name': 'str'
        }

        self.attribute_map = {
            'operations_insights_warehouse_id': 'operationsInsightsWarehouseId',
            'id': 'id',
            'em_instance_count': 'emInstanceCount',
            'targets_count': 'targetsCount',
            'em_instances': 'emInstances',
            'schema_name': 'schemaName'
        }

        self._operations_insights_warehouse_id = None
        self._id = None
        self._em_instance_count = None
        self._targets_count = None
        self._em_instances = None
        self._schema_name = None

    @property
    def operations_insights_warehouse_id(self):
        """
        **[Required]** Gets the operations_insights_warehouse_id of this ResourceUsage.
        operations Insights Warehouse Identifier


        :return: The operations_insights_warehouse_id of this ResourceUsage.
        :rtype: str
        """
        return self._operations_insights_warehouse_id

    @operations_insights_warehouse_id.setter
    def operations_insights_warehouse_id(self, operations_insights_warehouse_id):
        """
        Sets the operations_insights_warehouse_id of this ResourceUsage.
        operations Insights Warehouse Identifier


        :param operations_insights_warehouse_id: The operations_insights_warehouse_id of this ResourceUsage.
        :type: str
        """
        self._operations_insights_warehouse_id = operations_insights_warehouse_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResourceUsage.
        Unique identifier that is immutable on creation


        :return: The id of this ResourceUsage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResourceUsage.
        Unique identifier that is immutable on creation


        :param id: The id of this ResourceUsage.
        :type: str
        """
        self._id = id

    @property
    def em_instance_count(self):
        """
        Gets the em_instance_count of this ResourceUsage.
        EmInstanceCount


        :return: The em_instance_count of this ResourceUsage.
        :rtype: int
        """
        return self._em_instance_count

    @em_instance_count.setter
    def em_instance_count(self, em_instance_count):
        """
        Sets the em_instance_count of this ResourceUsage.
        EmInstanceCount


        :param em_instance_count: The em_instance_count of this ResourceUsage.
        :type: int
        """
        self._em_instance_count = em_instance_count

    @property
    def targets_count(self):
        """
        Gets the targets_count of this ResourceUsage.
        EmInstance Target count


        :return: The targets_count of this ResourceUsage.
        :rtype: int
        """
        return self._targets_count

    @targets_count.setter
    def targets_count(self, targets_count):
        """
        Sets the targets_count of this ResourceUsage.
        EmInstance Target count


        :param targets_count: The targets_count of this ResourceUsage.
        :type: int
        """
        self._targets_count = targets_count

    @property
    def em_instances(self):
        """
        Gets the em_instances of this ResourceUsage.
        List of emInstances


        :return: The em_instances of this ResourceUsage.
        :rtype: list[oci.em_warehouse.models.EmInstancesDetails]
        """
        return self._em_instances

    @em_instances.setter
    def em_instances(self, em_instances):
        """
        Sets the em_instances of this ResourceUsage.
        List of emInstances


        :param em_instances: The em_instances of this ResourceUsage.
        :type: list[oci.em_warehouse.models.EmInstancesDetails]
        """
        self._em_instances = em_instances

    @property
    def schema_name(self):
        """
        Gets the schema_name of this ResourceUsage.
        schema name


        :return: The schema_name of this ResourceUsage.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this ResourceUsage.
        schema name


        :param schema_name: The schema_name of this ResourceUsage.
        :type: str
        """
        self._schema_name = schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
