# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_emv_data_dukpt_decrypt_request
import mundiapi.models.create_emv_data_tlv_decrypt_request

class CreateEmvDataDecryptRequest(object):

    """Implementation of the 'CreateEmvDataDecryptRequest' model.

    TODO: type model description here.

    Attributes:
        cipher (string): Emv Decrypt cipher type
        dukpt (CreateEmvDataDukptDecryptRequest): TODO: type description
            here.
        tags (list of CreateEmvDataTlvDecryptRequest): Encrypted tags list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cipher":'cipher',
        "tags":'tags',
        "dukpt":'dukpt'
    }

    def __init__(self,
                 cipher=None,
                 tags=None,
                 dukpt=None):
        """Constructor for the CreateEmvDataDecryptRequest class"""

        # Initialize members of the class
        self.cipher = cipher
        self.dukpt = dukpt
        self.tags = tags


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
        cipher = dictionary.get('cipher')
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(mundiapi.models.create_emv_data_tlv_decrypt_request.CreateEmvDataTlvDecryptRequest.from_dictionary(structure))
        dukpt = mundiapi.models.create_emv_data_dukpt_decrypt_request.CreateEmvDataDukptDecryptRequest.from_dictionary(dictionary.get('dukpt')) if dictionary.get('dukpt') else None

        # Return an object of this model
        return cls(cipher,
                   tags,
                   dukpt)


