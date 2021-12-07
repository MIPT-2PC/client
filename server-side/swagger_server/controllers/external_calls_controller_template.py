import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server import util


def get_result():  # noqa: E501
    """returns calculated with 2PC result

    Returns the result of computation on config with A &amp; B inputs # noqa: E501


    :rtype: List[Answer]
    """
    return 'do some magic!'


def init(body=None):  # noqa: E501
    """Init call to start 2PC process.

    Consumes input data for this user and config location # noqa: E501

    :param body: calculated payload to send to neighbour in Decimal representation
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ExchangePayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
