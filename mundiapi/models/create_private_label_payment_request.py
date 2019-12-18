# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_card_request

class CreatePrivateLabelPaymentRequest(object):

    """Implementation of the 'CreatePrivateLabelPaymentRequest' model.

    The settings for creating a private label payment

    Attributes:
        installments (int): Number of installments
        statement_descriptor (string): The text that will be shown on the
            private label's statement
        card (CreateCardRequest): Card data
        card_id (string): The Card id
        card_token (string): TODO: type description here.
        recurrence (bool): Indicates a recurrence
        capture (bool): Indicates if the operation should be only
            authorization or auth and capture.
        extended_limit_enabled (bool): Indicates whether the extended label
            (private label) is enabled
        extended_limit_code (string): Extended Limit Code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "installments":'installments',
        "statement_descriptor":'statement_descriptor',
        "card":'card',
        "card_id":'card_id',
        "card_token":'card_token',
        "recurrence":'recurrence',
        "capture":'capture',
        "extended_limit_enabled":'extended_limit_enabled',
        "extended_limit_code":'extended_limit_code'
    }

    def __init__(self,
                 installments=1,
                 statement_descriptor=None,
                 card=None,
                 card_id=None,
                 card_token=None,
                 recurrence=None,
                 capture=True,
                 extended_limit_enabled=None,
                 extended_limit_code=None):
        """Constructor for the CreatePrivateLabelPaymentRequest class"""

        # Initialize members of the class
        self.installments = installments
        self.statement_descriptor = statement_descriptor
        self.card = card
        self.card_id = card_id
        self.card_token = card_token
        self.recurrence = recurrence
        self.capture = capture
        self.extended_limit_enabled = extended_limit_enabled
        self.extended_limit_code = extended_limit_code


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
        installments = dictionary.get("installments") if dictionary.get("installments") else 1
        statement_descriptor = dictionary.get('statement_descriptor')
        card = mundiapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        card_id = dictionary.get('card_id')
        card_token = dictionary.get('card_token')
        recurrence = dictionary.get('recurrence')
        capture = dictionary.get("capture") if dictionary.get("capture") else True
        extended_limit_enabled = dictionary.get('extended_limit_enabled')
        extended_limit_code = dictionary.get('extended_limit_code')

        # Return an object of this model
        return cls(installments,
                   statement_descriptor,
                   card,
                   card_id,
                   card_token,
                   recurrence,
                   capture,
                   extended_limit_enabled,
                   extended_limit_code)


