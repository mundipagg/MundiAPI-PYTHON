# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from mundiapi.api_helper import APIHelper


class InvoicesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(InvoicesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.invoices

    # Gets all invoices
    def test_test_get_invoices(self):
        # Parameters for the API call
        page = None
        size = None
        code = None
        customer_id = None
        subscription_id = None
        created_since = None
        created_until = None
        status = None
        due_since = None
        due_until = None
        customer_document = None

        # Perform the API call through the SDK function
        result = self.controller.get_invoices(page, size, code, customer_id, subscription_id, created_since, created_until, status, due_since, due_until, customer_document)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


