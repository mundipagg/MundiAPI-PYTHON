# -*- coding: utf-8 -*-

"""
    mundiapi.models.create_checkout_card_payment_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_checkout_card_installment_option_request

class CreateCheckoutCardPaymentRequest(object):

    """Implementation of the 'CreateCheckoutCardPaymentRequest' model.

    Checkout card payment request

    Attributes:
        statement_descriptor (string): Card invoice text descriptor
        installments (list of CreateCheckoutCardInstallmentOptionRequest):
            Payment installment options

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor" : "statement_descriptor",
        "installments" : "installments"
    }

    def __init__(self,
                 statement_descriptor=None,
                 installments=None):
        """Constructor for the CreateCheckoutCardPaymentRequest class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.installments = installments


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
        statement_descriptor = dictionary.get("statement_descriptor")
        installments = None
        if dictionary.get("installments") != None:
            installments = list()
            for structure in dictionary.get("installments"):
                installments.append(mundiapi.models.create_checkout_card_installment_option_request.CreateCheckoutCardInstallmentOptionRequest.from_dictionary(structure))

        # Return an object of this model
        return cls(statement_descriptor,
                   installments)


