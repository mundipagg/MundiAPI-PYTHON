# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RecipientsTransfersRequest(object):

    """Implementation of the 'Recipients Transfers Request' model.

    TODO: type model description here.

    Attributes:
        amount (int): Transfer amount
        metadata (dict<object, string>): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "metadata":'metadata'
    }

    def __init__(self,
                 amount=None,
                 metadata=None):
        """Constructor for the RecipientsTransfersRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.metadata = metadata


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
        amount = dictionary.get('amount')
        metadata = dictionary.get('metadata')

        # Return an object of this model
        return cls(amount,
                   metadata)


