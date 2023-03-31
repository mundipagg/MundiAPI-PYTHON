# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
from mundiapi.configuration import Configuration
from mundiapi.controllers.base_controller import BaseController
from mundiapi.http.auth.basic_auth import BasicAuth
from mundiapi.models.get_transfer import GetTransfer
from mundiapi.models.list_transfers import ListTransfers
from mundiapi.exceptions.error_exception import ErrorException

class TransfersController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_transfer_by_id(self,
                           transfer_id):
        """Does a GET request to /transfers/{transfer_id}.

        GetTransferById

        Args:
            transfer_id (string): TODO: type description here. Example: 

        Returns:
            GetTransfer: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers/{transfer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'transfer_id': transfer_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransfer.from_dictionary)

    def post_create_transfer(self,
                             body):
        """Does a POST request to /transfers/recipients.

        CreateTransfer

        Args:
            body (CreateTransfer): TODO: type description here. Example: 

        Returns:
            GetTransfer: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers/recipients'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransfer.from_dictionary)

    def get_transfers_1(self):
        """Does a GET request to /transfers.

        Gets all transfers

        Returns:
            ListTransfers: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListTransfers.from_dictionary)
