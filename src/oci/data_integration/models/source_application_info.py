# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceApplicationInfo(object):
    """
    The information about the application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceApplicationInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param workspace_id:
            The value to assign to the workspace_id property of this SourceApplicationInfo.
        :type workspace_id: str

        :param application_key:
            The value to assign to the application_key property of this SourceApplicationInfo.
        :type application_key: str

        :param application_version:
            The value to assign to the application_version property of this SourceApplicationInfo.
        :type application_version: str

        :param last_patch_key:
            The value to assign to the last_patch_key property of this SourceApplicationInfo.
        :type last_patch_key: str

        """
        self.swagger_types = {
            'workspace_id': 'str',
            'application_key': 'str',
            'application_version': 'str',
            'last_patch_key': 'str'
        }

        self.attribute_map = {
            'workspace_id': 'workspaceId',
            'application_key': 'applicationKey',
            'application_version': 'applicationVersion',
            'last_patch_key': 'lastPatchKey'
        }

        self._workspace_id = None
        self._application_key = None
        self._application_version = None
        self._last_patch_key = None

    @property
    def workspace_id(self):
        """
        Gets the workspace_id of this SourceApplicationInfo.
        The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.


        :return: The workspace_id of this SourceApplicationInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this SourceApplicationInfo.
        The OCID of the workspace containing the application. This allows cross workspace deployment to publish an application from a different workspace into the current workspace specified in this operation.


        :param workspace_id: The workspace_id of this SourceApplicationInfo.
        :type: str
        """
        self._workspace_id = workspace_id

    @property
    def application_key(self):
        """
        Gets the application_key of this SourceApplicationInfo.
        The source application key to use when creating the application.


        :return: The application_key of this SourceApplicationInfo.
        :rtype: str
        """
        return self._application_key

    @application_key.setter
    def application_key(self, application_key):
        """
        Sets the application_key of this SourceApplicationInfo.
        The source application key to use when creating the application.


        :param application_key: The application_key of this SourceApplicationInfo.
        :type: str
        """
        self._application_key = application_key

    @property
    def application_version(self):
        """
        Gets the application_version of this SourceApplicationInfo.
        The source application version of the application.


        :return: The application_version of this SourceApplicationInfo.
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this SourceApplicationInfo.
        The source application version of the application.


        :param application_version: The application_version of this SourceApplicationInfo.
        :type: str
        """
        self._application_version = application_version

    @property
    def last_patch_key(self):
        """
        Gets the last_patch_key of this SourceApplicationInfo.
        The last patch key for the application.


        :return: The last_patch_key of this SourceApplicationInfo.
        :rtype: str
        """
        return self._last_patch_key

    @last_patch_key.setter
    def last_patch_key(self, last_patch_key):
        """
        Sets the last_patch_key of this SourceApplicationInfo.
        The last patch key for the application.


        :param last_patch_key: The last_patch_key of this SourceApplicationInfo.
        :type: str
        """
        self._last_patch_key = last_patch_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
