# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.authentication_2

class DebitCard2(object):

    """Implementation of the 'DebitCard2' model.

    TODO: type model description here.

    Attributes:
        statement_descriptor (string): Card invoice text descriptor
        authentication (Authentication2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authentication":'authentication',
        "statement_descriptor":'statement_descriptor'
    }

    def __init__(self,
                 authentication=None,
                 statement_descriptor=None):
        """Constructor for the DebitCard2 class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.authentication = authentication


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        authentication = mundiapi.models.authentication_2.Authentication2.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        statement_descriptor = dictionary.get('statement_descriptor')

        # Return an object of this model
        return cls(authentication,
                   statement_descriptor)

