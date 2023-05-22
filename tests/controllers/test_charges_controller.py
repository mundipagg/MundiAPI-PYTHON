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


class ChargesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ChargesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.charges

    # Lists all charges
    def test_test_get_charges(self):
        # Parameters for the API call
        page = None
        size = None
        code = None
        status = None
        payment_method = None
        customer_id = None
        order_id = None
        created_since = None
        created_until = None

        # Perform the API call through the SDK function
        result = self.controller.get_charges(page, size, code, status, payment_method, customer_id, order_id, created_since, created_until)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

