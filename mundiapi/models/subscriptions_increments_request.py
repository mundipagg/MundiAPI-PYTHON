# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SubscriptionsIncrementsRequest(object):

    """Implementation of the 'Subscriptions Increments Request' model.

    TODO: type model description here.

    Attributes:
        value (float): The increment value
        increment_type (string): Increment type. Can be either flat or
            percentage.
        item_id (string): The item where the increment will be applied
        cycles (int): Number of cycles that the increment will be applied
        description (string): Description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value":'value',
        "increment_type":'increment_type',
        "item_id":'item_id',
        "cycles":'cycles',
        "description":'description'
    }

    def __init__(self,
                 value=None,
                 increment_type=None,
                 item_id=None,
                 cycles=None,
                 description=None):
        """Constructor for the SubscriptionsIncrementsRequest class"""

        # Initialize members of the class
        self.value = value
        self.increment_type = increment_type
        self.item_id = item_id
        self.cycles = cycles
        self.description = description


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
        value = dictionary.get('value')
        increment_type = dictionary.get('increment_type')
        item_id = dictionary.get('item_id')
        cycles = dictionary.get('cycles')
        description = dictionary.get('description')

        # Return an object of this model
        return cls(value,
                   increment_type,
                   item_id,
                   cycles,
                   description)


