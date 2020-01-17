# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
from mundiapi.configuration import Configuration
from mundiapi.controllers.base_controller import BaseController
from mundiapi.models.get_token_response import GetTokenResponse

class TokensController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_token(self,
                  id,
                  public_key):
        """Does a GET request to /tokens/{id}?appId={public_key}.

        Gets a token from its id

        Args:
            id (string): Token id
            public_key (string): Public key

        Returns:
            GetTokenResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/tokens/{id}?appId={public_key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id,
            'public_key': public_key
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
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetTokenResponse.from_dictionary)

    def create_token(self,
                     public_key,
                     request,
                     idempotency_key=None):
        """Does a POST request to /tokens?appId={public_key}.

        TODO: type endpoint description here.

        Args:
            public_key (string): Public key
            request (CreateTokenRequest): Request for creating a token
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetTokenResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/tokens?appId={public_key}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'public_key': public_key
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetTokenResponse.from_dictionary)
