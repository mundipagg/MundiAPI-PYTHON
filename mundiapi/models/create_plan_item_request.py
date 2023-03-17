# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.pricing_scheme_4

class CreatePlanItemRequest(object):

    """Implementation of the 'CreatePlanItemRequest' model.

    Request for creating a plan item

    Attributes:
        name (string): Item name
        pricing_scheme (PricingScheme4): TODO: type description here.
        id (string): Item's id
        description (string): Item's description
        cycles (int): Number of cycles where the item will be charged
        quantity (int): Quantity

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "pricing_scheme":'pricing_scheme',
        "id":'id',
        "description":'description',
        "cycles":'cycles',
        "quantity":'quantity'
    }

    def __init__(self,
                 name=None,
                 pricing_scheme=None,
                 id=None,
                 description=None,
                 cycles=None,
                 quantity=None):
        """Constructor for the CreatePlanItemRequest class"""

        # Initialize members of the class
        self.name = name
        self.pricing_scheme = pricing_scheme
        self.id = id
        self.description = description
        self.cycles = cycles
        self.quantity = quantity


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
        name = dictionary.get('name')
        pricing_scheme = mundiapi.models.pricing_scheme_4.PricingScheme4.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        id = dictionary.get('id')
        description = dictionary.get('description')
        cycles = dictionary.get('cycles')
        quantity = dictionary.get('quantity')

        # Return an object of this model
        return cls(name,
                   pricing_scheme,
                   id,
                   description,
                   cycles,
                   quantity)


