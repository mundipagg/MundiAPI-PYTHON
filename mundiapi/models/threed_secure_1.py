# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ThreedSecure1(object):

    """Implementation of the 'ThreedSecure1' model.

    TODO: type model description here.

    Attributes:
        mpi (string): The MPI Vendor (MerchantPlugin)
        cavv (string): The Cardholder Authentication Verification value
        eci (string): The Electronic Commerce Indicator value
        transaction_id (string): The TransactionId value (XID)
        success_url (string): The success URL after the authentication
        ds_transaction_id (string): Directory Service Transaction Identifier
        version (string): ThreeDSecure Version

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mpi":'mpi',
        "cavv":'cavv',
        "eci":'eci',
        "transaction_id":'transaction_id',
        "success_url":'success_url',
        "ds_transaction_id":'ds_transaction_id',
        "version":'version'
    }

    def __init__(self,
                 mpi=None,
                 cavv=None,
                 eci=None,
                 transaction_id=None,
                 success_url=None,
                 ds_transaction_id=None,
                 version=None):
        """Constructor for the ThreedSecure1 class"""

        # Initialize members of the class
        self.mpi = mpi
        self.cavv = cavv
        self.eci = eci
        self.transaction_id = transaction_id
        self.success_url = success_url
        self.ds_transaction_id = ds_transaction_id
        self.version = version


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
        mpi = dictionary.get('mpi')
        cavv = dictionary.get('cavv')
        eci = dictionary.get('eci')
        transaction_id = dictionary.get('transaction_id')
        success_url = dictionary.get('success_url')
        ds_transaction_id = dictionary.get('ds_transaction_id')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(mpi,
                   cavv,
                   eci,
                   transaction_id,
                   success_url,
                   ds_transaction_id,
                   version)


