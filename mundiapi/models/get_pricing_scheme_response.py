# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.api_helper import APIHelper
from mundiapi.models.get_price_bracket_response import GetPriceBracketResponse


class GetPricingSchemeResponse(object):

    """Implementation of the 'GetPricingSchemeResponse' model.

    Response object for getting a pricing scheme

    Attributes:
        price (int): TODO: type description here.
        scheme_type (string): TODO: type description here.
        price_brackets (list of GetPriceBracketResponse): TODO: type
            description here.
        minimum_price (int): TODO: type description here.
        percentage (float): percentual value used in pricing_scheme Percent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price": 'price',
        "scheme_type": 'scheme_type',
        "price_brackets": 'price_brackets',
        "minimum_price": 'minimum_price',
        "percentage": 'percentage'
    }

    _optionals = [
        'minimum_price',
        'percentage',
    ]

    def __init__(self,
                 price=None,
                 scheme_type=None,
                 price_brackets=None,
                 minimum_price=APIHelper.SKIP,
                 percentage=APIHelper.SKIP):
        """Constructor for the GetPricingSchemeResponse class"""

        # Initialize members of the class
        self.price = price 
        self.scheme_type = scheme_type 
        self.price_brackets = price_brackets 
        if minimum_price is not APIHelper.SKIP:
            self.minimum_price = minimum_price 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        price = dictionary.get("price") if dictionary.get("price") else None
        scheme_type = dictionary.get("scheme_type") if dictionary.get("scheme_type") else None
        price_brackets = None
        if dictionary.get('price_brackets') is not None:
            price_brackets = [GetPriceBracketResponse.from_dictionary(x) for x in dictionary.get('price_brackets')]
        minimum_price = dictionary.get("minimum_price") if dictionary.get("minimum_price") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        # Return an object of this model
        return cls(price,
                   scheme_type,
                   price_brackets,
                   minimum_price,
                   percentage)
