# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnprocessedDataBucket(object):
    """
    Configuration details of the bucket that stores unprocessed payloads.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnprocessedDataBucket object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this UnprocessedDataBucket.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this UnprocessedDataBucket.
        :type bucket_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UnprocessedDataBucket.
        :type is_enabled: bool

        :param time_created:
            The value to assign to the time_created property of this UnprocessedDataBucket.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this UnprocessedDataBucket.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'namespace': 'str',
            'bucket_name': 'str',
            'is_enabled': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'is_enabled': 'isEnabled',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._namespace = None
        self._bucket_name = None
        self._is_enabled = None
        self._time_created = None
        self._time_updated = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this UnprocessedDataBucket.
        Object Storage namespace.


        :return: The namespace of this UnprocessedDataBucket.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UnprocessedDataBucket.
        Object Storage namespace.


        :param namespace: The namespace of this UnprocessedDataBucket.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this UnprocessedDataBucket.
        Name of the Object Storage bucket.


        :return: The bucket_name of this UnprocessedDataBucket.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this UnprocessedDataBucket.
        Name of the Object Storage bucket.


        :param bucket_name: The bucket_name of this UnprocessedDataBucket.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UnprocessedDataBucket.
        Flag that specifies if this configuration is enabled or not.


        :return: The is_enabled of this UnprocessedDataBucket.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UnprocessedDataBucket.
        Flag that specifies if this configuration is enabled or not.


        :param is_enabled: The is_enabled of this UnprocessedDataBucket.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def time_created(self):
        """
        Gets the time_created of this UnprocessedDataBucket.
        The time when this record is created. An RFC3339 formatted datetime string.


        :return: The time_created of this UnprocessedDataBucket.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UnprocessedDataBucket.
        The time when this record is created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this UnprocessedDataBucket.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this UnprocessedDataBucket.
        The latest time when this record is updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this UnprocessedDataBucket.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this UnprocessedDataBucket.
        The latest time when this record is updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this UnprocessedDataBucket.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
