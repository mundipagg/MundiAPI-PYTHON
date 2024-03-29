# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Header(object):

    """Implementation of the 'Header' model.

    TODO: type model description here.

    Attributes:
        public_key_hash (string): SHA–256 hash, Base64 string codified
        ephemeral_public_key (string): X.509 encoded key bytes, Base64 encoded
            as a string
        transaction_id (string): Transaction identifier, generated on Device

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ephemeral_public_key":'ephemeral_public_key',
        "public_key_hash":'public_key_hash',
        "transaction_id":'transaction_id'
    }

    def __init__(self,
                 ephemeral_public_key=None,
                 public_key_hash=None,
                 transaction_id=None):
        """Constructor for the Header class"""

        # Initialize members of the class
        self.public_key_hash = public_key_hash
        self.ephemeral_public_key = ephemeral_public_key
        self.transaction_id = transaction_id


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
        ephemeral_public_key = dictionary.get('ephemeral_public_key')
        public_key_hash = dictionary.get('public_key_hash')
        transaction_id = dictionary.get('transaction_id')

        # Return an object of this model
        return cls(ephemeral_public_key,
                   public_key_hash,
                   transaction_id)


