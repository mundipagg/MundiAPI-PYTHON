# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
from mundiapi.configuration import Configuration
from mundiapi.controllers.base_controller import BaseController
from mundiapi.http.auth.basic_auth import BasicAuth
from mundiapi.models.orders_closed_response import OrdersClosedResponse
from mundiapi.models.orders_items_response import OrdersItemsResponse
from mundiapi.models.orders_items_response_1 import OrdersItemsResponse1
from mundiapi.models.orders_metadata_response import OrdersMetadataResponse
from mundiapi.models.orders_response import OrdersResponse
from mundiapi.models.orders_response_1 import OrdersResponse1
from mundiapi.exceptions.error_exception import ErrorException

class OrdersController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def update_order_status(self,
                            id,
                            body,
                            idempotency_key=None):
        """Does a PATCH request to /orders/{id}/closed.

        UpdateOrderStatus

        Args:
            id (string): Order Id
            body (UpdateOrderStatusRequest): Update Order Model
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersClosedResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{id}/closed'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersClosedResponse.from_dictionary)

    def delete_all_order_items(self,
                               order_id,
                               idempotency_key=None):
        """Does a DELETE request to /orders/{orderId}/items.

        DeleteAllOrderItems

        Args:
            order_id (string): Order Id
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersItemsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{orderId}/items'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'orderId': order_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersItemsResponse.from_dictionary)

    def create_order_item(self,
                          order_id,
                          body,
                          idempotency_key=None):
        """Does a POST request to /orders/{orderId}/items.

        CreateOrderItem

        Args:
            order_id (string): Order Id
            body (OrdersItemsRequest): Order Item Model
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersItemsResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{orderId}/items'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'orderId': order_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersItemsResponse1.from_dictionary)

    def update_order_metadata(self,
                              order_id,
                              body,
                              idempotency_key=None):
        """Does a PATCH request to /Orders/{order_id}/metadata.

        Updates the metadata from an order

        Args:
            order_id (string): The order id
            body (OrdersMetadataRequest): Request for updating the order
                metadata
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersMetadataResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Orders/{order_id}/metadata'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'order_id': order_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersMetadataResponse.from_dictionary)

    def get_orders(self,
                   page=None,
                   size=None,
                   code=None,
                   status=None,
                   created_since=None,
                   created_until=None,
                   customer_id=None):
        """Does a GET request to /orders.

        Gets all orders

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (string, optional): Filter for order's code
            status (string, optional): Filter for order's status
            created_since (datetime, optional): Filter for order's creation
                date start range
            created_until (datetime, optional): Filter for order's creation
                date end range
            customer_id (string, optional): Filter for order's customer id

        Returns:
            OrdersResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'code': code,
            'status': status,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until),
            'customer_id': customer_id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersResponse.from_dictionary)

    def create_order(self,
                     body,
                     idempotency_key=None):
        """Does a POST request to /orders.

        Creates a new Order

        Args:
            body (OrdersRequest): Request for creating an order
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersResponse1.from_dictionary)

    def delete_order_item(self,
                          order_id,
                          item_id,
                          idempotency_key=None):
        """Does a DELETE request to /orders/{orderId}/items/{itemId}.

        DeleteOrderItem

        Args:
            order_id (string): Order Id
            item_id (string): Item Id
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersItemsResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{orderId}/items/{itemId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'orderId': order_id,
            'itemId': item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersItemsResponse1.from_dictionary)

    def get_order_item(self,
                       order_id,
                       item_id):
        """Does a GET request to /orders/{orderId}/items/{itemId}.

        GetOrderItem

        Args:
            order_id (string): Order Id
            item_id (string): Item Id

        Returns:
            OrdersItemsResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{orderId}/items/{itemId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'orderId': order_id,
            'itemId': item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersItemsResponse1.from_dictionary)

    def update_order_item(self,
                          order_id,
                          item_id,
                          body,
                          idempotency_key=None):
        """Does a PUT request to /orders/{orderId}/items/{itemId}.

        UpdateOrderItem

        Args:
            order_id (string): Order Id
            item_id (string): Item Id
            body (OrdersItemsRequest1): Item Model
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            OrdersItemsResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{orderId}/items/{itemId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'orderId': order_id,
            'itemId': item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name,
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersItemsResponse1.from_dictionary)

    def get_order(self,
                  order_id):
        """Does a GET request to /orders/{order_id}.

        Gets an order

        Args:
            order_id (string): Order id

        Returns:
            OrdersResponse1: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/orders/{order_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'order_id': order_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'ServiceRefererName': Configuration.service_referer_name
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OrdersResponse1.from_dictionary)
