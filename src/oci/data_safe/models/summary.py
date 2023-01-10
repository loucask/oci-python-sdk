# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Summary(object):
    """
    Summary of the audit report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Summary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Summary.
        :type name: str

        :param is_hidden:
            The value to assign to the is_hidden property of this Summary.
        :type is_hidden: bool

        :param display_order:
            The value to assign to the display_order property of this Summary.
        :type display_order: int

        :param group_by_field_name:
            The value to assign to the group_by_field_name property of this Summary.
        :type group_by_field_name: str

        :param count_of:
            The value to assign to the count_of property of this Summary.
        :type count_of: str

        :param scim_filter:
            The value to assign to the scim_filter property of this Summary.
        :type scim_filter: str

        """
        self.swagger_types = {
            'name': 'str',
            'is_hidden': 'bool',
            'display_order': 'int',
            'group_by_field_name': 'str',
            'count_of': 'str',
            'scim_filter': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'is_hidden': 'isHidden',
            'display_order': 'displayOrder',
            'group_by_field_name': 'groupByFieldName',
            'count_of': 'countOf',
            'scim_filter': 'scimFilter'
        }

        self._name = None
        self._is_hidden = None
        self._display_order = None
        self._group_by_field_name = None
        self._count_of = None
        self._scim_filter = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Summary.
        Name of the report summary.


        :return: The name of this Summary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Summary.
        Name of the report summary.


        :param name: The name of this Summary.
        :type: str
        """
        self._name = name

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this Summary.
        Indicates if the summary is hidden. Values can either be 'true' or 'false'.


        :return: The is_hidden of this Summary.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this Summary.
        Indicates if the summary is hidden. Values can either be 'true' or 'false'.


        :param is_hidden: The is_hidden of this Summary.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def display_order(self):
        """
        **[Required]** Gets the display_order of this Summary.
        Specifies the order in which the summary must be displayed.


        :return: The display_order of this Summary.
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """
        Sets the display_order of this Summary.
        Specifies the order in which the summary must be displayed.


        :param display_order: The display_order of this Summary.
        :type: int
        """
        self._display_order = display_order

    @property
    def group_by_field_name(self):
        """
        Gets the group_by_field_name of this Summary.
        A comma-delimited string that specifies the names of the fields by which the records must be aggregated to get the summary.


        :return: The group_by_field_name of this Summary.
        :rtype: str
        """
        return self._group_by_field_name

    @group_by_field_name.setter
    def group_by_field_name(self, group_by_field_name):
        """
        Sets the group_by_field_name of this Summary.
        A comma-delimited string that specifies the names of the fields by which the records must be aggregated to get the summary.


        :param group_by_field_name: The group_by_field_name of this Summary.
        :type: str
        """
        self._group_by_field_name = group_by_field_name

    @property
    def count_of(self):
        """
        Gets the count_of of this Summary.
        Name of the key or count of object.


        :return: The count_of of this Summary.
        :rtype: str
        """
        return self._count_of

    @count_of.setter
    def count_of(self, count_of):
        """
        Sets the count_of of this Summary.
        Name of the key or count of object.


        :param count_of: The count_of of this Summary.
        :type: str
        """
        self._count_of = count_of

    @property
    def scim_filter(self):
        """
        Gets the scim_filter of this Summary.
        Additional scim filters used to get the specific summary.


        :return: The scim_filter of this Summary.
        :rtype: str
        """
        return self._scim_filter

    @scim_filter.setter
    def scim_filter(self, scim_filter):
        """
        Sets the scim_filter of this Summary.
        Additional scim filters used to get the specific summary.


        :param scim_filter: The scim_filter of this Summary.
        :type: str
        """
        self._scim_filter = scim_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
