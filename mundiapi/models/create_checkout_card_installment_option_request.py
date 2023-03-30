# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateCheckoutCardInstallmentOptionRequest(object):

    """Implementation of the 'CreateCheckoutCardInstallmentOptionRequest' model.

    Options for card installment

    Attributes:
        number (int): Installment quantity
        total (int): Total amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number": 'number',
        "total": 'total'
    }

    def __init__(self,
                 number=None,
                 total=None):
        """Constructor for the CreateCheckoutCardInstallmentOptionRequest class"""

        # Initialize members of the class
        self.number = number 
        self.total = total 

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

        number = dictionary.get("number") if dictionary.get("number") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        # Return an object of this model
        return cls(number,
                   total)
