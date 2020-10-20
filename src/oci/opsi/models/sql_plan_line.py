# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanLine(object):
    """
    SQL Plan Line type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanLine object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this SqlPlanLine.
        :type version: float

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlPlanLine.
        :type sql_identifier: str

        :param plan_hash:
            The value to assign to the plan_hash property of this SqlPlanLine.
        :type plan_hash: int

        :param time_collected:
            The value to assign to the time_collected property of this SqlPlanLine.
        :type time_collected: datetime

        :param operation:
            The value to assign to the operation property of this SqlPlanLine.
        :type operation: str

        :param remark:
            The value to assign to the remark property of this SqlPlanLine.
        :type remark: str

        :param options:
            The value to assign to the options property of this SqlPlanLine.
        :type options: str

        :param object_node:
            The value to assign to the object_node property of this SqlPlanLine.
        :type object_node: str

        :param object_owner:
            The value to assign to the object_owner property of this SqlPlanLine.
        :type object_owner: str

        :param object_name:
            The value to assign to the object_name property of this SqlPlanLine.
        :type object_name: str

        :param object_alias:
            The value to assign to the object_alias property of this SqlPlanLine.
        :type object_alias: str

        :param object_instance:
            The value to assign to the object_instance property of this SqlPlanLine.
        :type object_instance: int

        :param object_type:
            The value to assign to the object_type property of this SqlPlanLine.
        :type object_type: str

        :param optimizer:
            The value to assign to the optimizer property of this SqlPlanLine.
        :type optimizer: str

        :param search_columns:
            The value to assign to the search_columns property of this SqlPlanLine.
        :type search_columns: int

        :param identifier:
            The value to assign to the identifier property of this SqlPlanLine.
        :type identifier: int

        :param parent_identifier:
            The value to assign to the parent_identifier property of this SqlPlanLine.
        :type parent_identifier: int

        :param depth:
            The value to assign to the depth property of this SqlPlanLine.
        :type depth: int

        :param position:
            The value to assign to the position property of this SqlPlanLine.
        :type position: int

        :param cost:
            The value to assign to the cost property of this SqlPlanLine.
        :type cost: int

        :param cardinality:
            The value to assign to the cardinality property of this SqlPlanLine.
        :type cardinality: int

        :param bytes:
            The value to assign to the bytes property of this SqlPlanLine.
        :type bytes: int

        :param other:
            The value to assign to the other property of this SqlPlanLine.
        :type other: str

        :param other_tag:
            The value to assign to the other_tag property of this SqlPlanLine.
        :type other_tag: str

        :param partition_start:
            The value to assign to the partition_start property of this SqlPlanLine.
        :type partition_start: str

        :param partition_stop:
            The value to assign to the partition_stop property of this SqlPlanLine.
        :type partition_stop: str

        :param partition_identifier:
            The value to assign to the partition_identifier property of this SqlPlanLine.
        :type partition_identifier: int

        :param distribution:
            The value to assign to the distribution property of this SqlPlanLine.
        :type distribution: str

        :param cpu_cost:
            The value to assign to the cpu_cost property of this SqlPlanLine.
        :type cpu_cost: int

        :param io_cost:
            The value to assign to the io_cost property of this SqlPlanLine.
        :type io_cost: int

        :param temp_space:
            The value to assign to the temp_space property of this SqlPlanLine.
        :type temp_space: int

        :param access_predicates:
            The value to assign to the access_predicates property of this SqlPlanLine.
        :type access_predicates: str

        :param filter_predicates:
            The value to assign to the filter_predicates property of this SqlPlanLine.
        :type filter_predicates: str

        :param projection:
            The value to assign to the projection property of this SqlPlanLine.
        :type projection: str

        :param qblock_name:
            The value to assign to the qblock_name property of this SqlPlanLine.
        :type qblock_name: str

        :param elapsed_time_in_sec:
            The value to assign to the elapsed_time_in_sec property of this SqlPlanLine.
        :type elapsed_time_in_sec: float

        :param other_xml:
            The value to assign to the other_xml property of this SqlPlanLine.
        :type other_xml: str

        """
        self.swagger_types = {
            'version': 'float',
            'sql_identifier': 'str',
            'plan_hash': 'int',
            'time_collected': 'datetime',
            'operation': 'str',
            'remark': 'str',
            'options': 'str',
            'object_node': 'str',
            'object_owner': 'str',
            'object_name': 'str',
            'object_alias': 'str',
            'object_instance': 'int',
            'object_type': 'str',
            'optimizer': 'str',
            'search_columns': 'int',
            'identifier': 'int',
            'parent_identifier': 'int',
            'depth': 'int',
            'position': 'int',
            'cost': 'int',
            'cardinality': 'int',
            'bytes': 'int',
            'other': 'str',
            'other_tag': 'str',
            'partition_start': 'str',
            'partition_stop': 'str',
            'partition_identifier': 'int',
            'distribution': 'str',
            'cpu_cost': 'int',
            'io_cost': 'int',
            'temp_space': 'int',
            'access_predicates': 'str',
            'filter_predicates': 'str',
            'projection': 'str',
            'qblock_name': 'str',
            'elapsed_time_in_sec': 'float',
            'other_xml': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'sql_identifier': 'sqlIdentifier',
            'plan_hash': 'planHash',
            'time_collected': 'timeCollected',
            'operation': 'operation',
            'remark': 'remark',
            'options': 'options',
            'object_node': 'objectNode',
            'object_owner': 'objectOwner',
            'object_name': 'objectName',
            'object_alias': 'objectAlias',
            'object_instance': 'objectInstance',
            'object_type': 'objectType',
            'optimizer': 'optimizer',
            'search_columns': 'searchColumns',
            'identifier': 'identifier',
            'parent_identifier': 'parentIdentifier',
            'depth': 'depth',
            'position': 'position',
            'cost': 'cost',
            'cardinality': 'cardinality',
            'bytes': 'bytes',
            'other': 'other',
            'other_tag': 'otherTag',
            'partition_start': 'partitionStart',
            'partition_stop': 'partitionStop',
            'partition_identifier': 'partitionIdentifier',
            'distribution': 'distribution',
            'cpu_cost': 'cpuCost',
            'io_cost': 'ioCost',
            'temp_space': 'tempSpace',
            'access_predicates': 'accessPredicates',
            'filter_predicates': 'filterPredicates',
            'projection': 'projection',
            'qblock_name': 'qblockName',
            'elapsed_time_in_sec': 'elapsedTimeInSec',
            'other_xml': 'otherXML'
        }

        self._version = None
        self._sql_identifier = None
        self._plan_hash = None
        self._time_collected = None
        self._operation = None
        self._remark = None
        self._options = None
        self._object_node = None
        self._object_owner = None
        self._object_name = None
        self._object_alias = None
        self._object_instance = None
        self._object_type = None
        self._optimizer = None
        self._search_columns = None
        self._identifier = None
        self._parent_identifier = None
        self._depth = None
        self._position = None
        self._cost = None
        self._cardinality = None
        self._bytes = None
        self._other = None
        self._other_tag = None
        self._partition_start = None
        self._partition_stop = None
        self._partition_identifier = None
        self._distribution = None
        self._cpu_cost = None
        self._io_cost = None
        self._temp_space = None
        self._access_predicates = None
        self._filter_predicates = None
        self._projection = None
        self._qblock_name = None
        self._elapsed_time_in_sec = None
        self._other_xml = None

    @property
    def version(self):
        """
        Gets the version of this SqlPlanLine.
        Version
        Example: `1`


        :return: The version of this SqlPlanLine.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SqlPlanLine.
        Version
        Example: `1`


        :param version: The version of this SqlPlanLine.
        :type: float
        """
        self._version = version

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlPlanLine.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlPlanLine.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlPlanLine.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlPlanLine.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def plan_hash(self):
        """
        **[Required]** Gets the plan_hash of this SqlPlanLine.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash of this SqlPlanLine.
        :rtype: int
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this SqlPlanLine.
        Plan hash value for the SQL Execution Plan


        :param plan_hash: The plan_hash of this SqlPlanLine.
        :type: int
        """
        self._plan_hash = plan_hash

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this SqlPlanLine.
        Collection time stamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :return: The time_collected of this SqlPlanLine.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this SqlPlanLine.
        Collection time stamp
        Example: `\"2020-05-06T00:00:00.000Z\"`


        :param time_collected: The time_collected of this SqlPlanLine.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this SqlPlanLine.
        Operation
        Example: `\"SELECT STATEMENT\"`


        :return: The operation of this SqlPlanLine.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this SqlPlanLine.
        Operation
        Example: `\"SELECT STATEMENT\"`


        :param operation: The operation of this SqlPlanLine.
        :type: str
        """
        self._operation = operation

    @property
    def remark(self):
        """
        Gets the remark of this SqlPlanLine.
        Remark
        Example: `\"\"`


        :return: The remark of this SqlPlanLine.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """
        Sets the remark of this SqlPlanLine.
        Remark
        Example: `\"\"`


        :param remark: The remark of this SqlPlanLine.
        :type: str
        """
        self._remark = remark

    @property
    def options(self):
        """
        Gets the options of this SqlPlanLine.
        Options
        Example: `\"RANGE SCAN\"`


        :return: The options of this SqlPlanLine.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this SqlPlanLine.
        Options
        Example: `\"RANGE SCAN\"`


        :param options: The options of this SqlPlanLine.
        :type: str
        """
        self._options = options

    @property
    def object_node(self):
        """
        Gets the object_node of this SqlPlanLine.
        Object Node
        Example: `\"Q4000\"`


        :return: The object_node of this SqlPlanLine.
        :rtype: str
        """
        return self._object_node

    @object_node.setter
    def object_node(self, object_node):
        """
        Sets the object_node of this SqlPlanLine.
        Object Node
        Example: `\"Q4000\"`


        :param object_node: The object_node of this SqlPlanLine.
        :type: str
        """
        self._object_node = object_node

    @property
    def object_owner(self):
        """
        Gets the object_owner of this SqlPlanLine.
        Object Owner
        Example: `\"TENANT_A#SCHEMA\"`


        :return: The object_owner of this SqlPlanLine.
        :rtype: str
        """
        return self._object_owner

    @object_owner.setter
    def object_owner(self, object_owner):
        """
        Sets the object_owner of this SqlPlanLine.
        Object Owner
        Example: `\"TENANT_A#SCHEMA\"`


        :param object_owner: The object_owner of this SqlPlanLine.
        :type: str
        """
        self._object_owner = object_owner

    @property
    def object_name(self):
        """
        Gets the object_name of this SqlPlanLine.
        Object Name
        Example: `\"PLAN_LINES_PK\"`


        :return: The object_name of this SqlPlanLine.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this SqlPlanLine.
        Object Name
        Example: `\"PLAN_LINES_PK\"`


        :param object_name: The object_name of this SqlPlanLine.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_alias(self):
        """
        Gets the object_alias of this SqlPlanLine.
        Object Alias
        Example: `\"PLAN_LINES@SEL$1\"`


        :return: The object_alias of this SqlPlanLine.
        :rtype: str
        """
        return self._object_alias

    @object_alias.setter
    def object_alias(self, object_alias):
        """
        Sets the object_alias of this SqlPlanLine.
        Object Alias
        Example: `\"PLAN_LINES@SEL$1\"`


        :param object_alias: The object_alias of this SqlPlanLine.
        :type: str
        """
        self._object_alias = object_alias

    @property
    def object_instance(self):
        """
        Gets the object_instance of this SqlPlanLine.
        Object Instance
        Example: `37472`


        :return: The object_instance of this SqlPlanLine.
        :rtype: int
        """
        return self._object_instance

    @object_instance.setter
    def object_instance(self, object_instance):
        """
        Sets the object_instance of this SqlPlanLine.
        Object Instance
        Example: `37472`


        :param object_instance: The object_instance of this SqlPlanLine.
        :type: int
        """
        self._object_instance = object_instance

    @property
    def object_type(self):
        """
        Gets the object_type of this SqlPlanLine.
        Object Type
        Example: `\"INDEX (UNIQUE)\"`


        :return: The object_type of this SqlPlanLine.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SqlPlanLine.
        Object Type
        Example: `\"INDEX (UNIQUE)\"`


        :param object_type: The object_type of this SqlPlanLine.
        :type: str
        """
        self._object_type = object_type

    @property
    def optimizer(self):
        """
        Gets the optimizer of this SqlPlanLine.
        Optimizer
        Example: `\"CLUSTER\"`


        :return: The optimizer of this SqlPlanLine.
        :rtype: str
        """
        return self._optimizer

    @optimizer.setter
    def optimizer(self, optimizer):
        """
        Sets the optimizer of this SqlPlanLine.
        Optimizer
        Example: `\"CLUSTER\"`


        :param optimizer: The optimizer of this SqlPlanLine.
        :type: str
        """
        self._optimizer = optimizer

    @property
    def search_columns(self):
        """
        Gets the search_columns of this SqlPlanLine.
        Search Columns
        Example: `3`


        :return: The search_columns of this SqlPlanLine.
        :rtype: int
        """
        return self._search_columns

    @search_columns.setter
    def search_columns(self, search_columns):
        """
        Sets the search_columns of this SqlPlanLine.
        Search Columns
        Example: `3`


        :param search_columns: The search_columns of this SqlPlanLine.
        :type: int
        """
        self._search_columns = search_columns

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this SqlPlanLine.
        Identifier
        Example: `3`


        :return: The identifier of this SqlPlanLine.
        :rtype: int
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this SqlPlanLine.
        Identifier
        Example: `3`


        :param identifier: The identifier of this SqlPlanLine.
        :type: int
        """
        self._identifier = identifier

    @property
    def parent_identifier(self):
        """
        Gets the parent_identifier of this SqlPlanLine.
        Parent Identifier
        Example: `2`


        :return: The parent_identifier of this SqlPlanLine.
        :rtype: int
        """
        return self._parent_identifier

    @parent_identifier.setter
    def parent_identifier(self, parent_identifier):
        """
        Sets the parent_identifier of this SqlPlanLine.
        Parent Identifier
        Example: `2`


        :param parent_identifier: The parent_identifier of this SqlPlanLine.
        :type: int
        """
        self._parent_identifier = parent_identifier

    @property
    def depth(self):
        """
        Gets the depth of this SqlPlanLine.
        Depth
        Example: `3`


        :return: The depth of this SqlPlanLine.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth of this SqlPlanLine.
        Depth
        Example: `3`


        :param depth: The depth of this SqlPlanLine.
        :type: int
        """
        self._depth = depth

    @property
    def position(self):
        """
        Gets the position of this SqlPlanLine.
        Position
        Example: `1`


        :return: The position of this SqlPlanLine.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this SqlPlanLine.
        Position
        Example: `1`


        :param position: The position of this SqlPlanLine.
        :type: int
        """
        self._position = position

    @property
    def cost(self):
        """
        Gets the cost of this SqlPlanLine.
        Cost
        Example: `1`


        :return: The cost of this SqlPlanLine.
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this SqlPlanLine.
        Cost
        Example: `1`


        :param cost: The cost of this SqlPlanLine.
        :type: int
        """
        self._cost = cost

    @property
    def cardinality(self):
        """
        Gets the cardinality of this SqlPlanLine.
        Cardinality
        Example: `1`


        :return: The cardinality of this SqlPlanLine.
        :rtype: int
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """
        Sets the cardinality of this SqlPlanLine.
        Cardinality
        Example: `1`


        :param cardinality: The cardinality of this SqlPlanLine.
        :type: int
        """
        self._cardinality = cardinality

    @property
    def bytes(self):
        """
        Gets the bytes of this SqlPlanLine.
        Bytes
        Example: `150`


        :return: The bytes of this SqlPlanLine.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """
        Sets the bytes of this SqlPlanLine.
        Bytes
        Example: `150`


        :param bytes: The bytes of this SqlPlanLine.
        :type: int
        """
        self._bytes = bytes

    @property
    def other(self):
        """
        Gets the other of this SqlPlanLine.
        Other
        Example: ``


        :return: The other of this SqlPlanLine.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this SqlPlanLine.
        Other
        Example: ``


        :param other: The other of this SqlPlanLine.
        :type: str
        """
        self._other = other

    @property
    def other_tag(self):
        """
        Gets the other_tag of this SqlPlanLine.
        Other Tag
        Example: `\"PARALLEL_COMBINED_WITH_PARENT\"`


        :return: The other_tag of this SqlPlanLine.
        :rtype: str
        """
        return self._other_tag

    @other_tag.setter
    def other_tag(self, other_tag):
        """
        Sets the other_tag of this SqlPlanLine.
        Other Tag
        Example: `\"PARALLEL_COMBINED_WITH_PARENT\"`


        :param other_tag: The other_tag of this SqlPlanLine.
        :type: str
        """
        self._other_tag = other_tag

    @property
    def partition_start(self):
        """
        Gets the partition_start of this SqlPlanLine.
        Partition start
        Example: `1`


        :return: The partition_start of this SqlPlanLine.
        :rtype: str
        """
        return self._partition_start

    @partition_start.setter
    def partition_start(self, partition_start):
        """
        Sets the partition_start of this SqlPlanLine.
        Partition start
        Example: `1`


        :param partition_start: The partition_start of this SqlPlanLine.
        :type: str
        """
        self._partition_start = partition_start

    @property
    def partition_stop(self):
        """
        Gets the partition_stop of this SqlPlanLine.
        Partition stop
        Example: `2`


        :return: The partition_stop of this SqlPlanLine.
        :rtype: str
        """
        return self._partition_stop

    @partition_stop.setter
    def partition_stop(self, partition_stop):
        """
        Sets the partition_stop of this SqlPlanLine.
        Partition stop
        Example: `2`


        :param partition_stop: The partition_stop of this SqlPlanLine.
        :type: str
        """
        self._partition_stop = partition_stop

    @property
    def partition_identifier(self):
        """
        Gets the partition_identifier of this SqlPlanLine.
        Partition identifier
        Example: `8`


        :return: The partition_identifier of this SqlPlanLine.
        :rtype: int
        """
        return self._partition_identifier

    @partition_identifier.setter
    def partition_identifier(self, partition_identifier):
        """
        Sets the partition_identifier of this SqlPlanLine.
        Partition identifier
        Example: `8`


        :param partition_identifier: The partition_identifier of this SqlPlanLine.
        :type: int
        """
        self._partition_identifier = partition_identifier

    @property
    def distribution(self):
        """
        Gets the distribution of this SqlPlanLine.
        Distribution
        Example: `\"QC (RANDOM)\"`


        :return: The distribution of this SqlPlanLine.
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """
        Sets the distribution of this SqlPlanLine.
        Distribution
        Example: `\"QC (RANDOM)\"`


        :param distribution: The distribution of this SqlPlanLine.
        :type: str
        """
        self._distribution = distribution

    @property
    def cpu_cost(self):
        """
        Gets the cpu_cost of this SqlPlanLine.
        CPU cost
        Example: `7321`


        :return: The cpu_cost of this SqlPlanLine.
        :rtype: int
        """
        return self._cpu_cost

    @cpu_cost.setter
    def cpu_cost(self, cpu_cost):
        """
        Sets the cpu_cost of this SqlPlanLine.
        CPU cost
        Example: `7321`


        :param cpu_cost: The cpu_cost of this SqlPlanLine.
        :type: int
        """
        self._cpu_cost = cpu_cost

    @property
    def io_cost(self):
        """
        Gets the io_cost of this SqlPlanLine.
        IO cost
        Example: `1`


        :return: The io_cost of this SqlPlanLine.
        :rtype: int
        """
        return self._io_cost

    @io_cost.setter
    def io_cost(self, io_cost):
        """
        Sets the io_cost of this SqlPlanLine.
        IO cost
        Example: `1`


        :param io_cost: The io_cost of this SqlPlanLine.
        :type: int
        """
        self._io_cost = io_cost

    @property
    def temp_space(self):
        """
        Gets the temp_space of this SqlPlanLine.
        Time space
        Example: `15614000`


        :return: The temp_space of this SqlPlanLine.
        :rtype: int
        """
        return self._temp_space

    @temp_space.setter
    def temp_space(self, temp_space):
        """
        Sets the temp_space of this SqlPlanLine.
        Time space
        Example: `15614000`


        :param temp_space: The temp_space of this SqlPlanLine.
        :type: int
        """
        self._temp_space = temp_space

    @property
    def access_predicates(self):
        """
        Gets the access_predicates of this SqlPlanLine.
        Access predicates
        Example: `\"\\\"RESOURCE_ID\\\"=:1 AND \\\"QUERY_ID\\\"=:2\"`


        :return: The access_predicates of this SqlPlanLine.
        :rtype: str
        """
        return self._access_predicates

    @access_predicates.setter
    def access_predicates(self, access_predicates):
        """
        Sets the access_predicates of this SqlPlanLine.
        Access predicates
        Example: `\"\\\"RESOURCE_ID\\\"=:1 AND \\\"QUERY_ID\\\"=:2\"`


        :param access_predicates: The access_predicates of this SqlPlanLine.
        :type: str
        """
        self._access_predicates = access_predicates

    @property
    def filter_predicates(self):
        """
        Gets the filter_predicates of this SqlPlanLine.
        Filter predicates
        Example: `\"(INTERNAL_FUNCTION(\\\"J\\\".\\\"DATABASE_ROLE\\\") OR (\\\"J\\\".\\\"DATABASE_ROLE\\\" IS NULL AND SYS_CONTEXT('userenv','database_role')='PRIMARY'))\"`


        :return: The filter_predicates of this SqlPlanLine.
        :rtype: str
        """
        return self._filter_predicates

    @filter_predicates.setter
    def filter_predicates(self, filter_predicates):
        """
        Sets the filter_predicates of this SqlPlanLine.
        Filter predicates
        Example: `\"(INTERNAL_FUNCTION(\\\"J\\\".\\\"DATABASE_ROLE\\\") OR (\\\"J\\\".\\\"DATABASE_ROLE\\\" IS NULL AND SYS_CONTEXT('userenv','database_role')='PRIMARY'))\"`


        :param filter_predicates: The filter_predicates of this SqlPlanLine.
        :type: str
        """
        self._filter_predicates = filter_predicates

    @property
    def projection(self):
        """
        Gets the projection of this SqlPlanLine.
        Projection
        Example: `\"COUNT(*)[22]\"`


        :return: The projection of this SqlPlanLine.
        :rtype: str
        """
        return self._projection

    @projection.setter
    def projection(self, projection):
        """
        Sets the projection of this SqlPlanLine.
        Projection
        Example: `\"COUNT(*)[22]\"`


        :param projection: The projection of this SqlPlanLine.
        :type: str
        """
        self._projection = projection

    @property
    def qblock_name(self):
        """
        Gets the qblock_name of this SqlPlanLine.
        Qblock Name
        Example: `\"SEL$1\"`


        :return: The qblock_name of this SqlPlanLine.
        :rtype: str
        """
        return self._qblock_name

    @qblock_name.setter
    def qblock_name(self, qblock_name):
        """
        Sets the qblock_name of this SqlPlanLine.
        Qblock Name
        Example: `\"SEL$1\"`


        :param qblock_name: The qblock_name of this SqlPlanLine.
        :type: str
        """
        self._qblock_name = qblock_name

    @property
    def elapsed_time_in_sec(self):
        """
        Gets the elapsed_time_in_sec of this SqlPlanLine.
        Total elapsed time
        Example: `1.2`


        :return: The elapsed_time_in_sec of this SqlPlanLine.
        :rtype: float
        """
        return self._elapsed_time_in_sec

    @elapsed_time_in_sec.setter
    def elapsed_time_in_sec(self, elapsed_time_in_sec):
        """
        Sets the elapsed_time_in_sec of this SqlPlanLine.
        Total elapsed time
        Example: `1.2`


        :param elapsed_time_in_sec: The elapsed_time_in_sec of this SqlPlanLine.
        :type: float
        """
        self._elapsed_time_in_sec = elapsed_time_in_sec

    @property
    def other_xml(self):
        """
        Gets the other_xml of this SqlPlanLine.
        Other SQL
        Example: `\"<other_xml><info type=\\\"db_version\\\">18.0.0.0</info><info type=\\\"parse_schema\\\"><![CDATA[\\\"SYS\\\"]]></info><info type=\\\"plan_hash_full\\\">483892784</info><info type=\\\"plan_hash\\\">2709293936</info><info type=\\\"plan_hash_2\\\">483892784</info><outline_data><hint><![CDATA[IGNORE_OPTIM_EMBEDDED_HINTS]]></hint><hint><![CDATA[OPTIMIZER_FEATURES_ENABLE('18.1.0')]]></hint><hint><![CDATA[DB_VERSION('18.1.0')]]></hint><hint><![CDATA[OPT_PARAM('_b_tree_bitmap_plans' 'false')]]></hint><hint><![CDATA[OPT_PARAM('_optim_peek_user_binds' 'false')]]></hint><hint><![CDATA[OPT_PARAM('result_cache_mode' 'FORCE')]]></hint><hint><![CDATA[OPT_PARAM('_fix_control' '20648883:0 27745220:1 30001331:1 30142527:1 30539126:1')]]></hint><hint><![CDATA[OUTLINE_LEAF(@\\\"SEL$1\\\")]]></hint><hint><![CDATA[INDEX(@\\\"SEL$1\\\" \\\"USER$\\\"@\\\"SEL$1\\\" \\\"I_USER#\\\")]]></hint></outline_data></other_xml>\"`


        :return: The other_xml of this SqlPlanLine.
        :rtype: str
        """
        return self._other_xml

    @other_xml.setter
    def other_xml(self, other_xml):
        """
        Sets the other_xml of this SqlPlanLine.
        Other SQL
        Example: `\"<other_xml><info type=\\\"db_version\\\">18.0.0.0</info><info type=\\\"parse_schema\\\"><![CDATA[\\\"SYS\\\"]]></info><info type=\\\"plan_hash_full\\\">483892784</info><info type=\\\"plan_hash\\\">2709293936</info><info type=\\\"plan_hash_2\\\">483892784</info><outline_data><hint><![CDATA[IGNORE_OPTIM_EMBEDDED_HINTS]]></hint><hint><![CDATA[OPTIMIZER_FEATURES_ENABLE('18.1.0')]]></hint><hint><![CDATA[DB_VERSION('18.1.0')]]></hint><hint><![CDATA[OPT_PARAM('_b_tree_bitmap_plans' 'false')]]></hint><hint><![CDATA[OPT_PARAM('_optim_peek_user_binds' 'false')]]></hint><hint><![CDATA[OPT_PARAM('result_cache_mode' 'FORCE')]]></hint><hint><![CDATA[OPT_PARAM('_fix_control' '20648883:0 27745220:1 30001331:1 30142527:1 30539126:1')]]></hint><hint><![CDATA[OUTLINE_LEAF(@\\\"SEL$1\\\")]]></hint><hint><![CDATA[INDEX(@\\\"SEL$1\\\" \\\"USER$\\\"@\\\"SEL$1\\\" \\\"I_USER#\\\")]]></hint></outline_data></other_xml>\"`


        :param other_xml: The other_xml of this SqlPlanLine.
        :type: str
        """
        self._other_xml = other_xml

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
