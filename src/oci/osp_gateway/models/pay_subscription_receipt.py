# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PaySubscriptionReceipt(object):
    """
    Subscription payment action response
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PaySubscriptionReceipt object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param header_id:
            The value to assign to the header_id property of this PaySubscriptionReceipt.
        :type header_id: str

        :param api_token:
            The value to assign to the api_token property of this PaySubscriptionReceipt.
        :type api_token: str

        :param user_token:
            The value to assign to the user_token property of this PaySubscriptionReceipt.
        :type user_token: str

        """
        self.swagger_types = {
            'header_id': 'str',
            'api_token': 'str',
            'user_token': 'str'
        }

        self.attribute_map = {
            'header_id': 'headerId',
            'api_token': 'apiToken',
            'user_token': 'userToken'
        }

        self._header_id = None
        self._api_token = None
        self._user_token = None

    @property
    def header_id(self):
        """
        **[Required]** Gets the header_id of this PaySubscriptionReceipt.
        Payment header id


        :return: The header_id of this PaySubscriptionReceipt.
        :rtype: str
        """
        return self._header_id

    @header_id.setter
    def header_id(self, header_id):
        """
        Sets the header_id of this PaySubscriptionReceipt.
        Payment header id


        :param header_id: The header_id of this PaySubscriptionReceipt.
        :type: str
        """
        self._header_id = header_id

    @property
    def api_token(self):
        """
        Gets the api_token of this PaySubscriptionReceipt.
        Parameters in a token for Payment Service


        :return: The api_token of this PaySubscriptionReceipt.
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """
        Sets the api_token of this PaySubscriptionReceipt.
        Parameters in a token for Payment Service


        :param api_token: The api_token of this PaySubscriptionReceipt.
        :type: str
        """
        self._api_token = api_token

    @property
    def user_token(self):
        """
        Gets the user_token of this PaySubscriptionReceipt.
        Session token created for Payment Service


        :return: The user_token of this PaySubscriptionReceipt.
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        """
        Sets the user_token of this PaySubscriptionReceipt.
        Session token created for Payment Service


        :param user_token: The user_token of this PaySubscriptionReceipt.
        :type: str
        """
        self._user_token = user_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
