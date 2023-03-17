# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_order_item_request
import mundiapi.models.customer_8
import mundiapi.models.create_payment_request
import mundiapi.models.shipping_3
import mundiapi.models.location
import mundiapi.models.device_1
import mundiapi.models.create_antifraud_request
import mundiapi.models.submerchant

class CreateOrderRequest(object):

    """Implementation of the 'CreateOrderRequest' model.

    Request for creating an order

    Attributes:
        items (list of CreateOrderItemRequest): Items
        customer (Customer8): TODO: type description here.
        payments (list of CreatePaymentRequest): Payment data
        code (string): The order code
        customer_id (string): The customer id
        shipping (Shipping3): TODO: type description here.
        metadata (dict<object, string>): Metadata
        antifraud_enabled (bool): Defines whether the order will go through
            anti-fraud
        ip (string): Ip address
        session_id (string): Session id
        location (Location): TODO: type description here.
        device (Device1): TODO: type description here.
        closed (bool): TODO: type description here.
        currency (string): Currency
        antifraud (CreateAntifraudRequest): TODO: type description here.
        submerchant (Submerchant): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items":'items',
        "customer":'customer',
        "payments":'payments',
        "code":'code',
        "customer_id":'customer_id',
        "metadata":'metadata',
        "closed":'closed',
        "shipping":'shipping',
        "antifraud_enabled":'antifraud_enabled',
        "ip":'ip',
        "session_id":'session_id',
        "location":'location',
        "device":'device',
        "currency":'currency',
        "antifraud":'antifraud',
        "submerchant":'submerchant'
    }

    def __init__(self,
                 items=None,
                 customer=None,
                 payments=None,
                 code=None,
                 customer_id=None,
                 metadata=None,
                 closed=None,
                 shipping=None,
                 antifraud_enabled=None,
                 ip=None,
                 session_id=None,
                 location=None,
                 device=None,
                 currency=None,
                 antifraud=None,
                 submerchant=None):
        """Constructor for the CreateOrderRequest class"""

        # Initialize members of the class
        self.items = items
        self.customer = customer
        self.payments = payments
        self.code = code
        self.customer_id = customer_id
        self.shipping = shipping
        self.metadata = metadata
        self.antifraud_enabled = antifraud_enabled
        self.ip = ip
        self.session_id = session_id
        self.location = location
        self.device = device
        self.closed = closed
        self.currency = currency
        self.antifraud = antifraud
        self.submerchant = submerchant


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
        items = None
        if dictionary.get('items') != None:
            items = list()
            for structure in dictionary.get('items'):
                items.append(mundiapi.models.create_order_item_request.CreateOrderItemRequest.from_dictionary(structure))
        customer = mundiapi.models.customer_8.Customer8.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        payments = None
        if dictionary.get('payments') != None:
            payments = list()
            for structure in dictionary.get('payments'):
                payments.append(mundiapi.models.create_payment_request.CreatePaymentRequest.from_dictionary(structure))
        code = dictionary.get('code')
        customer_id = dictionary.get('customer_id')
        metadata = dictionary.get('metadata')
        closed = dictionary.get('closed')
        shipping = mundiapi.models.shipping_3.Shipping3.from_dictionary(dictionary.get('shipping')) if dictionary.get('shipping') else None
        antifraud_enabled = dictionary.get('antifraud_enabled')
        ip = dictionary.get('ip')
        session_id = dictionary.get('session_id')
        location = mundiapi.models.location.Location.from_dictionary(dictionary.get('location')) if dictionary.get('location') else None
        device = mundiapi.models.device_1.Device1.from_dictionary(dictionary.get('device')) if dictionary.get('device') else None
        currency = dictionary.get('currency')
        antifraud = mundiapi.models.create_antifraud_request.CreateAntifraudRequest.from_dictionary(dictionary.get('antifraud')) if dictionary.get('antifraud') else None
        submerchant = mundiapi.models.submerchant.Submerchant.from_dictionary(dictionary.get('submerchant')) if dictionary.get('submerchant') else None

        # Return an object of this model
        return cls(items,
                   customer,
                   payments,
                   code,
                   customer_id,
                   metadata,
                   closed,
                   shipping,
                   antifraud_enabled,
                   ip,
                   session_id,
                   location,
                   device,
                   currency,
                   antifraud,
                   submerchant)


