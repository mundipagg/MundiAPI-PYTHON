# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_phone_response
import mundiapi.models.address_1

class Submerchant(object):

    """Implementation of the 'Submerchant' model.

    TODO: type model description here.

    Attributes:
        payment_facilitator_code (string): Payment Facilitator Code
        code (string): Code
        name (string): Name
        merchant_category_code (string): Merchant Category Code
        document (string): Document number. Only numbers, no special
            characters.
        mtype (string): Document type. Can be either 'individual' or
            'company'
        phone (GetPhoneResponse): TODO: type description here.
        address (Address1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_facilitator_code":'payment_facilitator_code',
        "code":'code',
        "name":'name',
        "merchant_category_code":'merchant_category_code',
        "document":'document',
        "mtype":'type',
        "phone":'phone',
        "address":'address'
    }

    def __init__(self,
                 payment_facilitator_code=None,
                 code=None,
                 name=None,
                 merchant_category_code=None,
                 document=None,
                 mtype=None,
                 phone=None,
                 address=None):
        """Constructor for the Submerchant class"""

        # Initialize members of the class
        self.payment_facilitator_code = payment_facilitator_code
        self.code = code
        self.name = name
        self.merchant_category_code = merchant_category_code
        self.document = document
        self.mtype = mtype
        self.phone = phone
        self.address = address


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
        payment_facilitator_code = dictionary.get('payment_facilitator_code')
        code = dictionary.get('code')
        name = dictionary.get('name')
        merchant_category_code = dictionary.get('merchant_category_code')
        document = dictionary.get('document')
        mtype = dictionary.get('type')
        phone = mundiapi.models.get_phone_response.GetPhoneResponse.from_dictionary(dictionary.get('phone')) if dictionary.get('phone') else None
        address = mundiapi.models.address_1.Address1.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None

        # Return an object of this model
        return cls(payment_facilitator_code,
                   code,
                   name,
                   merchant_category_code,
                   document,
                   mtype,
                   phone,
                   address)


