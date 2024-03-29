# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Setup(object):

    """Implementation of the 'Setup' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        description (string): TODO: type description here.
        amount (int): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "description":'description',
        "amount":'amount',
        "status":'status'
    }

    def __init__(self,
                 id=None,
                 description=None,
                 amount=None,
                 status=None):
        """Constructor for the Setup class"""

        # Initialize members of the class
        self.id = id
        self.description = description
        self.amount = amount
        self.status = status


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
        id = dictionary.get('id')
        description = dictionary.get('description')
        amount = dictionary.get('amount')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(id,
                   description,
                   amount,
                   status)


