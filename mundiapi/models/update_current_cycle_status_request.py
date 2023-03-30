# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateCurrentCycleStatusRequest(object):

    """Implementation of the 'UpdateCurrentCycleStatusRequest' model.

    TODO: type model description here.

    Attributes:
        status (string): Status

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status'
    }

    def __init__(self,
                 status=None):
        """Constructor for the UpdateCurrentCycleStatusRequest class"""

        # Initialize members of the class
        self.status = status 

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

        status = dictionary.get("status") if dictionary.get("status") else None
        # Return an object of this model
        return cls(status)
