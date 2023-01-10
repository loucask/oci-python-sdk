# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomerContact(object):
    """
    Customer contact information that will be used by Oracle to provide notifications needed by database and infrastructure administrators.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomerContact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email:
            The value to assign to the email property of this CustomerContact.
        :type email: str

        """
        self.swagger_types = {
            'email': 'str'
        }

        self.attribute_map = {
            'email': 'email'
        }

        self._email = None

    @property
    def email(self):
        """
        Gets the email of this CustomerContact.
        The email address used by Oracle to send notifications regarding databases and infrastructure.


        :return: The email of this CustomerContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerContact.
        The email address used by Oracle to send notifications regarding databases and infrastructure.


        :param email: The email of this CustomerContact.
        :type: str
        """
        self._email = email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
