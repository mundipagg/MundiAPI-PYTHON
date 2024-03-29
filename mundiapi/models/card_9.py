# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Card9(object):

    """Implementation of the 'Card9' model.

    TODO: type model description here.

    Attributes:
        last_four_digits (string): TODO: type description here.
        holder_name (string): TODO: type description here.
        holder_document (string): TODO: type description here.
        exp_month (string): TODO: type description here.
        exp_year (string): TODO: type description here.
        brand (string): TODO: type description here.
        mtype (string): TODO: type description here.
        label (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_four_digits":'last_four_digits',
        "holder_name":'holder_name',
        "holder_document":'holder_document',
        "exp_month":'exp_month',
        "exp_year":'exp_year',
        "brand":'brand',
        "mtype":'type',
        "label":'label'
    }

    def __init__(self,
                 last_four_digits=None,
                 holder_name=None,
                 holder_document=None,
                 exp_month=None,
                 exp_year=None,
                 brand=None,
                 mtype=None,
                 label=None):
        """Constructor for the Card9 class"""

        # Initialize members of the class
        self.last_four_digits = last_four_digits
        self.holder_name = holder_name
        self.holder_document = holder_document
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.brand = brand
        self.mtype = mtype
        self.label = label


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
        last_four_digits = dictionary.get('last_four_digits')
        holder_name = dictionary.get('holder_name')
        holder_document = dictionary.get('holder_document')
        exp_month = dictionary.get('exp_month')
        exp_year = dictionary.get('exp_year')
        brand = dictionary.get('brand')
        mtype = dictionary.get('type')
        label = dictionary.get('label')

        # Return an object of this model
        return cls(last_four_digits,
                   holder_name,
                   holder_document,
                   exp_month,
                   exp_year,
                   brand,
                   mtype,
                   label)


