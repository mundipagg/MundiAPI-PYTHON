# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
from mundiapi.configuration import Configuration
from mundiapi.controllers.base_controller import BaseController
from mundiapi.models.tokens_response import TokensResponse
from mundiapi.exceptions.error_exception import ErrorException

class TokensController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def create_token(self,
                     public_key,
                     body,
                     idempotency_key=None,
                     app_id=None):
        """Does a POST request to /tokens.

        CreateToken

        Args:
            public_key (string): Public key
            body (TokensRequest): Request for creating a token
            idempotency_key (string, optional): TODO: type description here.
                Example: 
            app_id (string, optional): TODO: type description here. Example: 

        Returns:
            TokensResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/tokens'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'public_key': public_key
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'appId': app_id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
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
        return APIHelper.json_deserialize(_context.response.raw_body, TokensResponse.from_dictionary)

    def get_token(self,
                  id,
                  public_key,
                  app_id=None):
        """Does a GET request to /tokens/{id}.

        Gets a token from its id

        Args:
            id (string): Token id
            public_key (string): Public key
            app_id (string, optional): TODO: type description here. Example: 

        Returns:
            TokensResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/tokens/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id,
            'public_key': public_key
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'appId': app_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, TokensResponse.from_dictionary)
