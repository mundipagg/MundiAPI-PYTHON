# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.api_helper import APIHelper
from mundiapi.models.get_period_response import GetPeriodResponse
from mundiapi.models.list_usages_details_response import ListUsagesDetailsResponse


class GetUsagesDetailsResponse(object):

    """Implementation of the 'GetUsagesDetailsResponse' model.

    TODO: type model description here.

    Attributes:
        subscription_id (string): Subscription Identifier
        total_amount (int): Current Invoice Amount
        period (GetPeriodResponse): Period Details
        usages (ListUsagesDetailsResponse): Usages Details
        total_discount (int): Total discounted value
        total_increment (int): Total inremented value

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": 'subscription_id',
        "total_amount": 'total_amount',
        "usages": 'Usages',
        "period": 'Period',
        "total_discount": 'total_discount',
        "total_increment": 'total_increment'
    }

    _optionals = [
        'period',
        'total_discount',
        'total_increment',
    ]

    def __init__(self,
                 subscription_id=None,
                 total_amount=None,
                 usages=None,
                 period=APIHelper.SKIP,
                 total_discount=APIHelper.SKIP,
                 total_increment=APIHelper.SKIP):
        """Constructor for the GetUsagesDetailsResponse class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        self.total_amount = total_amount 
        if period is not APIHelper.SKIP:
            self.period = period 
        self.usages = usages 
        if total_discount is not APIHelper.SKIP:
            self.total_discount = total_discount 
        if total_increment is not APIHelper.SKIP:
            self.total_increment = total_increment 

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

        subscription_id = dictionary.get("subscription_id") if dictionary.get("subscription_id") else None
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else None
        usages = ListUsagesDetailsResponse.from_dictionary(dictionary.get('Usages')) if dictionary.get('Usages') else None
        period = GetPeriodResponse.from_dictionary(dictionary.get('Period')) if 'Period' in dictionary.keys() else APIHelper.SKIP
        total_discount = dictionary.get("total_discount") if dictionary.get("total_discount") else APIHelper.SKIP
        total_increment = dictionary.get("total_increment") if dictionary.get("total_increment") else APIHelper.SKIP
        # Return an object of this model
        return cls(subscription_id,
                   total_amount,
                   usages,
                   period,
                   total_discount,
                   total_increment)
