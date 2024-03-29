# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.payment

class Setup1(object):

    """Implementation of the 'Setup1' model.

    TODO: type model description here.

    Attributes:
        amount (int): Setup amount
        description (string): Description
        payment (Payment): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "description":'description',
        "payment":'payment'
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 payment=None):
        """Constructor for the Setup1 class"""

        # Initialize members of the class
        self.amount = amount
        self.description = description
        self.payment = payment


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
        description = dictionary.get('description')
        payment = mundiapi.models.payment.Payment.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None

        # Return an object of this model
        return cls(amount,
                   description,
                   payment)


