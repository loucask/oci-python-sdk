# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanExecutionOptions(object):
    """
    The options for a plan execution.
    """

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecutionOptions.
    #: This constant has a value of "SWITCHOVER"
    PLAN_EXECUTION_TYPE_SWITCHOVER = "SWITCHOVER"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecutionOptions.
    #: This constant has a value of "SWITCHOVER_PRECHECK"
    PLAN_EXECUTION_TYPE_SWITCHOVER_PRECHECK = "SWITCHOVER_PRECHECK"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecutionOptions.
    #: This constant has a value of "FAILOVER"
    PLAN_EXECUTION_TYPE_FAILOVER = "FAILOVER"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecutionOptions.
    #: This constant has a value of "FAILOVER_PRECHECK"
    PLAN_EXECUTION_TYPE_FAILOVER_PRECHECK = "FAILOVER_PRECHECK"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanExecutionOptions object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.disaster_recovery.models.SwitchoverExecutionOptions`
        * :class:`~oci.disaster_recovery.models.FailoverPrecheckExecutionOptions`
        * :class:`~oci.disaster_recovery.models.SwitchoverPrecheckExecutionOptions`
        * :class:`~oci.disaster_recovery.models.FailoverExecutionOptions`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_execution_type:
            The value to assign to the plan_execution_type property of this DrPlanExecutionOptions.
            Allowed values for this property are: "SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_execution_type: str

        """
        self.swagger_types = {
            'plan_execution_type': 'str'
        }

        self.attribute_map = {
            'plan_execution_type': 'planExecutionType'
        }

        self._plan_execution_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['planExecutionType']

        if type == 'SWITCHOVER':
            return 'SwitchoverExecutionOptions'

        if type == 'FAILOVER_PRECHECK':
            return 'FailoverPrecheckExecutionOptions'

        if type == 'SWITCHOVER_PRECHECK':
            return 'SwitchoverPrecheckExecutionOptions'

        if type == 'FAILOVER':
            return 'FailoverExecutionOptions'
        else:
            return 'DrPlanExecutionOptions'

    @property
    def plan_execution_type(self):
        """
        **[Required]** Gets the plan_execution_type of this DrPlanExecutionOptions.
        The type of the plan execution.

        Allowed values for this property are: "SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_execution_type of this DrPlanExecutionOptions.
        :rtype: str
        """
        return self._plan_execution_type

    @plan_execution_type.setter
    def plan_execution_type(self, plan_execution_type):
        """
        Sets the plan_execution_type of this DrPlanExecutionOptions.
        The type of the plan execution.


        :param plan_execution_type: The plan_execution_type of this DrPlanExecutionOptions.
        :type: str
        """
        allowed_values = ["SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK"]
        if not value_allowed_none_or_none_sentinel(plan_execution_type, allowed_values):
            plan_execution_type = 'UNKNOWN_ENUM_VALUE'
        self._plan_execution_type = plan_execution_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
