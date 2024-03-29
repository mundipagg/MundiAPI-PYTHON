# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SubscriptionsMinimumPriceRequest(object):

    """Implementation of the 'Subscriptions Minimum Price Request' model.

    TODO: type model description here.

    Attributes:
        minimum_price (int): Valor mínimo da assinatura

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "minimum_price":'minimum_price'
    }

    def __init__(self,
                 minimum_price=None):
        """Constructor for the SubscriptionsMinimumPriceRequest class"""

        # Initialize members of the class
        self.minimum_price = minimum_price


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
        minimum_price = dictionary.get('minimum_price')

        # Return an object of this model
        return cls(minimum_price)


