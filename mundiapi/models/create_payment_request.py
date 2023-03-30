# -*- coding: utf-8 -*-

"""
mundiapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mundiapi.api_helper import APIHelper
from mundiapi.models.create_bank_transfer_payment_request import CreateBankTransferPaymentRequest
from mundiapi.models.create_boleto_payment_request import CreateBoletoPaymentRequest
from mundiapi.models.create_cash_payment_request import CreateCashPaymentRequest
from mundiapi.models.create_checkout_payment_request import CreateCheckoutPaymentRequest
from mundiapi.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest
from mundiapi.models.create_customer_request import CreateCustomerRequest
from mundiapi.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest
from mundiapi.models.create_pix_payment_request import CreatePixPaymentRequest
from mundiapi.models.create_private_label_payment_request import CreatePrivateLabelPaymentRequest
from mundiapi.models.create_split_request import CreateSplitRequest
from mundiapi.models.create_voucher_payment_request import CreateVoucherPaymentRequest


class CreatePaymentRequest(object):

    """Implementation of the 'CreatePaymentRequest' model.

    Payment data

    Attributes:
        payment_method (string): Payment method
        credit_card (CreateCreditCardPaymentRequest): Settings for credit card
            payment
        debit_card (CreateDebitCardPaymentRequest): Settings for debit card
            payment
        boleto (CreateBoletoPaymentRequest): Settings for boleto payment
        currency (string): Currency. Must be informed using 3 characters
        voucher (CreateVoucherPaymentRequest): Settings for voucher payment
        split (list of CreateSplitRequest): Splits
        bank_transfer (CreateBankTransferPaymentRequest): Settings for bank
            transfer payment
        gateway_affiliation_id (string): Gateway affiliation code
        amount (int): The amount of the payment, in cents
        checkout (CreateCheckoutPaymentRequest): Settings for checkout
            payment
        customer_id (string): Customer Id
        customer (CreateCustomerRequest): Customer
        metadata (dict): Metadata
        cash (CreateCashPaymentRequest): Settings for cash payment
        private_label (CreatePrivateLabelPaymentRequest): Settings for private
            label payment
        pix (CreatePixPaymentRequest): Settings for pix payment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_method": 'payment_method',
        "private_label": 'private_label',
        "credit_card": 'credit_card',
        "debit_card": 'debit_card',
        "boleto": 'boleto',
        "currency": 'currency',
        "voucher": 'voucher',
        "split": 'split',
        "bank_transfer": 'bank_transfer',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "amount": 'amount',
        "checkout": 'checkout',
        "customer_id": 'customer_id',
        "customer": 'customer',
        "metadata": 'metadata',
        "cash": 'cash',
        "pix": 'pix'
    }

    _optionals = [
        'credit_card',
        'debit_card',
        'boleto',
        'currency',
        'voucher',
        'split',
        'bank_transfer',
        'gateway_affiliation_id',
        'amount',
        'checkout',
        'customer_id',
        'customer',
        'metadata',
        'cash',
        'pix',
    ]

    def __init__(self,
                 payment_method=None,
                 private_label=None,
                 credit_card=APIHelper.SKIP,
                 debit_card=APIHelper.SKIP,
                 boleto=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 voucher=APIHelper.SKIP,
                 split=APIHelper.SKIP,
                 bank_transfer=APIHelper.SKIP,
                 gateway_affiliation_id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 checkout=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 cash=APIHelper.SKIP,
                 pix=APIHelper.SKIP):
        """Constructor for the CreatePaymentRequest class"""

        # Initialize members of the class
        self.payment_method = payment_method 
        if credit_card is not APIHelper.SKIP:
            self.credit_card = credit_card 
        if debit_card is not APIHelper.SKIP:
            self.debit_card = debit_card 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if voucher is not APIHelper.SKIP:
            self.voucher = voucher 
        if split is not APIHelper.SKIP:
            self.split = split 
        if bank_transfer is not APIHelper.SKIP:
            self.bank_transfer = bank_transfer 
        if gateway_affiliation_id is not APIHelper.SKIP:
            self.gateway_affiliation_id = gateway_affiliation_id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if checkout is not APIHelper.SKIP:
            self.checkout = checkout 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if cash is not APIHelper.SKIP:
            self.cash = cash 
        self.private_label = private_label 
        if pix is not APIHelper.SKIP:
            self.pix = pix 

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

        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        private_label = CreatePrivateLabelPaymentRequest.from_dictionary(dictionary.get('private_label')) if dictionary.get('private_label') else None
        credit_card = CreateCreditCardPaymentRequest.from_dictionary(dictionary.get('credit_card')) if 'credit_card' in dictionary.keys() else APIHelper.SKIP
        debit_card = CreateDebitCardPaymentRequest.from_dictionary(dictionary.get('debit_card')) if 'debit_card' in dictionary.keys() else APIHelper.SKIP
        boleto = CreateBoletoPaymentRequest.from_dictionary(dictionary.get('boleto')) if 'boleto' in dictionary.keys() else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        voucher = CreateVoucherPaymentRequest.from_dictionary(dictionary.get('voucher')) if 'voucher' in dictionary.keys() else APIHelper.SKIP
        split = None
        if dictionary.get('split') is not None:
            split = [CreateSplitRequest.from_dictionary(x) for x in dictionary.get('split')]
        else:
            split = APIHelper.SKIP
        bank_transfer = CreateBankTransferPaymentRequest.from_dictionary(dictionary.get('bank_transfer')) if 'bank_transfer' in dictionary.keys() else APIHelper.SKIP
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id") if dictionary.get("gateway_affiliation_id") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        checkout = CreateCheckoutPaymentRequest.from_dictionary(dictionary.get('checkout')) if 'checkout' in dictionary.keys() else APIHelper.SKIP
        customer_id = dictionary.get("customer_id") if dictionary.get("customer_id") else APIHelper.SKIP
        customer = CreateCustomerRequest.from_dictionary(dictionary.get('customer')) if 'customer' in dictionary.keys() else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        cash = CreateCashPaymentRequest.from_dictionary(dictionary.get('cash')) if 'cash' in dictionary.keys() else APIHelper.SKIP
        pix = CreatePixPaymentRequest.from_dictionary(dictionary.get('pix')) if 'pix' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment_method,
                   private_label,
                   credit_card,
                   debit_card,
                   boleto,
                   currency,
                   voucher,
                   split,
                   bank_transfer,
                   gateway_affiliation_id,
                   amount,
                   checkout,
                   customer_id,
                   customer,
                   metadata,
                   cash,
                   pix)
