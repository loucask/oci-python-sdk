# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteMessagesResult(object):
    """
    The response to a DeleteMessages request. It indicates the number of server and client failures as well as an array of entries for successful and failed actions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteMessagesResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param server_failures:
            The value to assign to the server_failures property of this DeleteMessagesResult.
        :type server_failures: int

        :param client_failures:
            The value to assign to the client_failures property of this DeleteMessagesResult.
        :type client_failures: int

        :param entries:
            The value to assign to the entries property of this DeleteMessagesResult.
        :type entries: list[oci.queue.models.DeleteMessagesResultEntry]

        """
        self.swagger_types = {
            'server_failures': 'int',
            'client_failures': 'int',
            'entries': 'list[DeleteMessagesResultEntry]'
        }

        self.attribute_map = {
            'server_failures': 'serverFailures',
            'client_failures': 'clientFailures',
            'entries': 'entries'
        }

        self._server_failures = None
        self._client_failures = None
        self._entries = None

    @property
    def server_failures(self):
        """
        **[Required]** Gets the server_failures of this DeleteMessagesResult.
        The number of messages that failed to be deleted from the queue because of a server failure.


        :return: The server_failures of this DeleteMessagesResult.
        :rtype: int
        """
        return self._server_failures

    @server_failures.setter
    def server_failures(self, server_failures):
        """
        Sets the server_failures of this DeleteMessagesResult.
        The number of messages that failed to be deleted from the queue because of a server failure.


        :param server_failures: The server_failures of this DeleteMessagesResult.
        :type: int
        """
        self._server_failures = server_failures

    @property
    def client_failures(self):
        """
        **[Required]** Gets the client_failures of this DeleteMessagesResult.
        The number of messages that failed to be deleted from the queue because of a client failure such as an invalid receipt.


        :return: The client_failures of this DeleteMessagesResult.
        :rtype: int
        """
        return self._client_failures

    @client_failures.setter
    def client_failures(self, client_failures):
        """
        Sets the client_failures of this DeleteMessagesResult.
        The number of messages that failed to be deleted from the queue because of a client failure such as an invalid receipt.


        :param client_failures: The client_failures of this DeleteMessagesResult.
        :type: int
        """
        self._client_failures = client_failures

    @property
    def entries(self):
        """
        **[Required]** Gets the entries of this DeleteMessagesResult.
        An array of items representing the result of each action.
        The order is guaranteed to be the same as in the `DeleteMessagesDetails` object.
        If a message was successfully deleted from the queue, the entry does not contain any fields.
        If a message failed to be deleted from the queue, the entry includes the `errorCode` and `errorMessage` fields.


        :return: The entries of this DeleteMessagesResult.
        :rtype: list[oci.queue.models.DeleteMessagesResultEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this DeleteMessagesResult.
        An array of items representing the result of each action.
        The order is guaranteed to be the same as in the `DeleteMessagesDetails` object.
        If a message was successfully deleted from the queue, the entry does not contain any fields.
        If a message failed to be deleted from the queue, the entry includes the `errorCode` and `errorMessage` fields.


        :param entries: The entries of this DeleteMessagesResult.
        :type: list[oci.queue.models.DeleteMessagesResultEntry]
        """
        self._entries = entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
