# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.models.get_split_response import GetSplitResponse


class GetSubscriptionSplitResponse(object):

    """Implementation of the 'GetSubscriptionSplitResponse' model.

    Subscription's split response

    Attributes:
        enabled (bool): Defines if the split is enabled
        rules (list of GetSplitResponse): Split

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "rules": 'rules'
    }

    def __init__(self,
                 enabled=None,
                 rules=None):
        """Constructor for the GetSubscriptionSplitResponse class"""

        # Initialize members of the class
        self.enabled = enabled 
        self.rules = rules 

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

        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else None
        rules = None
        if dictionary.get('rules') is not None:
            rules = [GetSplitResponse.from_dictionary(x) for x in dictionary.get('rules')]
        # Return an object of this model
        return cls(enabled,
                   rules)
