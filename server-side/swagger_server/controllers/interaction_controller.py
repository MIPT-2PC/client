import connexion
import six

from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util

from .service.init_routine import *
from .service.calculation_routine import *
import os
from threading import Thread
from queue import Queue


def exchange_out(body=None):  # noqa: E501
    """Exchange calculated nodes with self table from Nth layer

    Exchange calculated nodes with self table from Nth layer # noqa: E501

    :param body: calculated payload to send to neighbour in Decimal representation
    :type body: dict | bytes

    :rtype: List[ExchangePayload]
    """
    if connexion.request.is_json:
        body = ExchangePayload.from_dict(connexion.request.get_json())  # noqa: E501
    CalculationRoutineInst.q.put((body.start_index, body.out_dec_number))
    position, result = CalculationRoutineInst.q.get()
    return [ExchangePayload(start_index=position, out_dec_number=result)], 200


def hello():  # noqa: E501
    """hello message to neighbour

    Returns hello message # noqa: E501


    :rtype: InlineResponse200
    """

    if os.getenv('CLIENT_B', None) is not None:
        SendToPreprocessorRoutineInst = SendToPreprocessorRoutine()
        SendToPreprocessorRoutineInst.start()

        CalculationRoutineInst = CalculationRoutine()
        CalculationRoutineInst.start(SendToPreprocessorRoutineInst.ClientB_Response)

        return InlineResponse200(hello="Hello, OK"), 200
    return '', 204
