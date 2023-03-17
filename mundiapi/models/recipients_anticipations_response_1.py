# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_anticipation_response
import mundiapi.models.paging

class RecipientsAnticipationsResponse1(object):

    """Implementation of the 'Recipients Anticipations Response1' model.

    TODO: type model description here.

    Attributes:
        data (list of GetAnticipationResponse): Anticipations
        paging (Paging): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data":'data',
        "paging":'paging'
    }

    def __init__(self,
                 data=None,
                 paging=None):
        """Constructor for the RecipientsAnticipationsResponse1 class"""

        # Initialize members of the class
        self.data = data
        self.paging = paging


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
        data = None
        if dictionary.get('data') != None:
            data = list()
            for structure in dictionary.get('data'):
                data.append(mundiapi.models.get_anticipation_response.GetAnticipationResponse.from_dictionary(structure))
        paging = mundiapi.models.paging.Paging.from_dictionary(dictionary.get('paging')) if dictionary.get('paging') else None

        # Return an object of this model
        return cls(data,
                   paging)


