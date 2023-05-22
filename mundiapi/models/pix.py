# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
import mundiapi.models.pix_additional_information

class Pix(object):

    """Implementation of the 'Pix' model.

    TODO: type model description here.

    Attributes:
        expires_at (datetime): Datetime when pix payment will expire
        expires_in (int): Seconds until pix payment expires
        additional_information (list of PixAdditionalInformation): Pix
            additional information

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "expires_at":'expires_at',
        "expires_in":'expires_in',
        "additional_information":'additional_information'
    }

    def __init__(self,
                 expires_at=None,
                 expires_in=None,
                 additional_information=None):
        """Constructor for the Pix class"""

        # Initialize members of the class
        self.expires_at = APIHelper.RFC3339DateTime(expires_at) if expires_at else None
        self.expires_in = expires_in
        self.additional_information = additional_information


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
        expires_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("expires_at")).datetime if dictionary.get("expires_at") else None
        expires_in = dictionary.get('expires_in')
        additional_information = None
        if dictionary.get('additional_information') != None:
            additional_information = list()
            for structure in dictionary.get('additional_information'):
                additional_information.append(mundiapi.models.pix_additional_information.PixAdditionalInformation.from_dictionary(structure))

        # Return an object of this model
        return cls(expires_at,
                   expires_in,
                   additional_information)

