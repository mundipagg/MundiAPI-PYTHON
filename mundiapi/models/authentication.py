# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.threed_secure

class Authentication(object):

    """Implementation of the 'Authentication' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        threed_secure (ThreedSecure): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "threed_secure":'threed_secure'
    }

    def __init__(self,
                 mtype=None,
                 threed_secure=None):
        """Constructor for the Authentication class"""

        # Initialize members of the class
        self.mtype = mtype
        self.threed_secure = threed_secure


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
        mtype = dictionary.get('type')
        threed_secure = mundiapi.models.threed_secure.ThreedSecure.from_dictionary(dictionary.get('threed_secure')) if dictionary.get('threed_secure') else None

        # Return an object of this model
        return cls(mtype,
                   threed_secure)


