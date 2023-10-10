# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaptureFilter(object):
    """
    A capture filter contains a set of *:func:`capture_filter_rule_details`* governing what traffic a *:class:`Vtap`* mirrors.
    The capture filter is created with no rules defined, and it must have at least one rule for the VTAP to start mirroring traffic.
    """

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the filter_type property of a CaptureFilter.
    #: This constant has a value of "VTAP"
    FILTER_TYPE_VTAP = "VTAP"

    #: A constant which can be used with the filter_type property of a CaptureFilter.
    #: This constant has a value of "FLOWLOG"
    FILTER_TYPE_FLOWLOG = "FLOWLOG"

    def __init__(self, **kwargs):
        """
        Initializes a new CaptureFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CaptureFilter.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CaptureFilter.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CaptureFilter.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CaptureFilter.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this CaptureFilter.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CaptureFilter.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param filter_type:
            The value to assign to the filter_type property of this CaptureFilter.
            Allowed values for this property are: "VTAP", "FLOWLOG"
        :type filter_type: str

        :param time_created:
            The value to assign to the time_created property of this CaptureFilter.
        :type time_created: datetime

        :param vtap_capture_filter_rules:
            The value to assign to the vtap_capture_filter_rules property of this CaptureFilter.
        :type vtap_capture_filter_rules: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]

        :param flow_log_capture_filter_rules:
            The value to assign to the flow_log_capture_filter_rules property of this CaptureFilter.
        :type flow_log_capture_filter_rules: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'filter_type': 'str',
            'time_created': 'datetime',
            'vtap_capture_filter_rules': 'list[VtapCaptureFilterRuleDetails]',
            'flow_log_capture_filter_rules': 'list[FlowLogCaptureFilterRuleDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'filter_type': 'filterType',
            'time_created': 'timeCreated',
            'vtap_capture_filter_rules': 'vtapCaptureFilterRules',
            'flow_log_capture_filter_rules': 'flowLogCaptureFilterRules'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._filter_type = None
        self._time_created = None
        self._vtap_capture_filter_rules = None
        self._flow_log_capture_filter_rules = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CaptureFilter.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CaptureFilter.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CaptureFilter.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CaptureFilter.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CaptureFilter.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CaptureFilter.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CaptureFilter.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CaptureFilter.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CaptureFilter.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CaptureFilter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CaptureFilter.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CaptureFilter.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CaptureFilter.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CaptureFilter.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CaptureFilter.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CaptureFilter.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CaptureFilter.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this CaptureFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CaptureFilter.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this CaptureFilter.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CaptureFilter.
        The capture filter's current administrative state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this CaptureFilter.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CaptureFilter.
        The capture filter's current administrative state.


        :param lifecycle_state: The lifecycle_state of this CaptureFilter.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                f"Invalid value for `lifecycle_state`, must be None or one of {allowed_values}"
            )
        self._lifecycle_state = lifecycle_state

    @property
    def filter_type(self):
        """
        Gets the filter_type of this CaptureFilter.
        Indicates which service will use this capture filter

        Allowed values for this property are: "VTAP", "FLOWLOG"


        :return: The filter_type of this CaptureFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this CaptureFilter.
        Indicates which service will use this capture filter


        :param filter_type: The filter_type of this CaptureFilter.
        :type: str
        """
        allowed_values = ["VTAP", "FLOWLOG"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            raise ValueError(
                f"Invalid value for `filter_type`, must be None or one of {allowed_values}"
            )
        self._filter_type = filter_type

    @property
    def time_created(self):
        """
        Gets the time_created of this CaptureFilter.
        The date and time the capture filter was created, in the format defined by `RFC3339`__.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CaptureFilter.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CaptureFilter.
        The date and time the capture filter was created, in the format defined by `RFC3339`__.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CaptureFilter.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vtap_capture_filter_rules(self):
        """
        Gets the vtap_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic a VTAP mirrors.


        :return: The vtap_capture_filter_rules of this CaptureFilter.
        :rtype: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]
        """
        return self._vtap_capture_filter_rules

    @vtap_capture_filter_rules.setter
    def vtap_capture_filter_rules(self, vtap_capture_filter_rules):
        """
        Sets the vtap_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic a VTAP mirrors.


        :param vtap_capture_filter_rules: The vtap_capture_filter_rules of this CaptureFilter.
        :type: list[oci.vn_monitoring.models.VtapCaptureFilterRuleDetails]
        """
        self._vtap_capture_filter_rules = vtap_capture_filter_rules

    @property
    def flow_log_capture_filter_rules(self):
        """
        Gets the flow_log_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.


        :return: The flow_log_capture_filter_rules of this CaptureFilter.
        :rtype: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]
        """
        return self._flow_log_capture_filter_rules

    @flow_log_capture_filter_rules.setter
    def flow_log_capture_filter_rules(self, flow_log_capture_filter_rules):
        """
        Sets the flow_log_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic the Flow Log collects when creating a flow log capture filter.


        :param flow_log_capture_filter_rules: The flow_log_capture_filter_rules of this CaptureFilter.
        :type: list[oci.vn_monitoring.models.FlowLogCaptureFilterRuleDetails]
        """
        self._flow_log_capture_filter_rules = flow_log_capture_filter_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
