# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_card_request
import mundiapi.models.create_payment_authentication_request
import mundiapi.models.create_card_payment_contactless_request

class CreateDebitCardPaymentRequest(object):

    """Implementation of the 'CreateDebitCardPaymentRequest' model.

    The settings for creating a debit card payment

    Attributes:
        statement_descriptor (string): The text that will be shown on the
            debit card's statement
        card (CreateCardRequest): Debit card data
        card_id (string): The debit card id
        card_token (string): The debit card token
        recurrence (bool): Indicates a recurrence
        authentication (CreatePaymentAuthenticationRequest): The payment
            authentication request
        token (CreateCardPaymentContactlessRequest): The Debit card payment
            token request
        recurrency_cycle (string): Defines whether the card has been used one
            or more times.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor":'statement_descriptor',
        "card":'card',
        "card_id":'card_id',
        "card_token":'card_token',
        "recurrence":'recurrence',
        "authentication":'authentication',
        "token":'token',
        "recurrency_cycle":'recurrency_cycle'
    }

    def __init__(self,
                 statement_descriptor=None,
                 card=None,
                 card_id=None,
                 card_token=None,
                 recurrence=None,
                 authentication=None,
                 token=None,
                 recurrency_cycle=None):
        """Constructor for the CreateDebitCardPaymentRequest class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.card = card
        self.card_id = card_id
        self.card_token = card_token
        self.recurrence = recurrence
        self.authentication = authentication
        self.token = token
        self.recurrency_cycle = recurrency_cycle


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
        statement_descriptor = dictionary.get('statement_descriptor')
        card = mundiapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        card_id = dictionary.get('card_id')
        card_token = dictionary.get('card_token')
        recurrence = dictionary.get('recurrence')
        authentication = mundiapi.models.create_payment_authentication_request.CreatePaymentAuthenticationRequest.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        token = mundiapi.models.create_card_payment_contactless_request.CreateCardPaymentContactlessRequest.from_dictionary(dictionary.get('token')) if dictionary.get('token') else None
        recurrency_cycle = dictionary.get('recurrency_cycle')

        # Return an object of this model
        return cls(statement_descriptor,
                   card,
                   card_id,
                   card_token,
                   recurrence,
                   authentication,
                   token,
                   recurrency_cycle)


