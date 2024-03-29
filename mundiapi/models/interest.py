# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Interest(object):

    """Implementation of the 'Interest' model.

    TODO: type model description here.

    Attributes:
        days (int): Days
        mtype (string): Type
        amount (int): Amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days":'days',
        "mtype":'type',
        "amount":'amount'
    }

    def __init__(self,
                 days=None,
                 mtype=None,
                 amount=None):
        """Constructor for the Interest class"""

        # Initialize members of the class
        self.days = days
        self.mtype = mtype
        self.amount = amount


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
        days = dictionary.get('days')
        mtype = dictionary.get('type')
        amount = dictionary.get('amount')

        # Return an object of this model
        return cls(days,
                   mtype,
                   amount)


