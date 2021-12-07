import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.init import Init  # noqa: E501
from swagger_server import util
from .service.config_uploader import ConfigUploader
from .service.init_routine import *
import os

import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


def get_result():  # noqa: E501
    """returns calculated with 2PC result

    Returns the result of computation on config with A &amp; B inputs # noqa: E501


    :rtype: List[Answer]
    """
    return 'do some magic!'


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
        api_instance = swagger_client.InteractionApi()
        try:
            # returns calculated with 2PC result
            api_response = api_instance.hello()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExternalCallsApi->get_result: %s\n" % e)



        print(connexion.request.form.get("inputNumber"))

        for i in connexion.request.files:
            print(i)

        file = connexion.request.files['config']
        file.save('./config.scheme')

        with open('./config.scheme') as file:
            for line in file:
                print(line)

        ConfigUploaderInst = ConfigUploader('./config.scheme')

        SendToPreprocessorRoutineInst = SendToPreprocessorRoutine()
        SendToPreprocessorRoutineInst.start(ConfigUploaderInst.dataToTransfer)
        return "Success initiation. Results will be available with /getResult request", 200

    return "do some magic!", 200
