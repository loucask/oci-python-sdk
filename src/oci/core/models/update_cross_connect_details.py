# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCrossConnectDetails(object):
    """
    Update a CrossConnect
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCrossConnectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCrossConnectDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateCrossConnectDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCrossConnectDetails.
        :type freeform_tags: dict(str, str)

        :param is_active:
            The value to assign to the is_active property of this UpdateCrossConnectDetails.
        :type is_active: bool

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this UpdateCrossConnectDetails.
        :type customer_reference_name: str

        :param macsec_properties:
            The value to assign to the macsec_properties property of this UpdateCrossConnectDetails.
        :type macsec_properties: oci.core.models.UpdateMacsecProperties

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'is_active': 'bool',
            'customer_reference_name': 'str',
            'macsec_properties': 'UpdateMacsecProperties'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'is_active': 'isActive',
            'customer_reference_name': 'customerReferenceName',
            'macsec_properties': 'macsecProperties'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._is_active = None
        self._customer_reference_name = None
        self._macsec_properties = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCrossConnectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCrossConnectDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCrossConnectDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCrossConnectDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateCrossConnectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateCrossConnectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCrossConnectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCrossConnectDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCrossConnectDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCrossConnectDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def is_active(self):
        """
        Gets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :return: The is_active of this UpdateCrossConnectDetails.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this UpdateCrossConnectDetails.
        Set to true to activate the cross-connect. You activate it after the physical cabling
        is complete, and you've confirmed the cross-connect's light levels are good and your side
        of the interface is up. Activation indicates to Oracle that the physical connection is ready.

        Example: `true`


        :param is_active: The is_active of this UpdateCrossConnectDetails.
        :type: bool
        """
        self._is_active = is_active

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this UpdateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection this cross-connect uses.


        :return: The customer_reference_name of this UpdateCrossConnectDetails.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this UpdateCrossConnectDetails.
        A reference name or identifier for the physical fiber connection this cross-connect uses.


        :param customer_reference_name: The customer_reference_name of this UpdateCrossConnectDetails.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    @property
    def macsec_properties(self):
        """
        Gets the macsec_properties of this UpdateCrossConnectDetails.

        :return: The macsec_properties of this UpdateCrossConnectDetails.
        :rtype: oci.core.models.UpdateMacsecProperties
        """
        return self._macsec_properties

    @macsec_properties.setter
    def macsec_properties(self, macsec_properties):
        """
        Sets the macsec_properties of this UpdateCrossConnectDetails.

        :param macsec_properties: The macsec_properties of this UpdateCrossConnectDetails.
        :type: oci.core.models.UpdateMacsecProperties
        """
        self._macsec_properties = macsec_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
