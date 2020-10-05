# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_recipient_response
import mundiapi.models.get_split_options_response

class GetSplitResponse(object):

    """Implementation of the 'GetSplitResponse' model.

    Split response

    Attributes:
        mtype (string): Type
        amount (int): Amount
        recipient (GetRecipientResponse): Recipient
        gateway_id (string): The split rule gateway id
        options (GetSplitOptionsResponse): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "amount":'amount',
        "gateway_id":'gateway_id',
        "recipient":'recipient',
        "options":'options'
    }

    def __init__(self,
                 mtype=None,
                 amount=None,
                 gateway_id=None,
                 recipient=None,
                 options=None):
        """Constructor for the GetSplitResponse class"""

        # Initialize members of the class
        self.mtype = mtype
        self.amount = amount
        self.recipient = recipient
        self.gateway_id = gateway_id
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
        gateway_id = dictionary.get('gateway_id')
        recipient = mundiapi.models.get_recipient_response.GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None
        options = mundiapi.models.get_split_options_response.GetSplitOptionsResponse.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None

        # Return an object of this model
        return cls(mtype,
                   amount,
                   gateway_id,
                   recipient,
                   options)


