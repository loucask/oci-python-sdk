# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceProfile(object):
    """
    Resource profile details
    """

    #: A constant which can be used with the risk_level property of a ResourceProfile.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a ResourceProfile.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a ResourceProfile.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a ResourceProfile.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a ResourceProfile.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sightings_count:
            The value to assign to the sightings_count property of this ResourceProfile.
        :type sightings_count: int

        :param id:
            The value to assign to the id property of this ResourceProfile.
        :type id: str

        :param resource_id:
            The value to assign to the resource_id property of this ResourceProfile.
        :type resource_id: str

        :param display_name:
            The value to assign to the display_name property of this ResourceProfile.
        :type display_name: str

        :param type:
            The value to assign to the type property of this ResourceProfile.
        :type type: str

        :param problem_ids:
            The value to assign to the problem_ids property of this ResourceProfile.
        :type problem_ids: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this ResourceProfile.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this ResourceProfile.
        :type target_id: str

        :param risk_score:
            The value to assign to the risk_score property of this ResourceProfile.
        :type risk_score: float

        :param risk_level:
            The value to assign to the risk_level property of this ResourceProfile.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param peak_risk_score:
            The value to assign to the peak_risk_score property of this ResourceProfile.
        :type peak_risk_score: float

        :param time_peak_score:
            The value to assign to the time_peak_score property of this ResourceProfile.
        :type time_peak_score: datetime

        :param time_first_detected:
            The value to assign to the time_first_detected property of this ResourceProfile.
        :type time_first_detected: datetime

        :param time_last_detected:
            The value to assign to the time_last_detected property of this ResourceProfile.
        :type time_last_detected: datetime

        :param tactics:
            The value to assign to the tactics property of this ResourceProfile.
        :type tactics: list[oci.cloud_guard.models.TacticSummary]

        """
        self.swagger_types = {
            'sightings_count': 'int',
            'id': 'str',
            'resource_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'problem_ids': 'list[str]',
            'compartment_id': 'str',
            'target_id': 'str',
            'risk_score': 'float',
            'risk_level': 'str',
            'peak_risk_score': 'float',
            'time_peak_score': 'datetime',
            'time_first_detected': 'datetime',
            'time_last_detected': 'datetime',
            'tactics': 'list[TacticSummary]'
        }

        self.attribute_map = {
            'sightings_count': 'sightingsCount',
            'id': 'id',
            'resource_id': 'resourceId',
            'display_name': 'displayName',
            'type': 'type',
            'problem_ids': 'problemIds',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'risk_score': 'riskScore',
            'risk_level': 'riskLevel',
            'peak_risk_score': 'peakRiskScore',
            'time_peak_score': 'timePeakScore',
            'time_first_detected': 'timeFirstDetected',
            'time_last_detected': 'timeLastDetected',
            'tactics': 'tactics'
        }

        self._sightings_count = None
        self._id = None
        self._resource_id = None
        self._display_name = None
        self._type = None
        self._problem_ids = None
        self._compartment_id = None
        self._target_id = None
        self._risk_score = None
        self._risk_level = None
        self._peak_risk_score = None
        self._time_peak_score = None
        self._time_first_detected = None
        self._time_last_detected = None
        self._tactics = None

    @property
    def sightings_count(self):
        """
        Gets the sightings_count of this ResourceProfile.
        Number of sightings associated with this resource profile


        :return: The sightings_count of this ResourceProfile.
        :rtype: int
        """
        return self._sightings_count

    @sightings_count.setter
    def sightings_count(self, sightings_count):
        """
        Sets the sightings_count of this ResourceProfile.
        Number of sightings associated with this resource profile


        :param sightings_count: The sightings_count of this ResourceProfile.
        :type: int
        """
        self._sightings_count = sightings_count

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResourceProfile.
        Unique identifier for resource profile


        :return: The id of this ResourceProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResourceProfile.
        Unique identifier for resource profile


        :param id: The id of this ResourceProfile.
        :type: str
        """
        self._id = id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this ResourceProfile.
        Unique identifier for resource profile


        :return: The resource_id of this ResourceProfile.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ResourceProfile.
        Unique identifier for resource profile


        :param resource_id: The resource_id of this ResourceProfile.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ResourceProfile.
        Resource name for resource profile


        :return: The display_name of this ResourceProfile.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResourceProfile.
        Resource name for resource profile


        :param display_name: The display_name of this ResourceProfile.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResourceProfile.
        Resource type for resource profile


        :return: The type of this ResourceProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceProfile.
        Resource type for resource profile


        :param type: The type of this ResourceProfile.
        :type: str
        """
        self._type = type

    @property
    def problem_ids(self):
        """
        Gets the problem_ids of this ResourceProfile.
        List of Problems associated with the resource profile.


        :return: The problem_ids of this ResourceProfile.
        :rtype: list[str]
        """
        return self._problem_ids

    @problem_ids.setter
    def problem_ids(self, problem_ids):
        """
        Sets the problem_ids of this ResourceProfile.
        List of Problems associated with the resource profile.


        :param problem_ids: The problem_ids of this ResourceProfile.
        :type: list[str]
        """
        self._problem_ids = problem_ids

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ResourceProfile.
        Compartment Id for resource profile


        :return: The compartment_id of this ResourceProfile.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ResourceProfile.
        Compartment Id for resource profile


        :param compartment_id: The compartment_id of this ResourceProfile.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this ResourceProfile.
        Target Id for resource profile


        :return: The target_id of this ResourceProfile.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this ResourceProfile.
        Target Id for resource profile


        :param target_id: The target_id of this ResourceProfile.
        :type: str
        """
        self._target_id = target_id

    @property
    def risk_score(self):
        """
        **[Required]** Gets the risk_score of this ResourceProfile.
        Risk Score for the resource profile


        :return: The risk_score of this ResourceProfile.
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """
        Sets the risk_score of this ResourceProfile.
        Risk Score for the resource profile


        :param risk_score: The risk_score of this ResourceProfile.
        :type: float
        """
        self._risk_score = risk_score

    @property
    def risk_level(self):
        """
        Gets the risk_level of this ResourceProfile.
        Risk Level associated with resource profile

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this ResourceProfile.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this ResourceProfile.
        Risk Level associated with resource profile


        :param risk_level: The risk_level of this ResourceProfile.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def peak_risk_score(self):
        """
        Gets the peak_risk_score of this ResourceProfile.
        Peak Risk Score for the resource profile


        :return: The peak_risk_score of this ResourceProfile.
        :rtype: float
        """
        return self._peak_risk_score

    @peak_risk_score.setter
    def peak_risk_score(self, peak_risk_score):
        """
        Sets the peak_risk_score of this ResourceProfile.
        Peak Risk Score for the resource profile


        :param peak_risk_score: The peak_risk_score of this ResourceProfile.
        :type: float
        """
        self._peak_risk_score = peak_risk_score

    @property
    def time_peak_score(self):
        """
        Gets the time_peak_score of this ResourceProfile.
        The date and time for peak risk score. Format defined by RFC3339.


        :return: The time_peak_score of this ResourceProfile.
        :rtype: datetime
        """
        return self._time_peak_score

    @time_peak_score.setter
    def time_peak_score(self, time_peak_score):
        """
        Sets the time_peak_score of this ResourceProfile.
        The date and time for peak risk score. Format defined by RFC3339.


        :param time_peak_score: The time_peak_score of this ResourceProfile.
        :type: datetime
        """
        self._time_peak_score = time_peak_score

    @property
    def time_first_detected(self):
        """
        **[Required]** Gets the time_first_detected of this ResourceProfile.
        The date and time the resource profile was first detected. Format defined by RFC3339.


        :return: The time_first_detected of this ResourceProfile.
        :rtype: datetime
        """
        return self._time_first_detected

    @time_first_detected.setter
    def time_first_detected(self, time_first_detected):
        """
        Sets the time_first_detected of this ResourceProfile.
        The date and time the resource profile was first detected. Format defined by RFC3339.


        :param time_first_detected: The time_first_detected of this ResourceProfile.
        :type: datetime
        """
        self._time_first_detected = time_first_detected

    @property
    def time_last_detected(self):
        """
        **[Required]** Gets the time_last_detected of this ResourceProfile.
        The date and time the resource profile was last detected. Format defined by RFC3339.


        :return: The time_last_detected of this ResourceProfile.
        :rtype: datetime
        """
        return self._time_last_detected

    @time_last_detected.setter
    def time_last_detected(self, time_last_detected):
        """
        Sets the time_last_detected of this ResourceProfile.
        The date and time the resource profile was last detected. Format defined by RFC3339.


        :param time_last_detected: The time_last_detected of this ResourceProfile.
        :type: datetime
        """
        self._time_last_detected = time_last_detected

    @property
    def tactics(self):
        """
        **[Required]** Gets the tactics of this ResourceProfile.
        List of tactic summary associated with the resource profile.


        :return: The tactics of this ResourceProfile.
        :rtype: list[oci.cloud_guard.models.TacticSummary]
        """
        return self._tactics

    @tactics.setter
    def tactics(self, tactics):
        """
        Sets the tactics of this ResourceProfile.
        List of tactic summary associated with the resource profile.


        :param tactics: The tactics of this ResourceProfile.
        :type: list[oci.cloud_guard.models.TacticSummary]
        """
        self._tactics = tactics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
