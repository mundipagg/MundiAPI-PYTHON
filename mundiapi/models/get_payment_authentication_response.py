# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.models.get_three_d_secure_response import GetThreeDSecureResponse


class GetPaymentAuthenticationResponse(object):

    """Implementation of the 'GetPaymentAuthenticationResponse' model.

    Payment Authentication response

    Attributes:
        mtype (string): TODO: type description here.
        threed_secure (GetThreeDSecureResponse): 3D-S payment authentication
            response

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "threed_secure": 'threed_secure'
    }

    def __init__(self,
                 mtype=None,
                 threed_secure=None):
        """Constructor for the GetPaymentAuthenticationResponse class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.threed_secure = threed_secure 

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

        mtype = dictionary.get("type") if dictionary.get("type") else None
        threed_secure = GetThreeDSecureResponse.from_dictionary(dictionary.get('threed_secure')) if dictionary.get('threed_secure') else None
        # Return an object of this model
        return cls(mtype,
                   threed_secure)
