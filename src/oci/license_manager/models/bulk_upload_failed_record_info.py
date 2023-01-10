# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUploadFailedRecordInfo(object):
    """
    Error information for a valid license record that could not be uploaded.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUploadFailedRecordInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param row_number:
            The value to assign to the row_number property of this BulkUploadFailedRecordInfo.
        :type row_number: int

        :param product_name:
            The value to assign to the product_name property of this BulkUploadFailedRecordInfo.
        :type product_name: str

        :param error:
            The value to assign to the error property of this BulkUploadFailedRecordInfo.
        :type error: str

        """
        self.swagger_types = {
            'row_number': 'int',
            'product_name': 'str',
            'error': 'str'
        }

        self.attribute_map = {
            'row_number': 'rowNumber',
            'product_name': 'productName',
            'error': 'error'
        }

        self._row_number = None
        self._product_name = None
        self._error = None

    @property
    def row_number(self):
        """
        **[Required]** Gets the row_number of this BulkUploadFailedRecordInfo.
        Refers to the license record number as provided in the bulk upload file.


        :return: The row_number of this BulkUploadFailedRecordInfo.
        :rtype: int
        """
        return self._row_number

    @row_number.setter
    def row_number(self, row_number):
        """
        Sets the row_number of this BulkUploadFailedRecordInfo.
        Refers to the license record number as provided in the bulk upload file.


        :param row_number: The row_number of this BulkUploadFailedRecordInfo.
        :type: int
        """
        self._row_number = row_number

    @property
    def product_name(self):
        """
        **[Required]** Gets the product_name of this BulkUploadFailedRecordInfo.
        Product name of the failed row.


        :return: The product_name of this BulkUploadFailedRecordInfo.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this BulkUploadFailedRecordInfo.
        Product name of the failed row.


        :param product_name: The product_name of this BulkUploadFailedRecordInfo.
        :type: str
        """
        self._product_name = product_name

    @property
    def error(self):
        """
        **[Required]** Gets the error of this BulkUploadFailedRecordInfo.
        Failed license record error information.


        :return: The error of this BulkUploadFailedRecordInfo.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this BulkUploadFailedRecordInfo.
        Failed license record error information.


        :param error: The error of this BulkUploadFailedRecordInfo.
        :type: str
        """
        self._error = error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
