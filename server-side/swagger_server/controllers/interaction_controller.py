import connexion
import six

from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util

from .service.init_routine import *
from .service.calculation_routine import *
import os
import time
import threading
from flask import Response
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

    if os.getenv('CLIENT_B', None) is not None:
        if not SendToPreprocessorRoutineInst.gotMaskedInput:
            print("HI THERE")
            print(body.end_index)
            print(body.start_index)
            CalculationRoutineInst.maskedInputNeighbour = body.end_index
            CalculationRoutineInst.resultBitness = body.start_index
            result = SendToPreprocessorRoutineInst.inputNumber ^ SendToPreprocessorRoutineInst.inputMasks
            CalculationRoutineInst.maskedInputSelf = result
            SendToPreprocessorRoutineInst.gotMaskedInput = True
            #print("ClientB got masked input fro ClientA")
            #print(CalculationRoutineInst.maskedInputNeighbour)
            return [ExchangePayload(start_index=0, filled_links={}, end_index=result)], 200
    #print("storing neighbour data")
    CalculationRoutineInst.q.put(body.filled_links)
    #print("sending answer")
    filled = CalculationRoutineInst.answer.get()
    return [ExchangePayload(start_index=0, filled_links=filled, end_index=0)], 200


def hello():  # noqa: E501
    """hello message to neighbour

    Returns hello message # noqa: E501


    :rtype: InlineResponse200
    """

    if os.getenv('CLIENT_B', None) is not None:

        print("ClientB get hello message from ClientA")
        print("ClientB send message to Preprocessor")

        SendToPreprocessorRoutineInst.start()
        print("ClientB got reply from server and now starts calculation routine")

        def long_running_task(**kwargs):
            while not SendToPreprocessorRoutineInst.gotMaskedInput:
                continue
            CalculationRoutineInst.start(kwargs)

        thread = threading.Thread(target=long_running_task, kwargs={'config': SendToPreprocessorRoutineInst.config,
                                                                    'nodes': SendToPreprocessorRoutineInst.nodes
                                                                    })
        thread.start()

        return InlineResponse200(hello="Hello, OK"), 200

    return '', 204
