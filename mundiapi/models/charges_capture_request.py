# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_split_request

class ChargesCaptureRequest(object):

    """Implementation of the 'Charges Capture Request' model.

    TODO: type model description here.

    Attributes:
        code (string): Code for the charge. Sending this field will update the
            code send on the charge and order creation.
        amount (int): The amount that will be captured
        split (list of CreateSplitRequest): Splits
        operation_reference (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "operation_reference":'operation_reference',
        "amount":'amount',
        "split":'split'
    }

    def __init__(self,
                 code=None,
                 operation_reference=None,
                 amount=None,
                 split=None):
        """Constructor for the ChargesCaptureRequest class"""

        # Initialize members of the class
        self.code = code
        self.amount = amount
        self.split = split
        self.operation_reference = operation_reference


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
        code = dictionary.get('code')
        operation_reference = dictionary.get('operation_reference')
        amount = dictionary.get('amount')
        split = None
        if dictionary.get('split') != None:
            split = list()
            for structure in dictionary.get('split'):
                split.append(mundiapi.models.create_split_request.CreateSplitRequest.from_dictionary(structure))

        # Return an object of this model
        return cls(code,
                   operation_reference,
                   amount,
                   split)


