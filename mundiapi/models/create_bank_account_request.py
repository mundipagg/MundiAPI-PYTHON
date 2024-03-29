# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateBankAccountRequest(object):

    """Implementation of the 'CreateBankAccountRequest' model.

    Request for creating a bank account

    Attributes:
        holder_name (string): Bank account holder name
        holder_type (string): Bank account holder type
        holder_document (string): Bank account holder document
        bank (string): Bank
        branch_number (string): Branch number
        branch_check_digit (string): Branch check digit
        account_number (string): Account number
        account_check_digit (string): Account check digit
        mtype (string): Bank account type
        metadata (dict<object, string>): Metadata
        pix_key (string): Pix key

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "holder_name":'holder_name',
        "holder_type":'holder_type',
        "holder_document":'holder_document',
        "bank":'bank',
        "branch_number":'branch_number',
        "branch_check_digit":'branch_check_digit',
        "account_number":'account_number',
        "account_check_digit":'account_check_digit',
        "mtype":'type',
        "metadata":'metadata',
        "pix_key":'pix_key'
    }

    def __init__(self,
                 holder_name=None,
                 holder_type=None,
                 holder_document=None,
                 bank=None,
                 branch_number=None,
                 branch_check_digit=None,
                 account_number=None,
                 account_check_digit=None,
                 mtype=None,
                 metadata=None,
                 pix_key=None):
        """Constructor for the CreateBankAccountRequest class"""

        # Initialize members of the class
        self.holder_name = holder_name
        self.holder_type = holder_type
        self.holder_document = holder_document
        self.bank = bank
        self.branch_number = branch_number
        self.branch_check_digit = branch_check_digit
        self.account_number = account_number
        self.account_check_digit = account_check_digit
        self.mtype = mtype
        self.metadata = metadata
        self.pix_key = pix_key


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
        holder_name = dictionary.get('holder_name')
        holder_type = dictionary.get('holder_type')
        holder_document = dictionary.get('holder_document')
        bank = dictionary.get('bank')
        branch_number = dictionary.get('branch_number')
        branch_check_digit = dictionary.get('branch_check_digit')
        account_number = dictionary.get('account_number')
        account_check_digit = dictionary.get('account_check_digit')
        mtype = dictionary.get('type')
        metadata = dictionary.get('metadata')
        pix_key = dictionary.get('pix_key')

        # Return an object of this model
        return cls(holder_name,
                   holder_type,
                   holder_document,
                   bank,
                   branch_number,
                   branch_check_digit,
                   account_number,
                   account_check_digit,
                   mtype,
                   metadata,
                   pix_key)


