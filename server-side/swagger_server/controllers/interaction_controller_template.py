import connexion
import six

from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def exchange_out(body=None):  # noqa: E501
    """Exchange calculated nodes with self table from Nth layer

    Exchange calculated nodes with self table from Nth layer # noqa: E501

    :param body: calculated payload to send to neighbour in Decimal representation
    :type body: dict | bytes

    :rtype: List[ExchangePayload]
    """
    if connexion.request.is_json:
        body = ExchangePayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hello():  # noqa: E501
    """hello message to neighbour

    Returns hello message # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'
