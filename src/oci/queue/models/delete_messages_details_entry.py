# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteMessagesDetailsEntry(object):
    """
    Object that represents a message to delete from a queue.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteMessagesDetailsEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param receipt:
            The value to assign to the receipt property of this DeleteMessagesDetailsEntry.
        :type receipt: str

        """
        self.swagger_types = {
            'receipt': 'str'
        }

        self.attribute_map = {
            'receipt': 'receipt'
        }

        self._receipt = None

    @property
    def receipt(self):
        """
        **[Required]** Gets the receipt of this DeleteMessagesDetailsEntry.
        The receipt of the message to delete


        :return: The receipt of this DeleteMessagesDetailsEntry.
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """
        Sets the receipt of this DeleteMessagesDetailsEntry.
        The receipt of the message to delete


        :param receipt: The receipt of this DeleteMessagesDetailsEntry.
        :type: str
        """
        self._receipt = receipt

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
