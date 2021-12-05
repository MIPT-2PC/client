# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.models.table import Table  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInteractionController(BaseTestCase):
    """InteractionController integration test stubs"""

    def test_exchange_out(self):
        """Test case for exchange_out

        Exchange calculated nodes with self table from Nth layer
        """
        body = ExchangePayload()
        response = self.client.open(
            '/MIPT-2PC/user/1.0.0/exchangeOut',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hello(self):
        """Test case for hello

        hello message to get preprocessed data
        """
        response = self.client.open(
            '/MIPT-2PC/user/1.0.0/hello',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
