# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
import mundiapi.models.get_order_item_response
import mundiapi.models.get_customer_response
import mundiapi.models.get_charge_response
import mundiapi.models.get_shipping_response
import mundiapi.models.get_checkout_payment_response
import mundiapi.models.get_location_response
import mundiapi.models.get_device_response

class GetOrderResponse(object):

    """Implementation of the 'GetOrderResponse' model.

    Response object for getting an Order

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        currency (string): TODO: type description here.
        items (list of GetOrderItemResponse): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        charges (list of GetChargeResponse): TODO: type description here.
        invoice_url (string): TODO: type description here.
        shipping (GetShippingResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        checkouts (list of GetCheckoutPaymentResponse): Checkout Payment
            Settings Response
        ip (string): Ip address
        session_id (string): Session id
        location (GetLocationResponse): Location
        device (GetDeviceResponse): Device's informations
        closed (bool): Indicates whether the order is closed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "code":'code',
        "currency":'currency',
        "items":'items',
        "status":'status',
        "created_at":'created_at',
        "updated_at":'updated_at',
        "charges":'charges',
        "invoice_url":'invoice_url',
        "shipping":'shipping',
        "metadata":'metadata',
        "closed":'closed',
        "customer":'customer',
        "checkouts":'checkouts',
        "ip":'ip',
        "session_id":'session_id',
        "location":'location',
        "device":'device'
    }

    def __init__(self,
                 id=None,
                 code=None,
                 currency=None,
                 items=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 charges=None,
                 invoice_url=None,
                 shipping=None,
                 metadata=None,
                 closed=None,
                 customer=None,
                 checkouts=None,
                 ip=None,
                 session_id=None,
                 location=None,
                 device=None):
        """Constructor for the GetOrderResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.currency = currency
        self.items = items
        self.customer = customer
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.charges = charges
        self.invoice_url = invoice_url
        self.shipping = shipping
        self.metadata = metadata
        self.checkouts = checkouts
        self.ip = ip
        self.session_id = session_id
        self.location = location
        self.device = device
        self.closed = closed


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
        id = dictionary.get('id')
        code = dictionary.get('code')
        currency = dictionary.get('currency')
        items = None
        if dictionary.get('items') != None:
            items = list()
            for structure in dictionary.get('items'):
                items.append(mundiapi.models.get_order_item_response.GetOrderItemResponse.from_dictionary(structure))
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        charges = None
        if dictionary.get('charges') != None:
            charges = list()
            for structure in dictionary.get('charges'):
                charges.append(mundiapi.models.get_charge_response.GetChargeResponse.from_dictionary(structure))
        invoice_url = dictionary.get('invoice_url')
        shipping = mundiapi.models.get_shipping_response.GetShippingResponse.from_dictionary(dictionary.get('shipping')) if dictionary.get('shipping') else None
        metadata = dictionary.get('metadata')
        closed = dictionary.get('closed')
        customer = mundiapi.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        checkouts = None
        if dictionary.get('checkouts') != None:
            checkouts = list()
            for structure in dictionary.get('checkouts'):
                checkouts.append(mundiapi.models.get_checkout_payment_response.GetCheckoutPaymentResponse.from_dictionary(structure))
        ip = dictionary.get('ip')
        session_id = dictionary.get('session_id')
        location = mundiapi.models.get_location_response.GetLocationResponse.from_dictionary(dictionary.get('location')) if dictionary.get('location') else None
        device = mundiapi.models.get_device_response.GetDeviceResponse.from_dictionary(dictionary.get('device')) if dictionary.get('device') else None

        # Return an object of this model
        return cls(id,
                   code,
                   currency,
                   items,
                   status,
                   created_at,
                   updated_at,
                   charges,
                   invoice_url,
                   shipping,
                   metadata,
                   closed,
                   customer,
                   checkouts,
                   ip,
                   session_id,
                   location,
                   device)


