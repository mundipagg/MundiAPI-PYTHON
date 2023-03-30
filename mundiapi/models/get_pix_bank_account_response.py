# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GetPixBankAccountResponse(object):

    """Implementation of the 'GetPixBankAccountResponse' model.

    Payer's bank details.

    Attributes:
        bank_name (string): TODO: type description here.
        ispb (string): TODO: type description here.
        branch_code (string): TODO: type description here.
        account_number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank_name": 'bank_name',
        "ispb": 'ispb',
        "branch_code": 'branch_code',
        "account_number": 'account_number'
    }

    _nullables = [
        'bank_name',
        'ispb',
        'branch_code',
        'account_number',
    ]

    def __init__(self,
                 bank_name=None,
                 ispb=None,
                 branch_code=None,
                 account_number=None):
        """Constructor for the GetPixBankAccountResponse class"""

        # Initialize members of the class
        self.bank_name = bank_name 
        self.ispb = ispb 
        self.branch_code = branch_code 
        self.account_number = account_number 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        bank_name = dictionary.get("bank_name") if dictionary.get("bank_name") else None
        ispb = dictionary.get("ispb") if dictionary.get("ispb") else None
        branch_code = dictionary.get("branch_code") if dictionary.get("branch_code") else None
        account_number = dictionary.get("account_number") if dictionary.get("account_number") else None
        # Return an object of this model
        return cls(bank_name,
                   ispb,
                   branch_code,
                   account_number)
