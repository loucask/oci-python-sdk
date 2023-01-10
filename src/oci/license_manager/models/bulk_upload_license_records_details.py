# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUploadLicenseRecordsDetails(object):
    """
    Details required for bulk uploading of license records.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUploadLicenseRecordsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this BulkUploadLicenseRecordsDetails.
        :type compartment_id: str

        :param file_name:
            The value to assign to the file_name property of this BulkUploadLicenseRecordsDetails.
        :type file_name: str

        :param file_content:
            The value to assign to the file_content property of this BulkUploadLicenseRecordsDetails.
        :type file_content: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'file_name': 'str',
            'file_content': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'file_name': 'fileName',
            'file_content': 'fileContent'
        }

        self._compartment_id = None
        self._file_name = None
        self._file_content = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BulkUploadLicenseRecordsDetails.
        The compartment `OCID`__ where license records are created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this BulkUploadLicenseRecordsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BulkUploadLicenseRecordsDetails.
        The compartment `OCID`__ where license records are created.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this BulkUploadLicenseRecordsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def file_name(self):
        """
        **[Required]** Gets the file_name of this BulkUploadLicenseRecordsDetails.
        Name of the file that is being uploaded.


        :return: The file_name of this BulkUploadLicenseRecordsDetails.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this BulkUploadLicenseRecordsDetails.
        Name of the file that is being uploaded.


        :param file_name: The file_name of this BulkUploadLicenseRecordsDetails.
        :type: str
        """
        self._file_name = file_name

    @property
    def file_content(self):
        """
        **[Required]** Gets the file_content of this BulkUploadLicenseRecordsDetails.
        The file to be uploaded.


        :return: The file_content of this BulkUploadLicenseRecordsDetails.
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        """
        Sets the file_content of this BulkUploadLicenseRecordsDetails.
        The file to be uploaded.


        :param file_content: The file_content of this BulkUploadLicenseRecordsDetails.
        :type: str
        """
        self._file_content = file_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
