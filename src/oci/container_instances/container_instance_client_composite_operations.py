# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ContainerInstanceClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.container_instances.ContainerInstanceClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new ContainerInstanceClientCompositeOperations object

        :param ContainerInstanceClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def change_container_instance_compartment_and_wait_for_state(self, container_instance_id, change_container_instance_compartment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.change_container_instance_compartment` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param oci.container_instances.models.ChangeContainerInstanceCompartmentDetails change_container_instance_compartment_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.change_container_instance_compartment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.change_container_instance_compartment(container_instance_id, change_container_instance_compartment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_container_instance_and_wait_for_state(self, create_container_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.create_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param oci.container_instances.models.CreateContainerInstanceDetails create_container_instance_details: (required)
            Details for the new ContainerInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.create_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_container_instance(create_container_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_container_instance_and_wait_for_state(self, container_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.delete_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.delete_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_container_instance(container_instance_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restart_container_instance_and_wait_for_state(self, container_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.restart_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.restart_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restart_container_instance(container_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def start_container_instance_and_wait_for_state(self, container_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.start_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.start_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.start_container_instance(container_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def stop_container_instance_and_wait_for_state(self, container_instance_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.stop_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.stop_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.stop_container_instance(container_instance_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_container_and_wait_for_state(self, container_id, update_container_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.update_container` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_id: (required)
            The unique identifier for the Container.

        :param oci.container_instances.models.UpdateContainerDetails update_container_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.update_container`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_container(container_id, update_container_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_container_instance_and_wait_for_state(self, container_instance_id, update_container_instance_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.container_instances.ContainerInstanceClient.update_container_instance` and waits for the :py:class:`~oci.container_instances.models.WorkRequest`
        to enter the given state(s).

        :param str container_instance_id: (required)
            The system-generated unique identifier for the ContainerInstance.

        :param oci.container_instances.models.UpdateContainerInstanceDetails update_container_instance_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.container_instances.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.container_instances.ContainerInstanceClient.update_container_instance`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_container_instance(container_instance_id, update_container_instance_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
