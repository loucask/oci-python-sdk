# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentAggregation(object):
    """
    A count of Management Agents sharing the values for specified dimensions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions:
            The value to assign to the dimensions property of this ManagementAgentAggregation.
        :type dimensions: oci.management_agent.models.ManagementAgentAggregationDimensions

        :param count:
            The value to assign to the count property of this ManagementAgentAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions': 'ManagementAgentAggregationDimensions',
            'count': 'int'
        }

        self.attribute_map = {
            'dimensions': 'dimensions',
            'count': 'count'
        }

        self._dimensions = None
        self._count = None

    @property
    def dimensions(self):
        """
        Gets the dimensions of this ManagementAgentAggregation.

        :return: The dimensions of this ManagementAgentAggregation.
        :rtype: oci.management_agent.models.ManagementAgentAggregationDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this ManagementAgentAggregation.

        :param dimensions: The dimensions of this ManagementAgentAggregation.
        :type: oci.management_agent.models.ManagementAgentAggregationDimensions
        """
        self._dimensions = dimensions

    @property
    def count(self):
        """
        Gets the count of this ManagementAgentAggregation.
        The number of Management Agents in this group


        :return: The count of this ManagementAgentAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ManagementAgentAggregation.
        The number of Management Agents in this group


        :param count: The count of this ManagementAgentAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
