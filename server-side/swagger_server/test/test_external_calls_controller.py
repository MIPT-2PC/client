# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExternalCallsController(BaseTestCase):
    """ExternalCallsController integration test stubs"""

    def test_get_result(self):
        """Test case for get_result

        returns calculated with 2PC result
        """
        response = self.client.open(
            '/MIPT-2PC/user/1.0.0/getResult',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_init(self):
        """Test case for init

        Init call to start 2PC process.
        """
        body = ExchangePayload()
        response = self.client.open(
            '/MIPT-2PC/user/1.0.0/init',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
