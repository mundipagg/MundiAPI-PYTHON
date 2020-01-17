# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_address_request
import mundiapi.models.create_card_options_request

class CreateCardRequest(object):

    """Implementation of the 'CreateCardRequest' model.

    Card data

    Attributes:
        number (string): Credit card number
        holder_name (string): Holder name, as written on the card
        exp_month (int): The expiration month
        exp_year (int): The expiration year, that can be informed with 2 or 4
            digits
        cvv (string): The card's security code
        billing_address (CreateAddressRequest): Card's billing address
        brand (string): Card brand
        billing_address_id (string): The address id for the billing address
        metadata (dict<object, string>): Metadata
        mtype (string): Card type
        options (CreateCardOptionsRequest): Options for creating the card
        holder_document (string): Document number for the card's holder
        private_label (bool): Indicates whether it is a private label card
        label (string): TODO: type description here.
        id (string): Identifier
        token (string): token identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number":'number',
        "holder_name":'holder_name',
        "exp_month":'exp_month',
        "exp_year":'exp_year',
        "cvv":'cvv',
        "billing_address":'billing_address',
        "brand":'brand',
        "billing_address_id":'billing_address_id',
        "metadata":'metadata',
        "mtype":'type',
        "options":'options',
        "private_label":'private_label',
        "label":'label',
        "holder_document":'holder_document',
        "id":'id',
        "token":'token'
    }

    def __init__(self,
                 number=None,
                 holder_name=None,
                 exp_month=None,
                 exp_year=None,
                 cvv=None,
                 billing_address=None,
                 brand=None,
                 billing_address_id=None,
                 metadata=None,
                 mtype='credit',
                 options=None,
                 private_label=None,
                 label=None,
                 holder_document=None,
                 id=None,
                 token=None):
        """Constructor for the CreateCardRequest class"""

        # Initialize members of the class
        self.number = number
        self.holder_name = holder_name
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.cvv = cvv
        self.billing_address = billing_address
        self.brand = brand
        self.billing_address_id = billing_address_id
        self.metadata = metadata
        self.mtype = mtype
        self.options = options
        self.holder_document = holder_document
        self.private_label = private_label
        self.label = label
        self.id = id
        self.token = token


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
        number = dictionary.get('number')
        holder_name = dictionary.get('holder_name')
        exp_month = dictionary.get('exp_month')
        exp_year = dictionary.get('exp_year')
        cvv = dictionary.get('cvv')
        billing_address = mundiapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        brand = dictionary.get('brand')
        billing_address_id = dictionary.get('billing_address_id')
        metadata = dictionary.get('metadata')
        mtype = dictionary.get("type") if dictionary.get("type") else 'credit'
        options = mundiapi.models.create_card_options_request.CreateCardOptionsRequest.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None
        private_label = dictionary.get('private_label')
        label = dictionary.get('label')
        holder_document = dictionary.get('holder_document')
        id = dictionary.get('id')
        token = dictionary.get('token')

        # Return an object of this model
        return cls(number,
                   holder_name,
                   exp_month,
                   exp_year,
                   cvv,
                   billing_address,
                   brand,
                   billing_address_id,
                   metadata,
                   mtype,
                   options,
                   private_label,
                   label,
                   holder_document,
                   id,
                   token)


