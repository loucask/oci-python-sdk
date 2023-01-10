# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StopBdsInstanceDetails(object):
    """
    The request body for stopping a BDS cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StopBdsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_force_stop_jobs:
            The value to assign to the is_force_stop_jobs property of this StopBdsInstanceDetails.
        :type is_force_stop_jobs: bool

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this StopBdsInstanceDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'is_force_stop_jobs': 'bool',
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'is_force_stop_jobs': 'isForceStopJobs',
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._is_force_stop_jobs = None
        self._cluster_admin_password = None

    @property
    def is_force_stop_jobs(self):
        """
        Gets the is_force_stop_jobs of this StopBdsInstanceDetails.
        Boolean indicating whether to force stop jobs while stopping cluster. Defaults to false.


        :return: The is_force_stop_jobs of this StopBdsInstanceDetails.
        :rtype: bool
        """
        return self._is_force_stop_jobs

    @is_force_stop_jobs.setter
    def is_force_stop_jobs(self, is_force_stop_jobs):
        """
        Sets the is_force_stop_jobs of this StopBdsInstanceDetails.
        Boolean indicating whether to force stop jobs while stopping cluster. Defaults to false.


        :param is_force_stop_jobs: The is_force_stop_jobs of this StopBdsInstanceDetails.
        :type: bool
        """
        self._is_force_stop_jobs = is_force_stop_jobs

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this StopBdsInstanceDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this StopBdsInstanceDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this StopBdsInstanceDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this StopBdsInstanceDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
