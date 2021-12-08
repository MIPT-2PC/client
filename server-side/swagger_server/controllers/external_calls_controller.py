import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.init import Init  # noqa: E501
from swagger_server import util
from .service.config_uploader import ConfigUploader
from .service.init_routine import *
from .service.calculation_routine import *
import os

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
        print(connexion.request.form.get("inputNumber"))

        file = connexion.request.files['config']
        file.save('./config.scheme')

        print("ClientA started processing config file")

        ConfigUploaderInst = ConfigUploader('./config.scheme')

        print("ClientA processed config file")

        print("ClientA is ready to send config to server")


        SendToPreprocessorRoutineInst = SendToPreprocessorRoutine()
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

        def generate():
            yield "Success initiation. Results will be available with /getResult request"
            CalculationRoutineInst.start(SendToPreprocessorRoutineInst.ClientA_Response)
            yield ''
        return Response(generate(), mimetype='application/json'), 200

    print("ClientB tried to call init()")
    return "This is not Adversary (ClientA)", 500
