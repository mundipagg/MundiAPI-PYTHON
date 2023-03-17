# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.options_2

class CreateSplitRequest(object):

    """Implementation of the 'CreateSplitRequest' model.

    Split

    Attributes:
        mtype (string): Split type
        amount (int): Amount
        recipient_id (string): Recipient id
        options (Options2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "amount":'amount',
        "recipient_id":'recipient_id',
        "options":'options'
    }

    def __init__(self,
                 mtype=None,
                 amount=None,
                 recipient_id=None,
                 options=None):
        """Constructor for the CreateSplitRequest class"""

        # Initialize members of the class
        self.mtype = mtype
        self.amount = amount
        self.recipient_id = recipient_id
        self.options = options


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
        mtype = dictionary.get('type')
        amount = dictionary.get('amount')
        recipient_id = dictionary.get('recipient_id')
        options = mundiapi.models.options_2.Options2.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None

        # Return an object of this model
        return cls(mtype,
                   amount,
                   recipient_id,
                   options)


