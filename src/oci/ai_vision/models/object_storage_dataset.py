# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .dataset import Dataset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageDataset(Dataset):
    """
    The dataset that resides in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageDataset object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ObjectStorageDataset.dataset_type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dataset_type:
            The value to assign to the dataset_type property of this ObjectStorageDataset.
            Allowed values for this property are: "DATA_SCIENCE_LABELING", "OBJECT_STORAGE"
        :type dataset_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectStorageDataset.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageDataset.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this ObjectStorageDataset.
        :type object_name: str

        """
        self.swagger_types = {
            'dataset_type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'dataset_type': 'datasetType',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._dataset_type = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._dataset_type = 'OBJECT_STORAGE'

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ObjectStorageDataset.
        The namespace name of the Object Storage bucket that contains the input data file.


        :return: The namespace_name of this ObjectStorageDataset.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectStorageDataset.
        The namespace name of the Object Storage bucket that contains the input data file.


        :param namespace_name: The namespace_name of this ObjectStorageDataset.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageDataset.
        The name of the Object Storage bucket that contains the input data file.


        :return: The bucket_name of this ObjectStorageDataset.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageDataset.
        The name of the Object Storage bucket that contains the input data file.


        :param bucket_name: The bucket_name of this ObjectStorageDataset.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ObjectStorageDataset.
        The object name of the input data file.


        :return: The object_name of this ObjectStorageDataset.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ObjectStorageDataset.
        The object name of the input data file.


        :param object_name: The object_name of this ObjectStorageDataset.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
