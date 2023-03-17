# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.pricing_scheme_4
import mundiapi.models.create_discount_request

class SubscriptionsItemsRequest1(object):

    """Implementation of the 'Subscriptions Items Request1' model.

    TODO: type model description here.

    Attributes:
        description (string): Item description
        pricing_scheme (PricingScheme4): TODO: type description here.
        id (string): Item id
        plan_item_id (string): Plan item id
        discounts (list of CreateDiscountRequest): Discounts for the item
        name (string): Item name
        cycles (int): Number of cycles which the item will be charged
        quantity (int): Quantity of items
        minimum_price (int): Minimum price

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "pricing_scheme":'pricing_scheme',
        "id":'id',
        "plan_item_id":'plan_item_id',
        "discounts":'discounts',
        "name":'name',
        "cycles":'cycles',
        "quantity":'quantity',
        "minimum_price":'minimum_price'
    }

    def __init__(self,
                 description=None,
                 pricing_scheme=None,
                 id=None,
                 plan_item_id=None,
                 discounts=None,
                 name=None,
                 cycles=None,
                 quantity=None,
                 minimum_price=None):
        """Constructor for the SubscriptionsItemsRequest1 class"""

        # Initialize members of the class
        self.description = description
        self.pricing_scheme = pricing_scheme
        self.id = id
        self.plan_item_id = plan_item_id
        self.discounts = discounts
        self.name = name
        self.cycles = cycles
        self.quantity = quantity
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
        description = dictionary.get('description')
        pricing_scheme = mundiapi.models.pricing_scheme_4.PricingScheme4.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        id = dictionary.get('id')
        plan_item_id = dictionary.get('plan_item_id')
        discounts = None
        if dictionary.get('discounts') != None:
            discounts = list()
            for structure in dictionary.get('discounts'):
                discounts.append(mundiapi.models.create_discount_request.CreateDiscountRequest.from_dictionary(structure))
        name = dictionary.get('name')
        cycles = dictionary.get('cycles')
        quantity = dictionary.get('quantity')
        minimum_price = dictionary.get('minimum_price')

        # Return an object of this model
        return cls(description,
                   pricing_scheme,
                   id,
                   plan_item_id,
                   discounts,
                   name,
                   cycles,
                   quantity,
                   minimum_price)


