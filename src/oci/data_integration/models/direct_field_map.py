# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .field_map import FieldMap
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DirectFieldMap(FieldMap):
    """
    The information about a field map.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DirectFieldMap object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DirectFieldMap.model_type` attribute
        of this class is ``DIRECT_FIELD_MAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DirectFieldMap.
            Allowed values for this property are: "DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP", "CONDITIONAL_COMPOSITE_FIELD_MAP", "NAMED_ENTITY_MAP", "RULE_BASED_ENTITY_MAP"
        :type model_type: str

        :param description:
            The value to assign to the description property of this DirectFieldMap.
        :type description: str

        :param key:
            The value to assign to the key property of this DirectFieldMap.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DirectFieldMap.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DirectFieldMap.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this DirectFieldMap.
        :type config_values: oci.data_integration.models.ConfigValues

        :param source_typed_object:
            The value to assign to the source_typed_object property of this DirectFieldMap.
        :type source_typed_object: str

        :param target_typed_object:
            The value to assign to the target_typed_object property of this DirectFieldMap.
        :type target_typed_object: str

        :param source_scope_reference:
            The value to assign to the source_scope_reference property of this DirectFieldMap.
        :type source_scope_reference: oci.data_integration.models.ScopeReference

        :param target_scope_reference:
            The value to assign to the target_scope_reference property of this DirectFieldMap.
        :type target_scope_reference: oci.data_integration.models.ScopeReference

        :param object_status:
            The value to assign to the object_status property of this DirectFieldMap.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'description': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'source_typed_object': 'str',
            'target_typed_object': 'str',
            'source_scope_reference': 'ScopeReference',
            'target_scope_reference': 'ScopeReference',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'description': 'description',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'source_typed_object': 'sourceTypedObject',
            'target_typed_object': 'targetTypedObject',
            'source_scope_reference': 'sourceScopeReference',
            'target_scope_reference': 'targetScopeReference',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._description = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._source_typed_object = None
        self._target_typed_object = None
        self._source_scope_reference = None
        self._target_scope_reference = None
        self._object_status = None
        self._model_type = 'DIRECT_FIELD_MAP'

    @property
    def key(self):
        """
        Gets the key of this DirectFieldMap.
        The object key.


        :return: The key of this DirectFieldMap.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DirectFieldMap.
        The object key.


        :param key: The key of this DirectFieldMap.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DirectFieldMap.
        The object's model version.


        :return: The model_version of this DirectFieldMap.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DirectFieldMap.
        The object's model version.


        :param model_version: The model_version of this DirectFieldMap.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DirectFieldMap.

        :return: The parent_ref of this DirectFieldMap.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DirectFieldMap.

        :param parent_ref: The parent_ref of this DirectFieldMap.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def config_values(self):
        """
        Gets the config_values of this DirectFieldMap.

        :return: The config_values of this DirectFieldMap.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this DirectFieldMap.

        :param config_values: The config_values of this DirectFieldMap.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def source_typed_object(self):
        """
        Gets the source_typed_object of this DirectFieldMap.
        Deprecated - Reference to a typed object.


        :return: The source_typed_object of this DirectFieldMap.
        :rtype: str
        """
        return self._source_typed_object

    @source_typed_object.setter
    def source_typed_object(self, source_typed_object):
        """
        Sets the source_typed_object of this DirectFieldMap.
        Deprecated - Reference to a typed object.


        :param source_typed_object: The source_typed_object of this DirectFieldMap.
        :type: str
        """
        self._source_typed_object = source_typed_object

    @property
    def target_typed_object(self):
        """
        Gets the target_typed_object of this DirectFieldMap.
        Deprecated - Reference to a typed object.


        :return: The target_typed_object of this DirectFieldMap.
        :rtype: str
        """
        return self._target_typed_object

    @target_typed_object.setter
    def target_typed_object(self, target_typed_object):
        """
        Sets the target_typed_object of this DirectFieldMap.
        Deprecated - Reference to a typed object.


        :param target_typed_object: The target_typed_object of this DirectFieldMap.
        :type: str
        """
        self._target_typed_object = target_typed_object

    @property
    def source_scope_reference(self):
        """
        Gets the source_scope_reference of this DirectFieldMap.

        :return: The source_scope_reference of this DirectFieldMap.
        :rtype: oci.data_integration.models.ScopeReference
        """
        return self._source_scope_reference

    @source_scope_reference.setter
    def source_scope_reference(self, source_scope_reference):
        """
        Sets the source_scope_reference of this DirectFieldMap.

        :param source_scope_reference: The source_scope_reference of this DirectFieldMap.
        :type: oci.data_integration.models.ScopeReference
        """
        self._source_scope_reference = source_scope_reference

    @property
    def target_scope_reference(self):
        """
        Gets the target_scope_reference of this DirectFieldMap.

        :return: The target_scope_reference of this DirectFieldMap.
        :rtype: oci.data_integration.models.ScopeReference
        """
        return self._target_scope_reference

    @target_scope_reference.setter
    def target_scope_reference(self, target_scope_reference):
        """
        Sets the target_scope_reference of this DirectFieldMap.

        :param target_scope_reference: The target_scope_reference of this DirectFieldMap.
        :type: oci.data_integration.models.ScopeReference
        """
        self._target_scope_reference = target_scope_reference

    @property
    def object_status(self):
        """
        Gets the object_status of this DirectFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DirectFieldMap.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DirectFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DirectFieldMap.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
