import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.init import Init  # noqa: E501
from swagger_server.models.exchange_payload import ExchangePayload  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from .service.config_uploader import ConfigUploader
from .service.init_routine import *
from .service.calculation_routine import *
import time
import os
import copy

import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from flask import Response


def get_result():  # noqa: E501
    """returns calculated with 2PC result

    Returns the result of computation on config with A &amp; B inputs # noqa: E501


    :rtype: List[Answer]
    """
    return [Answer(result=CalculationRoutineInst.list.pop())], 200


def init(input_number=None, config=None):  # noqa: E501
    """Init call to start 2PC process.

    Consumes input data for this user and config location # noqa: E501

    :param input_number:
    :type input_number: int
    :param config:
    :type config: strstr

    :rtype: None
    """

    if os.getenv('CLIENT_A', None) is not None:
        SendToPreprocessorRoutineInst.inputNumber = int(connexion.request.form.get("inputNumber"))

        file = connexion.request.files['config']
        file.save('./config.scheme')

        print("ClientA started processing config file")
        ConfigUploaderInst = ConfigUploader('./config.scheme')
        print("ClientA processed config file")

        print("ClientA is ready to send config to server")
        SendToPreprocessorRoutineInst.resultBitness = copy.deepcopy(ConfigUploaderInst.dataToTransfer['config']['resultBitness'])
        print(SendToPreprocessorRoutineInst.resultBitness)
        SendToPreprocessorRoutineInst.start(ConfigUploaderInst.dataToTransfer)
        print("ClientA should have preprocessed table here and begin some computations on them")

        print("ClientA send hello message to ClientB")
        api_instance = swagger_client.InteractionApi()
        try:
            api_response = api_instance.hello()
            print("ClientA got message from ClientB:")
            print(api_response)
        except ApiException as e:
            print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)

        '''
        inputMasks = 12:
        00000000.00000000.00000000.00001100
        
        inputNumber = 54:
        00000000.00000000.00000000.00110110
        
        maskedInput = inputMasks ^ inputNumber = 58:
        00000000.00000000.00000000.00111010
        '''
        maskedInput = SendToPreprocessorRoutineInst.inputMasks ^ SendToPreprocessorRoutineInst.inputNumber

        time.sleep(2)  # чисто чтобы удостовериться, что клиент В успел получить данные от препроцессора
        body = ExchangePayload(start_index=int(SendToPreprocessorRoutineInst.resultBitness), filled_links={}, end_index=maskedInput)
        print("ClientA share itself masked input to ClientB")
        try:
            api_response = api_instance.exchange_out(body=body)
            CalculationRoutineInst.maskedInputNeighbour = api_response[0].end_index
            CalculationRoutineInst.maskedInputSelf = maskedInput
            CalculationRoutineInst.resultBitness = SendToPreprocessorRoutineInst.resultBitness
            print("ClientA got masked input from ClientB:")
            print(api_response)
        except ApiException as e:
            print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)

        def generate():
            yield "Success initiation. Results will be available with /getResult request"
            CalculationRoutineInst.start({'config': SendToPreprocessorRoutineInst.config,
                                          'nodes': SendToPreprocessorRoutineInst.nodes
                                          })
            yield ''
        return Response(generate(), mimetype='application/json'), 200



    print("ClientB tried to call init()")
    return "This is not Adversary (ClientA)", 500
