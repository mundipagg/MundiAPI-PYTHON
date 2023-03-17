# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
import mundiapi.models.get_transaction_response
import mundiapi.models.invoice
import mundiapi.models.order
import mundiapi.models.customer

class ChargesMetadataResponse(object):

    """Implementation of the 'Charges Metadata Response' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        gateway_id (string): TODO: type description here.
        amount (int): TODO: type description here.
        status (string): TODO: type description here.
        currency (string): TODO: type description here.
        payment_method (string): TODO: type description here.
        due_at (datetime): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        last_transaction (GetTransactionResponse): TODO: type description
            here.
        invoice (Invoice): TODO: type description here.
        order (Order): TODO: type description here.
        customer (Customer): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        paid_at (datetime): TODO: type description here.
        canceled_at (datetime): TODO: type description here.
        canceled_amount (int): Canceled Amount
        paid_amount (int): Paid amount
        recurrency_cycle (string): Defines whether the card has been used one
            or more times.
        interest_and_fine_paid (int): interest and fine paid

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "code":'code',
        "gateway_id":'gateway_id',
        "amount":'amount',
        "status":'status',
        "currency":'currency',
        "payment_method":'payment_method',
        "due_at":'due_at',
        "created_at":'created_at',
        "updated_at":'updated_at',
        "metadata":'metadata',
        "canceled_amount":'canceled_amount',
        "paid_amount":'paid_amount',
        "last_transaction":'last_transaction',
        "invoice":'invoice',
        "order":'order',
        "customer":'customer',
        "paid_at":'paid_at',
        "canceled_at":'canceled_at',
        "recurrency_cycle":'recurrency_cycle',
        "interest_and_fine_paid":'interest_and_fine_paid'
    }

    def __init__(self,
                 id=None,
                 code=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 currency=None,
                 payment_method=None,
                 due_at=None,
                 created_at=None,
                 updated_at=None,
                 metadata=None,
                 canceled_amount=None,
                 paid_amount=None,
                 last_transaction=None,
                 invoice=None,
                 order=None,
                 customer=None,
                 paid_at=None,
                 canceled_at=None,
                 recurrency_cycle=None,
                 interest_and_fine_paid=None):
        """Constructor for the ChargesMetadataResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.gateway_id = gateway_id
        self.amount = amount
        self.status = status
        self.currency = currency
        self.payment_method = payment_method
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.last_transaction = last_transaction
        self.invoice = invoice
        self.order = order
        self.customer = customer
        self.metadata = metadata
        self.paid_at = APIHelper.RFC3339DateTime(paid_at) if paid_at else None
        self.canceled_at = APIHelper.RFC3339DateTime(canceled_at) if canceled_at else None
        self.canceled_amount = canceled_amount
        self.paid_amount = paid_amount
        self.recurrency_cycle = recurrency_cycle
        self.interest_and_fine_paid = interest_and_fine_paid


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
        gateway_id = dictionary.get('gateway_id')
        amount = dictionary.get('amount')
        status = dictionary.get('status')
        currency = dictionary.get('currency')
        payment_method = dictionary.get('payment_method')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        metadata = dictionary.get('metadata')
        canceled_amount = dictionary.get('canceled_amount')
        paid_amount = dictionary.get('paid_amount')
        last_transaction = mundiapi.models.get_transaction_response.GetTransactionResponse.from_dictionary(dictionary.get('last_transaction')) if dictionary.get('last_transaction') else None
        invoice = mundiapi.models.invoice.Invoice.from_dictionary(dictionary.get('invoice')) if dictionary.get('invoice') else None
        order = mundiapi.models.order.Order.from_dictionary(dictionary.get('order')) if dictionary.get('order') else None
        customer = mundiapi.models.customer.Customer.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        paid_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("paid_at")).datetime if dictionary.get("paid_at") else None
        canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None
        recurrency_cycle = dictionary.get('recurrency_cycle')
        interest_and_fine_paid = dictionary.get('interest_and_fine_paid')

        # Return an object of this model
        return cls(id,
                   code,
                   gateway_id,
                   amount,
                   status,
                   currency,
                   payment_method,
                   due_at,
                   created_at,
                   updated_at,
                   metadata,
                   canceled_amount,
                   paid_amount,
                   last_transaction,
                   invoice,
                   order,
                   customer,
                   paid_at,
                   canceled_at,
                   recurrency_cycle,
                   interest_and_fine_paid)


