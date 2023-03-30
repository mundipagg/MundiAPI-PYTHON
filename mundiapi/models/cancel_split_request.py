# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.api_helper import APIHelper
from mundiapi.models.create_split_options_request import CreateSplitOptionsRequest


class CancelSplitRequest(object):

    """Implementation of the 'CancelSplitRequest' model.

    Split

    Attributes:
        mtype (string): Split type
        amount (int): Amount
        recipient_id (string): Recipient id
        options (CreateSplitOptionsRequest): The split options request
        split_rule_id (string): Rule id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "amount": 'amount',
        "recipient_id": 'recipient_id',
        "options": 'options',
        "split_rule_id": 'split_rule_id'
    }

    _optionals = [
        'options',
        'split_rule_id',
    ]

    def __init__(self,
                 mtype=None,
                 amount=None,
                 recipient_id=None,
                 options=APIHelper.SKIP,
                 split_rule_id=APIHelper.SKIP):
        """Constructor for the CancelSplitRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.amount = amount 
        self.recipient_id = recipient_id 
        if options is not APIHelper.SKIP:
            self.options = options 
        if split_rule_id is not APIHelper.SKIP:
            self.split_rule_id = split_rule_id 

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

        mtype = dictionary.get("type") if dictionary.get("type") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        recipient_id = dictionary.get("recipient_id") if dictionary.get("recipient_id") else None
        options = CreateSplitOptionsRequest.from_dictionary(dictionary.get('options')) if 'options' in dictionary.keys() else APIHelper.SKIP
        split_rule_id = dictionary.get("split_rule_id") if dictionary.get("split_rule_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   amount,
                   recipient_id,
                   options,
                   split_rule_id)
